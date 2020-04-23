from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.keywords import WaitingKeywords
from .elementkeywords import ElementKeywords
from ..utilities import Utilities as GBUtilies
from ..extended import ExtWebElement
import time

__version__ = '1.0.0'

GB_ATTRIBUTE_NAME = 'data-gb-name'
GB_LOADING = 'gb-name=loading-status'
BG_DROPDOWN_MENU_OPEN = 'dropdown-menu open'

GB_DATE_PICKER_MENU_CLASS = 'datepicker datepicker-dropdown dropdown-menu datepicker-orient-left datepicker-orient-top'
GB_DATE_PICKER_DAYS_CLASS = 'datepicker-days'
GB_DATE_PICKER_MONTHS_CLASS = 'datepicker-months'
GB_DATE_PICKER_YEARS_CLASS = 'datepicker-years'
GB_DATE_PICKER_DECADES_CLASS = 'datepicker-decades'
GB_DATE_PICKER_CENTURIES_CLASS = 'datepicker-centuries'
GB_DATE_PICKER_SWITCH_CLASS = 'datepicker-switch'
GB_DATE_PICKER_NEXT_CLASS = 'next'
GB_DATE_PICKER_PREV_CLASS = 'prev'


class GoBearCoreKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.elementKeys = ElementKeywords(ctx)
        self.waiting_management = WaitingKeywords(ctx)

    def get_element(self, locator, tag=None):
        _locator = GBUtilies.extract_locator(locator)
        if GB_ATTRIBUTE_NAME in _locator[0].lower():
            return self.elementKeys.get_element_by_attribute(GB_ATTRIBUTE_NAME, _locator[1])
        if 'href' in _locator[0].lower():
            return self.elementKeys.get_element_by_href(_locator[1])
        else:
            return ExtWebElement(self.elementKeys.find_element(locator, tag))

    def get_elements(self, locator, tag=None):
        _locator = GBUtilies.extract_locator(locator)
        if GB_ATTRIBUTE_NAME in _locator[0].lower():
            return self.elementKeys.get_elements_by_attribute(GB_ATTRIBUTE_NAME, _locator[1])
        else:
            return [ExtWebElement(e) for e in self.elementKeys.find_elements(locator, tag)]

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
        if not self.get_element(locator).is_contain_class('active'):
            raise AssertionError("Tab %s is not active" % locator)

    @keyword
    def select_button_dropdown(self, locator, value):
        self.wait_until_element_is_visible(locator)
        control = self.get_element(locator)
        # show dropdown list
        control.get_elements_by_tag('button')[0].click()
        self.wait_until_dropdown_menu_visible(control)
        # options are in 'li' tags
        control.select_element_by_tag('li', value)

    def is_dropdown_menu_visible(self, element):
        """
        Check if the dropdown menu of BG Dropdown Button is visible
        :param element:
        """
        return self.elementKeys.is_any_element_contain_class(BG_DROPDOWN_MENU_OPEN, element)

    def wait_until_dropdown_menu_visible(self, control, timeout=None, error=None):
        # constant wait time works better than dynamic function
        # TODO: Need to debug and fix
        time.sleep(0.5)
        # self.waiting_management._wait_until(
        #     lambda: self.is_dropdown_menu_visible(control) == True,
        #     "No dropdown menu is visible <TIMEOUT>",
        #     timeout,
        #     error
        # )

#################### DATE PICKER ##########################

    @keyword
    def set_date(self, locator, value):
        """
        Set date values for date picker
        Support input value in format: dd-mm-yyy or dd/mm/yyy or dd.mm.yyy
        Where 'mm' is month in WORD (ex: April)
        :param locator:
        :param value:
        """
        dates = GBUtilies.split(value, ['/', ' ', '.', '-'])
        day = dates[0]
        month = dates[1]
        year = dates[2]

        # popup date picker
        self.get_element(locator).click()
        self.wait_until_data_picker_popup()

        # get date picker
        date_picker = self.get_date_picker_popup()

        # check if date picker is Days mode
        if self.is_date_picker_days():
            _position = 0
            # get date picker values
            datepicker_switch_value = self.get_date_picker_switch_values()
            current_month = datepicker_switch_value['month'] or None
            current_year = datepicker_switch_value['year'] or None

            if current_year != year:
                self.select_datepicker_year_at(date_picker, day, month, year, _position)
            elif current_month != month:
                self.select_datepicker_month_at(date_picker, day, month, year, _position)
            else:
                # current_month == month and current_year == year
                self.select_datepicker_day_at(date_picker, day, month, year, _position)

        # TODO: Add more cases when Date Picker is at Month screen when popup
        # if self.is_date_picker_months():
        #     _position = 1
            # get month popup
            # current_date_picker = date_picker.get_element_by_class(GB_DATE_PICKER_MONTHS_CLASS)

        # TODO: Add more cases when Date Picker is at Year screen when popup
        # if self.is_date_picker_years():
        #     _position = 2
            # get years popup
            # current_date_picker = date_picker.get_element_by_class(GB_DATE_PICKER_YEARS_CLASS)

    def select_datepicker_year_at(self, datepicker, day, month, year, position=2):
        """
        Select value for Year Date Picker
        :param datepicker:
        :param year:
        :param position: integer number | is where datepicker at
        0: for days, 1: for month, 2: for year
        """
        if position == 0:
            # at Day => click twice on switch
            self.click_date_picker_switch(2)
        if position == 1:
            # at Month => click once on switch
            self.click_date_picker_switch(1)
        self.select_datepicker_value(datepicker, GB_DATE_PICKER_YEARS_CLASS, year)
        self.select_datepicker_value(datepicker, GB_DATE_PICKER_MONTHS_CLASS, month)
        self.select_datepicker_value(datepicker, GB_DATE_PICKER_DAYS_CLASS, day)

    def select_datepicker_month_at(self, date_picker, day, month, year, position=1):
        if position == 0:
            # at Day => click once on switch
            self.click_date_picker_switch(1)
        if position == 2:
            # at Year => select Year
            self.select_datepicker_value(year)
        self.select_datepicker_value(date_picker, GB_DATE_PICKER_MONTHS_CLASS, month)
        self.select_datepicker_value(date_picker, GB_DATE_PICKER_DAYS_CLASS, day)

    def select_datepicker_day_at(self, datepicker, day, month, year, position=0):
        if position == 1:
            # at Month => select Month
            self.select_datepicker_value(datepicker, GB_DATE_PICKER_MONTHS_CLASS, month)
        if position == 2:
            # at Year, select Year then Month
            self.select_datepicker_value(datepicker, GB_DATE_PICKER_YEARS_CLASS, year)
            self.select_datepicker_value(datepicker, GB_DATE_PICKER_MONTHS_CLASS, month)
        self.select_datepicker_value(datepicker, GB_DATE_PICKER_MONTHS_CLASS, day)

    def select_datepicker_value(self, datepicker, picker_class, value):
        current_date_picker = datepicker.get_element_by_class(picker_class)
        if picker_class == GB_DATE_PICKER_DAYS_CLASS:
            values = current_date_picker.find_elements_by_xpath("//tbody//td")
        else:
            values = current_date_picker.find_elements_by_xpath("//tbody//td/span")
        available_values = [v for v in values if not self.elementKeys.is_element_contain_class('disabled', v)]
        for v in available_values:
            if picker_class == GB_DATE_PICKER_MONTHS_CLASS:
                value = GBUtilies.month_lname_to_sname(value)
            if v.get_textContent() == value:
                v.click()
                return
        message = "Cannot select value %s" % value
        raise AssertionError(message)

    def click_date_picker_switch(self, times=1):
        for i in range(0, times):
            self.get_date_picker_switch().click()
            time.sleep(0.25)

    def get_date_picker_switch(self):
        if self.is_date_picker_days():
            picker_class = GB_DATE_PICKER_DAYS_CLASS
        elif self.is_date_picker_months():
            picker_class = GB_DATE_PICKER_MONTHS_CLASS
        else:
            picker_class = GB_DATE_PICKER_YEARS_CLASS
        current_picker = self.elementKeys.find_element_by_class(picker_class)
        return current_picker.get_element_by_class(GB_DATE_PICKER_SWITCH_CLASS)

    def get_date_picker_switch_values(self):
        datepicker_switch = self.get_date_picker_switch()
        _raw = datepicker_switch.get_textContent()
        if ' ' in _raw:
            values = _raw.split(' ')
            return {'month': values[0], 'year': values[1]}
        elif '-' in _raw:
            values = _raw.split('-')
            return {'start': values[0], 'end': values[1]}
        else:
            return {'year': _raw}

    def is_date_picker_days(self):
        try:
            return self.elementKeys.find_element_by_class(GB_DATE_PICKER_DAYS_CLASS).is_displayed()
        except:
            return False

    def is_date_picker_months(self):
        try:
            return self.elementKeys.find_element_by_class(GB_DATE_PICKER_MONTHS_CLASS).is_displayed()
        except:
            return False

    def is_date_picker_years(self):
        try:
            return self.elementKeys.find_element_by_class(GB_DATE_PICKER_YEARS_CLASS).is_displayed()
        except:
            return False

    def get_date_picker_popup(self):
        return self.elementKeys.find_element_by_class(GB_DATE_PICKER_MENU_CLASS)

    def is_date_picker_popup(self):
        return self.elementKeys.is_any_element_contain_class(GB_DATE_PICKER_MENU_CLASS)

    def wait_until_data_picker_popup(self, timeout=None, error=None):
        self.waiting_management._wait_until(
            lambda: self.is_date_picker_popup() == True,
            "No date picker is popup <TIMEOUT>",
            timeout,
            error
        )

