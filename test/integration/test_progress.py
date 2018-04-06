from pages.desktop.home import Home


def test_progress(selenium, base_url, download_location_dir, test_file):
    """Test progress icon shows while uploading."""
    home = Home(selenium, base_url).open()
    test_file.location.write('This is a test!')
    assert home.upload_area("{0}".format(test_file.location.realpath()))
