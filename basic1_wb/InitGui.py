# -*- coding: utf-8 -*-
# FreeCAD init script of the Basic 1 module,
# very simple workbench, just for the tutorial

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


class Basic1Workbench (Workbench):
    """Basic 1 workbench object"""
    # this is the icon in XPM format 16x16 pixels 
    Icon = """
    /* XPM */
    static char * basic1_xpm[] = {
    "16 16 5 1",
    " 	c None",
    ".	c #FFFFFF",
    "+	c #000000",
    "@	c #7F4F00",
    "#	c #FFBF00",
    "................",
    "...++++++++++++.",
    "..+@#########++.",
    ".+@#########+@+.",
    ".+++++++++++@#+.",
    ".+#########+##+.",
    ".+###++####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+###+++###+#@+.",
    ".+#########+@+..",
    ".++++++++++++...",
    "................"};
    """

    MenuText = "Basic1"
    ToolTip = "Basic 1 workbench"

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        from PySide import QtCore, QtGui
        # python file where the commands are:
        import Basic1Gui
        # list of commands, only one (it is in the imported Basic1Gui):
        cmdlist = [ "Basic1_MakeBox"]
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Basic1", "Basic1")), cmdlist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Basic1", "Basic1")), cmdlist)

        #FreeCADGui.addIconPath(":/icons")
        Log ('Loading Basic1 module... done\n')

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# The workbench is added
Gui.addWorkbench(Basic1Workbench())

