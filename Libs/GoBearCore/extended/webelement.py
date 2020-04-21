from selenium.webdriver.remote.webelement import WebElement


def js_click(self):
    """
    Customized click function incase of Selenium's click function does not work
    :param self:
    """
    self.scroll_to_webElement()
    self.parent.execute_script("arguments[0].click();", self)


def scroll_to_webElement(self):
    self.parent.execute_script("arguments[0].scrollIntoView();", self)


def get_textContent(self):
    return self.get_attribute("textContent").strip()


WebElement.js_click = js_click
WebElement.scroll_to_webElement = scroll_to_webElement
WebElement.get_textContent = get_textContent
