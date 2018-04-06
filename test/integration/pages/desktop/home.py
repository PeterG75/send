from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class Home(Base):
    """Addons Home page"""

    _upload_area_locator = (By.ID, 'file-upload')
    _upload_button_locator = (By.CLASS_NAME, 'btn--file')

    @property
    def upload_btn(self):
        return self.find_element(*self._upload_button_locator)

    def upload_area(self, path, cancel=False):
        self.find_element(*self._upload_area_locator).send_keys(path)
        from pages.desktop.progress import Progress
        return Progress(
            self.selenium, self.base_url).wait_for_page_to_load(
                                          cancel_after_load=cancel)
