#
# LocalLib.SFBrowser/SFChromeBrowser
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

from LocalLib.SFBrowser.SFAbstractBrowser import SFAbstractBrowser
from selenium import webdriver


class SFChromeBrowser(webdriver.Chrome,SFAbstractBrowser):

    def __init__(self):
        webdriver.Chrome.__init__(self)
        SFAbstractBrowser.__init__(self)

    def close(self):
        webdriver.Chrome.close(self)
        webdriver.Chrome.quit(self)