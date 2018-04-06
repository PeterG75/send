from pages.desktop.download import Download
from pages.desktop.home import Home


def test_download(selenium, base_url, download_location_dir, test_file):
    """Test downloaded file matches uploaded file."""
    home = Home(selenium, base_url).open()
    test_file.location.write('This is a test!')
    share = home.upload_area("{0}".format(test_file.location.realpath()))
    download = Download(selenium, share.file_url).open()
    download.download_btn.click()
    assert download_location_dir.ensure(test_file.name)
