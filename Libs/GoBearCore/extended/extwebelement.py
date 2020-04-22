from selenium.webdriver.remote.webelement import WebElement


class ExtWebElement(WebElement):
    def __init__(self, we):
        WebElement.__init__(self, we.parent, we.id)

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

    def get_element_contains_text(self, value, tag='*'):
        return self.find_element("//"+tag+"[contains(text(),'"+value+"')]")

    def get_element_by_tag(self, tag='*'):
        return self.get_elements_by_tag(tag)[0]

    def get_elements_by_tag(self, tag='*'):
        return [ExtWebElement(e) for e in self.find_elements_by_tag_name(tag)]

    def select_element_by_tag(self, tag, value):
        for e in self.get_elements_by_tag(tag):
            if value in e.get_textContent():
                e.click()
                return
        message = "Element '%s = %s' not found!" % (tag, value)
        raise AssertionError(message)

    def is_contain_class(self, class_name):
        return class_name in self.get_attribute('class')

    def get_element_by_class(self, class_name):
        return ExtWebElement(self.find_element("//*[@class="+class_name+"]"))
