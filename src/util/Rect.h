/**	Rect.h - ZScratch
*	Copyright(C) 2017-2018 Alex Cui
*
*	This program is free software : you can redistribute it and/or modify
*	it under the terms of the GNU Affero General Public License as
*	published by the Free Software Foundation, either version 3 of the
*	License, or (at your option) any later version.
*
*	This program is distributed in the hope that it will be useful,
*	but WITHOUT ANY WARRANTY; without even the implied warranty of
*	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
*	GNU Affero General Public License for more details.
*
*	You should have received a copy of the GNU Affero General Public License
*	along with this program.If not, see <https://www.gnu.org/licenses/>.
*/

/**
* Rect.h
* Alex Cui, March 2018
*
* Useful class for RECT(Windows.h).
*/

#pragma once
#ifndef UTIL_RECT
#define UTIL_RECT
#include <Windows.h>
class Rect: public RECT {
public:
	Rect();
	~Rect();

	LONG width();
	LONG height();
};
#endif

