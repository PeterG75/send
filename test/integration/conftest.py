# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""Configuration files for pytest."""
import pytest
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


# @pytest.fixture
# def firefox_options(firefox_options, download_location_dir):
#     """Firefox options."""
#     firefox_options.set_preference(
#         'extensions.install.requireBuiltInCerts', False)
#     firefox_options.set_preference('xpinstall.signatures.required', False)
#     firefox_options.set_preference('extensions.webapi.testing', True)
#     firefox_options.set_preference('ui.popup.disable_autohide', True)
#     firefox_options.set_preference("browser.download.panel.shown", False)
#     firefox_options.set_preference(
#         "browser.helperApps.neverAsk.openFile", "text/plain")
#     firefox_options.set_preference(
#         "browser.helperApps.neverAsk.saveToDisk", "text/plain")
#     firefox_options.set_preference("browser.download.folderList", 2)
#     firefox_options.set_preference(
#         "browser.download.dir", "{0}".format(download_location_dir))
#     firefox_options.add_argument('-foreground')
#     firefox_options.log.level = 'trace'
#     return firefox_options


@pytest.fixture(scope='session', autouse=True)
def _verify_url(request, base_url):
    """Verifies the base URL"""
    verify = request.config.option.verify_base_url
    if base_url and verify:
        session = requests.Session()
        retries = Retry(backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504])
        session.mount(base_url, HTTPAdapter(max_retries=retries))
        session.get(base_url, verify=False)


@pytest.fixture
def download_location_dir(tmpdir):
    return tmpdir.mkdir('test_download')


@pytest.fixture
def upload_location_dir(tmpdir):
    return tmpdir.mkdir('test_upload')


@pytest.fixture
def test_file(upload_location_dir):
    setattr(test_file, 'name', 'sample.txt')
    setattr(test_file, 'location', upload_location_dir.join(test_file.name))
    return test_file
