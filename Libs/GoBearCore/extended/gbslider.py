from .extwebelement import ExtWebElement
from selenium.webdriver.common.action_chains import ActionChains


SLIDER_SLIDER_HANDLE_MIN = 'slider-handle min-slider-handle round'
SLIDER_SLIDER_HANDLE_MAX = 'slider-handle max-slider-handle round'
SLIDER_SLIDER_SELECTION_BAR = 'slider-selection'
SLIDER_SLIDER_MAX_VALUE = 'pull-right value'
SLIDER_SLIDER_VALUE_ATTRIBUTE = 'data-max-value'


class GBSliderGroup(ExtWebElement):
    def __init__(self, we):
        ExtWebElement.__init__(self, we)
        self.items = self.get_item_map()

    def get_item_map(self):
        item_map = {}
        label_list = self.get_elements_by_tag('label')
        for l in label_list:
            item_map[l.get_textContent().lower()] = GBSlider(l.get_following_neighbor())
        return item_map

    def get_slider_by_label(self, label):
        return self.items[label.lower()]


class GBSlider(ExtWebElement):
    def __init__(self, we):
        ExtWebElement.__init__(self, we)

    def get_max_value(self):
        return float(self.get_element_by_class(SLIDER_SLIDER_MAX_VALUE).get_attribute(SLIDER_SLIDER_VALUE_ATTRIBUTE))

    def get_min_handle(self):
        return self.get_element_by_class(SLIDER_SLIDER_HANDLE_MIN)

    def get_max_handle(self):
        return self.get_element_by_class(SLIDER_SLIDER_HANDLE_MAX)

    def get_selection_bar(self):
        return self.get_element_by_class(SLIDER_SLIDER_SELECTION_BAR)

    def get_selection_bar_width(self):
        return self.get_selection_bar().get_offset('width')

    def set_min_value(self, value):
        action = ActionChains(self.parent)
        distance = float(value)*(self.get_selection_bar_width())/self.get_max_value()
        action.click_and_hold(self.get_min_handle()).move_by_offset(distance, 0).release().perform()

    def set_max_value(self, value):
        action = ActionChains(self.parent)
        size = self.get_selection_bar_width()
        distance = float(value)*(size)/self.get_max_value()
        action.click_and_hold(self.get_max_handle()).move_by_offset(distance-size, 0).release().perform()
