#############################################################################################
#
# Test Factory For ArrayField :
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
from LocalLib.SeleniumShortcuts import SeleniumShortcuts
from LocalLib.SFBrowser.SFChromeBrowser import SFChromeBrowser
from TestResources.TestResManager import TestResManager
import pytest


# import selenium.webdriver.common.by


@pytest.fixture(scope="module", autouse=True)
def create_browser():
    pytest.common_browser = SFChromeBrowser()
    yield
    pytest.common_browser.close()


def test_simple_selectors():
    browser = pytest.common_browser
    browser.get(TestResManager.web_resource_url('simple_select'))
    match_type = "name"
    match_string = "simple_select[]"
    field = SFFieldFactory.create( "array_{},{},{},{}".format(match_type,'bob' ,match_type,match_string) )
    assert len(field.get_element(browser)) == 6


@pytest.mark.parametrize("index,expect", [
    (0,'option 0'),
    (1,'option 1'),
    (2,'option 2'),
    (3,'option 3'),
    (4,'option 4'),
    (5,'option 5'),
])
def test_simple_selector_values(index,expect):
    """
    Test against a simple HTML multi select, each item has the name value "simple_select[]"
    :param index: select index
    :param expect: The Text in the matching item
    """
    browser = pytest.common_browser
    browser.get(TestResManager.web_resource_url('simple_select'))
    match_type = "name"
    match_string = "simple_select[]"

    field = SFFieldFactory.create( "array_{},{},{},{}".format(match_type,'bob' ,match_type,match_string) )
    elem = field.get_element(browser,index)
    assert not isinstance(elem,list)
    assert expect == field.get_value(browser,index)


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
    For array items this should return a list by default, or the actual element
    if an index is specified
    :param match_string: selenium match pattern
    :param match_type: selenium match type (eg css...)
    :param expected: Text that is in the field
    """
    browser = pytest.common_browser
    browser.get(TestResManager.web_resource_url('simple_page'))

    #
    #   test using supplied (short) string
    #
    field = SFFieldFactory.create( "array_{},{},{},{}".format(match_type,'bob' ,match_type,match_string) )
    assert isinstance(field.get_element(browser),list)
    assert not isinstance(field.get_element(browser,0),list)
    assert field.get_value(browser,0) == expected


    #
    #   test using selenium match string
    #
    match_type = SeleniumShortcuts.get_selector(match_type)
    field = SFFieldFactory.create( "array_{},{},{},{}".format(match_type,'bob' ,match_type,match_string) )
    assert isinstance(field.get_element(browser),list)
    assert not isinstance(field.get_element(browser,0),list)
    assert field.get_value(browser,0) == expected
