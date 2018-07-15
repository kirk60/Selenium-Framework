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

class SeleniumShortcuts(object):

    valid_selectors = [
        selenium.webdriver.common.by.By.CLASS_NAME,
        selenium.webdriver.common.by.By.CSS_SELECTOR,
        selenium.webdriver.common.by.By.ID,
        selenium.webdriver.common.by.By.LINK_TEXT,
        selenium.webdriver.common.by.By.NAME,
        selenium.webdriver.common.by.By.PARTIAL_LINK_TEXT,
        selenium.webdriver.common.by.By.TAG_NAME,
        selenium.webdriver.common.by.By.XPATH
    ]

    @staticmethod
    def is_selector(sel):
        return sel in SeleniumShortcuts.valid_selectors

    @staticmethod
    def all_selectors():
        return SeleniumShortcuts.valid_selectors
