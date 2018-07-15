#
# TestResources/TestResManager
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


import os

class TestResManager(object):

    res_root = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def web_resource_url(file_name):
        full_name = os.path.join(TestResManager.res_root,'web_pages',file_name + '.html')
        return "file://" + full_name

