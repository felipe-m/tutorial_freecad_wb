# -*- coding: utf-8 -*-
# FreeCAD script for the commands of the basic workbench creation tutorial
# (c) 2017 Felipe Machado

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

import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui
import Part
import os

from DraftTools import translate

__dir__ = os.path.dirname(__file__)

# FreeCAD Command made with a Python script
def MakeBox():
    doc = FreeCAD.ActiveDocument
    box =  doc.addObject("Part::Box",'box')
    box.Length = 1
    box.Width  = 1
    box.Height = 1

# GUI command that links the Python script
class _MakeBoxCmd:
    """Command to create a box"""

    def Activated(self):
        # what is done when the command is clicked
        MakeBox()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic2_Box',
            'Box 1 1 1')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic2_Box',
            'Creates a new box')
        return {
            'Pixmap': __dir__ + '/icons/basic2_makebox_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

# ---------- classes to make a box with a dialog

# Task Panel creation: the task panel has to have:
#   1. a widget called self.form
#   2. reject and accept methods (if needed)
class BoxSimpleTaskPanel:
    def __init__(self,widget):
        self.form = widget

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        MakeBox()
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script
class _MakeBoxDialogCmd:
    """Command to create a box with a very simple dialog
    """

    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = BoxSimpleTaskPanel(baseWidget)
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic2_DBox',
            'Box Dialog')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic2_DBox',
            'Creates a box using a task panel dialog')
        return {
            'Pixmap': __dir__ + '/icons/basic2_makeboxdialog_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Basic2_MakeBox', _MakeBoxCmd())
FreeCADGui.addCommand('Basic2_MakeBoxDialog', _MakeBoxDialogCmd())
