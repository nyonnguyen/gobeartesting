from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.keywords import ElementKeywords as SeleniumElementKeywords
from selenium.webdriver.common.keys import Keys
from SeleniumLibrary.keywords import WaitingKeywords
from ..extended import ExtWebElement


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
    def find_child_element_by_tag_and_attribute(self, element, tag, attribute_name, attribute_value):
        child_elements = element.find_elements_by_tag_name(tag)
        for child in child_elements:
            if child.get_attribute(attribute_name).strip() == attribute_value:
                return ExtWebElement(child)
        message = "Child element '%s = %s' not found!" % (attribute_name, attribute_value)
        raise AssertionError(message)

    @keyword
    def find_element_by_attribute(self, attribute, value, tag='*'):
        # return self.find_elements_by_attribute(attribute, value, tag)[0]
        e = self.find_elements_by_attribute(attribute, value, tag)[0]
        print(e)
        return e

    @keyword
    def find_elements_by_attribute(self, attribute, value, tag='*'):
        return [ExtWebElement(e) for e in self.SEKeywords.find_elements("//" + tag + "[@" +
                                                                        attribute + "='" + value + "']")]

    def is_any_element_contain_class(self, class_name, element=None):
        try:
            self.find_element_by_class(class_name, element)
            return True
        except:
            return False

    def find_element_by_class(self, class_name, element=None):
        return ExtWebElement(self.find_element("//*[contains(@class, '"+class_name+"')]", None, None, element))

    def find_element_by_href(self, value):
        return ExtWebElement(self.find_element_by_attribute("href", value, tag='a'))
