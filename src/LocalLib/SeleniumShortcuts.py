#
# LocalLib/SeleniumShortcuts : simple shortcuts for selenium
#
# Copyright (C) 2018  Kirk Larson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import selenium.webdriver.common.by
from typing import List

class SeleniumShortcuts(object):

    selector_map = {
        'class': selenium.webdriver.common.by.By.CLASS_NAME,
        'css' : selenium.webdriver.common.by.By.CSS_SELECTOR,
        'id' : selenium.webdriver.common.by.By.ID,
        'linktext' : selenium.webdriver.common.by.By.LINK_TEXT,
        'name' : selenium.webdriver.common.by.By.NAME,
        'partlink' : selenium.webdriver.common.by.By.PARTIAL_LINK_TEXT,
        'tag' : selenium.webdriver.common.by.By.TAG_NAME,
        'xpath' : selenium.webdriver.common.by.By.XPATH
    }


    @staticmethod
    def is_selector(sel:str)-> bool:
        return sel in SeleniumShortcuts.selector_map.values()

    @staticmethod
    def all_selectors_long() -> List[str]:
        return SeleniumShortcuts.selector_map.values()

    @staticmethod
    def all_selectors_short()  -> List[str]:
        return SeleniumShortcuts.selector_map.keys()

    @staticmethod
    def get_selector(name:str) -> str:
        if name in SeleniumShortcuts.all_selectors_short():
            return SeleniumShortcuts.selector_map[name]

        if name in SeleniumShortcuts.all_selectors_long():
            return name

        raise LookupError("Unknown selector type '{}'".format(name))


