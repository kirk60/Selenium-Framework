#############################################################################################
#
# Test Factory For Field :
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
#############################################################################################


from LocalLib.SFFieldFactory import SFFieldFactory
from LocalLib.SFBrowser.SFChromeBrowser import SFChromeBrowser
from TestResManager import TestResManager
from LocalLib.SeleniumShortcuts import SeleniumShortcuts

import pytest


# import selenium.webdriver.common.by


@pytest.fixture(scope="module", autouse=True)
def create_browser():
    pytest.common_browser = SFChromeBrowser()
    yield
    pytest.common_browser.close()


@pytest.mark.parametrize("match_string,match_type,expected", [
    ("simple_class", 'class', 'simple class text'),
    ("body > div:nth-child(3)", 'css', 'simple css text'),
    ("id_field", 'id', 'simple id text'),
    ("simple linktext text", 'linktext', 'simple linktext text'),
    ("name_field", 'name', 'simple name text'),
    ("partlink", 'partlink', 'simple partlink text'),
    ("textarea", 'tag', 'simple textarea text'),
    ("/html/body/div[5]", 'xpath', 'simple xpath text'),
])
def test_all_selectors(match_string, match_type, expected):
    """
    basic test of selectors, using full selector description & the short form
    :param match_string: selenium match pattern
    :param match_type: selenium match type (eg css...)
    :param expected: Text that is in the field
    :return:
    """
    browser = pytest.common_browser
    browser.get(TestResManager.web_resource_url('simple_page'))

    #
    #   test using supplied (short) string
    #
    field = SFFieldFactory.create_from_csv( "{},{},{},{}".format(match_type,'bob' ,match_type,match_string) )
    field.get_element(browser)
    assert field.get_value(browser) == expected

    #
    #   test using long string
    #
    match_type = SeleniumShortcuts.get_selector(match_type)
    field = SFFieldFactory.create_from_csv( "{},{},{},{}".format(match_type,'bob' ,match_type,match_string) )
    field.get_element(browser)
    assert field.get_value(browser) == expected

