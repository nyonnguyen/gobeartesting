from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.keywords import ElementKeywords as SeleniumElementKeywords
from selenium.webdriver.common.keys import Keys
from SeleniumLibrary.keywords import WaitingKeywords


class ElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.SEKeywords = SeleniumElementKeywords(ctx)
        self.waiting_management = WaitingKeywords(ctx)

    @keyword
    def clear_textfield_value(self, locator):
        text = self.SEKeywords.get_value(locator)
        i = 0
        while i < len(text):
            i += 1
            self.SEKeywords.press_key(locator, Keys.BACK_SPACE)
            self.SEKeywords.press_key(locator, Keys.DELETE)

    @keyword
    def get_child_element_by_tag_and_attribute(self, element, tag, attribute_name, attribute_value):
        child_elements = element.find_elements_by_tag_name(tag)
        for child in child_elements:
            if child.get_attribute(attribute_name).strip() == attribute_value:
                return child
        message = "Child element '%s = %s' not found!" % (attribute_name, attribute_value)
        raise AssertionError(message)

    @keyword
    def get_element_by_attribute(self, attribute, value, tag='*'):
        return self.get_elements_by_attribute(attribute, value, tag)[0]

    @keyword
    def get_elements_by_attribute(self, attribute, value, tag='*'):
        return self.SEKeywords.find_elements("//" + tag + "[@" + attribute + "='" + value + "']")

    def get_element_by_tag(self, element, tag):
        return self.find_element(element).find_elements_by_tag_name(tag)

    def select_element_by_tag(self, element, tag, value):
        for e in self.get_element_by_tag(element, tag):
            if value in e.get_textContent():
                e.click()
                return
        message = "Element '%s = %s' not found!" % (tag, value)
        raise AssertionError(message)

    def is_contain_class(self, class_name, locator=None):
        # return class_name in self.find_element(locator).get_attribute('class')
        try:
            self.get_element_by_class(class_name, locator)
            return True
        except:
            return False

    def get_element_by_class(self, class_name, locator=None):
        return self.find_element("//*[contains(@class='"+class_name+"']", None, None, locator)

    def get_element_by_href(self, value):
        return self.get_element_by_attribute("href", value, tag='a')

    def get_element_contains_text(self, locator, value, tag='*'):
        return self.find_element("//"+tag+"[contains(text(),'"+value+"')]", None, None, locator)
