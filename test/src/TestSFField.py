#############################################################################################
#
# Test SFField :
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


from LocalLib.SFField import SFField
from LocalLib.SeleniumShortcuts import SeleniumShortcuts
from LocalLib.SFBrowser.SFChromeBrowser import SFChromeBrowser
from TestResources.TestResManager import TestResManager
import selenium.webdriver.common.by
import pytest


# import selenium.webdriver.common.by


@pytest.fixture(scope="module", autouse=True)
def create_browser():
    pytest.common_browser = SFChromeBrowser()
    yield
    pytest.common_browser.close()


def test_constructor():
    """
    Basic Constructor test
    """
    for type in SeleniumShortcuts.all_selectors():
        SFField('name', "fred", type)


@pytest.mark.parametrize("match_string,match_type,expected", [
    ("simple_class", selenium.webdriver.common.by.By.CLASS_NAME, 'simple class text'),
])
def test_all_selectors(match_string, match_type, expected):
    browser = pytest.common_browser
    browser.get(TestResManager.web_resource_url('simple_page'))
    field = SFField('bob', match_string, match_type)
    elem = field.get_element(browser)
    assert elem.text == expected
