from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.keywords import WaitingKeywords
from .elementkeywords import ElementKeywords
from ..utilities import Utilities as ufnc


__version__ = '1.0.0'

GB_ATTRIBUTE_NAME = 'data-gb-name'
GB_LOADING = 'gb-name=loading-status'
BG_DROPDOWN_MENU_OPEN = 'dropdown-menu open'
GB_DATE_PICKER_MENU_CLASS = 'datepicker datepicker-dropdown dropdown-menu datepicker-orient-left datepicker-orient-top'


class GoBearCoreKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.elementKeys = ElementKeywords(ctx)
        self.waiting_management = WaitingKeywords(ctx)

    # def click(self, element):
    #     self.elementKeys.js_click(element)

    def get_element(self, locator, tag=None):
        _locator = ufnc.extract_locator(locator)
        if GB_ATTRIBUTE_NAME in _locator[0].lower():
            return self.elementKeys.get_element_by_attribute(GB_ATTRIBUTE_NAME, _locator[1])
        if 'href' in _locator[0].lower():
            return self.elementKeys.get_element_by_href(_locator[1])
        else:
            return self.elementKeys.find_element(locator, tag)

    def get_elements(self, locator, tag=None):
        _locator = ufnc.extract_locator(locator)
        if GB_ATTRIBUTE_NAME in _locator[0].lower():
            return self.elementKeys.get_element_by_attribute(GB_ATTRIBUTE_NAME, _locator[1])
        else:
            return self.elementKeys.find_element(locator, tag)

    @keyword
    def select_element(self, locator):
        self.get_element(locator).click()

    @keyword
    def select_gb_element(self, locator):
        self.find_element(locator).click()

    def is_loading(self, locator=GB_ATTRIBUTE_NAME):
        loader = self.get_element(locator)
        return loader.is_displayed()

    @keyword
    def wait_until_loaded(self, timeout=None, error=None):
        self.waiting_management._wait_until(
            lambda: self.is_loading() == False,
            "Web is loading too long '<TIMEOUT>'",
            timeout,
            error
        )

    # @keyword
    # def wait_until_gb_element_visible(self, locator):
    #     gb_element = self.get_element(locator)
    #     self.waiting_management.wait_until_element_is_visible(gb_element)

    def is_element_visible(self, locator):
        try:
            self.get_element(locator)
            return True
        except:
            return False

    @keyword
    def wait_until_element_is_visible(self, locator, timeout=None, error=None):
        self.waiting_management._wait_until(
            lambda: self.is_element_visible(locator) == True,
            "Element %s is not visible <TIMEOUT>" % locator,
            timeout,
            error
        )

    @keyword
    def tab_should_be_active(self, locator):
        if not self.elementKeys.is_contain_class('active', locator):
            raise AssertionError("Tab %s is not active" % locator)

    @keyword
    def select_button_dropdown(self, locator, value):
        self.wait_until_element_is_visible(locator)
        control = self.get_element(locator)
        # show dropdown list
        self.elementKeys.get_element_by_tag(control, 'button')[0].click()
        self.wait_until_dropdown_menu_visible(control)
        # options are in 'li' tags
        self.elementKeys.select_element_by_tag(control, 'li', value)

    def is_dropdown_menu_visible(self, element):
        """
        Check if the dropdown menu of BG Dropdown Button is visible
        :param element:
        """
        try:
            self.find_element("//*[@class='"+BG_DROPDOWN_MENU_OPEN+"']", None, None, element)
            return True
        except:
            return False
        # return self.elementKeys.is_contain_class(element, BG_DROPDOWN_MENU_OPEN)

    def wait_until_dropdown_menu_visible(self, control, timeout=None, error=None):
        self.waiting_management._wait_until(
            lambda: self.is_dropdown_menu_visible(control) == True,
            "No dropdown menu is visible <TIMEOUT>",
            timeout,
            error
        )

    @keyword
    def set_date(self, locator, value):
        # popup date picker
        self.elementKeys.find_element(locator).click()
        self.wait_until_data_picker_popup()
        print(self.get_date_picker_popup())

    def get_date_picker_popup(self):
        return self.elementKeys.get_element_by_class(GB_DATE_PICKER_MENU_CLASS)

    def is_date_picker_popup(self):
        return self.elementKeys.is_contain_class(self.driver, GB_DATE_PICKER_MENU_CLASS)

    def wait_until_data_picker_popup(self, timeout=None, error=None):
        self.waiting_management._wait_until(
            lambda: self.is_date_picker_popup() == True,
            "No date picker is popup <TIMEOUT>",
            timeout,
            error
        )

    # @keyword
    # def click_on_product_item(self, locator, product_name, product_price):
    #     """
    #     :locator: Locator of the tab container
    #     :product_name: Displayed name of product
    #     "product_price: Displayed price of product"
    #     """
    #     items = self.get_all_product_in_tab(locator)
    #     for i in items:
    #         if self.get_product_name(i) == product_name:
    #             if self.get_product_price(i) == product_price:
    #                 self.click(self.get_product_clickable_item(i))
    #                 return
    #     message = "Item %s - %s not found in %s!" % (product_name, product_price, locator)
    #     raise AssertionError(message)
    #
    # def get_product_url(self, element):
    #     return self._get_child_element_by_property(element).get_attribute("href").strip()
    #
    # def get_product_clickable_item(self, element):
    #     return self._get_child_element_by_property(element, "url")
    #
    # def get_product_name(self, element):
    #     return self._get_child_element_by_property(element, "name").get_attribute("textContent").strip()
    #
    # def get_product_price(self, element):
    #     return self._get_child_element_by_property(element, "price").get_attribute("textContent").strip().replace("$","")
    #
    # def _get_child_element_by_property(self, locator, property):
    #     return self.find_element(locator).find_element_by_xpath(".//*[@itemprop='"+property+"']")
    #
    # @keyword
    # def get_alert_div(self):
    #     return self.driver.find_element_by_xpath("//*[@id='center_column']//*[@class='alert alert-danger']") #get the first element
    #
    # @keyword
    # def is_alert_visible(self):
    #     try:
    #         self.get_alert_div()
    #         return True
    #     except:
    #         return False
    #
    # @keyword
    # def wait_until_alert_displayed(self, timeout=None, error=None):
    #     self.waiting_management._wait_until(
    #         lambda: self.is_alert_visible() == True,
    #         "Alert was not appeared in <TIMEOUT>",
    #         timeout,
    #         error
    #     )
    #
    # @keyword
    # def get_login_alert_messages(self):
    #     alert = self.get_alert_div()
    #     return [li.get_attribute("textContent").strip() for li in alert.find_elements_by_tag_name("li")]
    #
    # @keyword
    # def is_error_message(self, error_message):
    #     messages = self.get_login_alert_messages()
    #     if error_message in messages:
    #         pass
    #     else:
    #         raise AssertionError("Message '{}' is not found".format(error_message))
