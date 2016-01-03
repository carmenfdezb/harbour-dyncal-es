#!/bin/bash
#
#    DynCal - Sailfish OS calendar icon will show you the current day of the month.
#    Copyright (C) 2015  fravaccaro fravaccaro90@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

ls /usr/share/harbour-dyncal-es/icons/ > /usr/share/harbour-dyncal-es/backup.txt
for file in $(</usr/share/harbour-dyncal-es/backup.txt); do cp "/usr/share/harbour-dyncal/icons/$file" /usr/share/harbour-dyncal-es/backup/; done
cp /usr/share/harbour-dyncal-es/icons/*.* /usr/share/harbour-dyncal/icons/

exit 0