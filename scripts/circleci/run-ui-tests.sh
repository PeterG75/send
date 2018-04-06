#!/bin/bash
set -ex

IS_PONTOON=$(git show -s --format=%s | grep -q 'Pontoon:' && echo 'true' || echo '')
if [[ $IS_PONTOON ]]; then
  echo "Skipping Integration Tests on Pontoon commit.";
  exit 0;
fi

GECKODRIVER_URL=$(
  curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' |
  python -c "import sys, json; r = json.load(sys.stdin); print([a for a in r['assets'] if 'linux64' in a['name']][0]['browser_download_url']);"
);


curl -L -o geckodriver.tar.gz $GECKODRIVER_URL
gunzip -c geckodriver.tar.gz | tar xopf -
chmod +x geckodriver
sudo mv geckodriver /bin
geckodriver --version
# Install pip
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade setuptools

sudo pip install tox mozdownload mozinstall
easy_install --upgrade six

mkdir -p ~/project/firefox-downloads/
find  ~/project/firefox-downloads/ -type f -mtime +90 -delete
mozdownload --version latest --type daily --destination ~/project/firefox-downloads/firefox_nightly/

# Dependencies for firefox
sudo apt-get install -y libgtk3.0-cil-dev libasound2 libasound2 libdbus-glib-1-2 libdbus-1-3
sudo mozinstall $(ls -t ~/project/firefox-downloads/firefox_nightly/*.tar.bz2 | head -1)
export PATH=/home/ubuntu/send/firefox/firefox:$PATH
firefox --version
tox -e ui-tests
