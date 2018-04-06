from pages.desktop.home import Home


def test_upload(selenium, base_url, download_location_dir, test_file):
    """Test file upload and creates URL."""
    home = Home(selenium, base_url).open()
    test_file.location.write('sample, sample, sample')
    share = home.upload_area("{0}".format(test_file.location.realpath()))
    assert share.file_url is not None
