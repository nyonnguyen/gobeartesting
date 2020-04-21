import re


class Utilities:

    def extract_locator(locator):
        _locator = locator.split('=')
        return _locator[0], _locator[1]
