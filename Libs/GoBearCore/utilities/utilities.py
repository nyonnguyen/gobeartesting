import re
import calendar

MONTH_LONG_NAMES = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
               'august', 'september', 'october', 'november', 'december']


class Utilities:

    def extract_locator(locator):
        _locator = locator.split('=')
        return _locator[0], _locator[1]

    def split(input, separators):
        for s in separators[1:]:
            new_value = input.replace(s, separators[0])
        return [v.strip() for v in new_value.split(separators[0])]

    def month_name_to_num(name):
        try:
            return MONTH_LONG_NAMES.index(name.lower()) + 1
        except:
            return -1

    def month_num_to_name(num):
        try:
            return MONTH_LONG_NAMES[num - 1].title()
        except:
            return
