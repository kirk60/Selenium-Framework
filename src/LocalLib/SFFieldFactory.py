#
# LocalLib/SFFieldFactory
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

from LocalLib.SFArrayField import SFArrayField
from LocalLib.SFField import SFField
from LocalLib.SeleniumShortcuts import SeleniumShortcuts


class SFFieldFactory(object):
    factories = {}

    @staticmethod
    def addFactory(id, fact):
        SFFieldFactory.factories[id] = fact

    @staticmethod
    def create_from_csv(argument):
        fields = argument.split(",", 1)
        type = fields[0]

        if fields[0] in SFFieldFactory.factories:
            return SFFieldFactory.factories[fields[0]](fields[1])
        return None


#
#   defaults are to add all selectors as selector long/short name
#   and the same as an array
#
for name in SeleniumShortcuts.all_selectors_long():
    SFFieldFactory.addFactory(name, SFField)
    SFFieldFactory.addFactory("array_" + name, SFArrayField)

for name in SeleniumShortcuts.all_selectors_short():
    SFFieldFactory.addFactory(name, SFField)
    SFFieldFactory.addFactory("array_" + name, SFArrayField)
