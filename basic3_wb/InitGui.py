# -*- coding: utf-8 -*-
# FreeCAD init script of the Basic 3 module,
# simple workbench, 3 commands

#***************************************************************************
#*   (c) Felipe Machado    https://github.com/felipe-m  2017               *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/


class Basic3Workbench (Workbench):
    """Basic 3 workbench object"""
    # this is the icon in XPM format 16x16 pixels 
    Icon = """
    /* XPM */
    static char * basic3_xpm[] = {
    "16 16 7 1",
    " 	c None",
    ".	c #FFFFFF",
    "+	c #000000",
    "@	c #7F4F00",
    "#	c #FFBF00",
    "$	c #B88900",
    "%	c #6E5200",
    "................",
    "...++++++++++++.",
    "..+@#########++.",
    ".+@#########+@+.",
    ".+++++++++++@#+.",
    ".+#########+##+.",
    ".+##$++$###+##+.",
    ".+##%#$+###+##+.",
    ".+####$+###+##+.",
    ".+###++$###+##+.",
    ".+####$+###+##+.",
    ".+##%#$+###+##+.",
    ".+##$++$###+#@+.",
    ".+#########+@+..",
    ".++++++++++++...",
    "................"};
    """
    MenuText = "Basic3"
    ToolTip = "Basic 3 workbench"

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        from PySide import QtCore, QtGui
        # python file where the commands are:
        import Basic3Gui
        # list of commands, just 3 (they are in the imported Basic3Gui):
        cmdlist = [ "Basic3_MakeBox",
                    "Basic3_MakeBoxDialog",
                    "Basic3_MakeBoxEdgeP"]
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Basic3", "Basic3")), cmdlist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Basic3", "Basic3")), cmdlist)

        Log ('Loading Basic3 module... done\n')

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# The workbench is added
Gui.addWorkbench(Basic3Workbench())

