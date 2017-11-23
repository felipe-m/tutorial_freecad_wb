# -*- coding: utf-8 -*-
# FreeCAD init script of the Basic 4 module,
# simple workbench, 4 commands

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


class Basic4Workbench (Workbench):
    """Basic 4 workbench object"""
    # this is the icon in XPM format 16x16 pixels 
    Icon = """
    /* XPM */
    static char * basic4_xpm[] = {
    "16 16 10 1",
    " 	c None",
    ".	c #FFFFFF",
    "+	c #000000",
    "@	c #7F4F00",
    "#	c #FFBF00",
    "$	c #684D00",
    "%	c #EBB000",
    "&	c #9F7700",
    "*	c #D39E00",
    "=	c #FBBC00",
    "................",
    "...++++++++++++.",
    "..+@#########++.",
    ".+@#########+@+.",
    ".+++++++++++@#+.",
    ".+#########+##+.",
    ".+####$+###+##+.",
    ".+###%++###+##+.",
    ".+###$&+###+##+.",
    ".+##*+=+###+##+.",
    ".+##+&#+###+##+.",
    ".+##+++++##+##+.",
    ".+#####+###+#@+.",
    ".+#########+@+..",
    ".++++++++++++...",
    "................"};
    """
    MenuText = "Basic4"
    ToolTip = "Basic 4 workbench"

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        from PySide import QtCore, QtGui
        # python file where the commands are:
        import Basic4Gui
        # list of commands, 4 (they are in the imported Basic4Gui):
        cmdlist = [ "Basic4_MakeBox",
                    "Basic4_MakeBoxDialog",
                    "Basic4_MakeBoxEdgeP",
                    "Basic4_MakeBoxParam"]
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Basic4", "Basic4")), cmdlist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Basic4", "Basic4")), cmdlist)

        Log ('Loading Basic4 module... done\n')

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# The workbench is added
Gui.addWorkbench(Basic4Workbench())

