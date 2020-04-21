import re


class Utilities:

    def extract_locator(locator):
        _locator = locator.split('=')
        return _locator[0], _locator[1]

    def split(input, separators):
        for s in separators[1:]:
            new_value = input.replace(s, separators[0])
        return [v.strip() for v in new_value.split(separators[0])]
