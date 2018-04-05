#   Scratch.py - ZScratch
#   Copyright(C) 2017-2018 Alex Cui
#
#	This program is free software : you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.If not, see <https://www.gnu.org/licenses/>.
#
#   =============================================
#   Scratch.py
#   Alex Cui, March 2018
#
#   The interface of scratch for python.
#   =============================================

class ScratchExtension(object):
    extid = str();
    exttitle = str();
    def __init__(self):
        return super().__init__()
    def pre_init(self):
        pass
    def init(self):
        pass
    def post_init(self):
        pass
    pass
