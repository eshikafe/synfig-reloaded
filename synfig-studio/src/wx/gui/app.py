# -*- coding: utf-8 -*-

# ====================== S Y N F I G =============================================
#   File: app.py
#   Description:
#
#   This package is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation; either version 2 of
#   the License, or (at your option) any later version.
#
#   This package is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   General Public License for more details.
#
# =========================================================================

import os
import sys
import math
import wx
import wx.aui
from dialogs.about import About


if sys.platform == 'win32':
    WIN32 = 1
    WINVER = 0x0500
    SINGLE_THREADED = 1


from general import *


MISC_DIR_PREFERENCE     = "misc_dir"
ANIMATION_DIR_PREFERENCE    = "animation_dir"
IMAGE_DIR_PREFERENCE        = "image_dir"
SKETCH_DIR_PREFERENCE       = "sketch_dir"
RENDER_DIR_PREFERENCE       = "render_dir"

def DPM2DPI(x):
    return (float(x)/39.3700787402)
def DPI2DPM(x):
    return (float(x)*39.3700787402)

if sys.platform == 'win32':
    IMAGE_DIR = "share\\pixmaps"
else:
    IMAGE_DIR = "/usr/local/share/pixmaps"

IMAGE_EXT = "tif"

if sys.platform == 'win32':
    PLUGIN_DIR = "share\\synfig\\plugins"
else:
    PLUGIN_DIR = "/usr/local/share/synfig/plugins"

ID_New = wx.NewId()
ID_Open = wx.NewId()
ID_MenuOpenRecent = wx.NewId()
ID_Save = wx.NewId()
ID_SaveAs = wx.NewId()
ID_SaveAll = wx.NewId()
ID_Revert = wx.NewId()
ID_Import = wx.NewId()
ID_Preview = wx.NewId()
ID_Render = wx.NewId()
ID_CloseDocument = wx.NewId()
ID_Quit = wx.NewId()

ID_Undo = wx.NewId()
ID_Redo = wx.NewId()
ID_Cut = wx.NewId()
ID_Copy = wx.NewId()
ID_Paste = wx.NewId()
ID_SelectAllLayers = wx.NewId()
ID_UnselectAllLayers = wx.NewId()
ID_SelectAllHandles = wx.NewId()
ID_UnselectAllHandles = wx.NewId()
ID_InputDevices = wx.NewId()
ID_Preferences = wx.NewId()

ID_Help = wx.NewId()
ID_HelpTutorials = wx.NewId()
ID_HelpReference = wx.NewId()
ID_HelpFAQ = wx.NewId()
ID_HelpSupport = wx.NewId()
ID_HelpAbout = wx.NewId()

class App(wx.Frame):
    def __init__(self, basepath, argc, argv):
        wx.Frame.__init__(self,None, -1, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |wx.SUNKEN_BORDER |wx.CLIP_CHILDREN)
        self.page_count = 0
        self.sTitle = "Synfig Studio (Experimental)"
        self.app_base_path_=os.path.dirname(basepath)
        self.SetTitle(_(self.sTitle))
        self.SetIcon(wx.Icon("synfig_icon.ico"))
        self.init_ui_manager()
        self.Maximize()
        self.SetMinSize(wx.Size(800, 300))
        self.Show()

    def init_ui_manager(self):
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        self._perspectives = []

        synfig_menubar = wx.MenuBar()

        # File menu
        menu_file = wx.Menu()
        menu_file.Append(ID_New,_("New\tCtrl+N"))
        menu_file.Append(ID_Open, _("Open\tCtrl+O"))
        menu_open_recent = wx.Menu()
        menu_file.AppendMenu(ID_MenuOpenRecent,_("Open Recent"), menu_open_recent)
        menu_file.AppendSeparator()
        menu_file.Append(ID_Save, _("Save\tCtrl+S"))
        menu_file.Append(ID_SaveAs, _("Save As...\tShift+Ctrl+S"))
        menu_file.Append(ID_SaveAll, _("Save All"))
        menu_file.Append(ID_Revert, _("Revert"))
        menu_file.AppendSeparator()
        menu_file.Append(ID_Import, _("Import\tCtrl+I"))
        menu_file.AppendSeparator()
        menu_file.Append(ID_Preview, _("Preview\tF11"))
        menu_file.Append(ID_Render, _("Render\tF9"))
        menu_file.AppendSeparator()
        menu_file.Append(ID_CloseDocument, _("Close Document\tCtrl+W"))
        menu_file.Append(ID_Quit, _("Quit\tCtrl+Q"))

        # Edit menu
        menu_edit = wx.Menu()
        menu_edit.Append(ID_Undo,_("Undo\tCtrl+Z"))
        menu_edit.Append(ID_Redo,_("Redo\tCtrl+R"))
        menu_edit.AppendSeparator()
        menu_edit.Append(ID_Cut,_("Cut\tCtrl+X"))
        menu_edit.Append(ID_Copy,_("Copy\tCtrl+C"))
        menu_edit.Append(ID_Paste,_("Paste\tCtrl+V"))
        menu_edit.AppendSeparator()
        menu_edit.Append(ID_SelectAllLayers,_("Select All Layers\tShift+Ctrl+A"))
        menu_edit.Append(ID_UnselectAllLayers,_("Unselect All Layers\tShift+Ctrl+D"))
        menu_edit.Append(ID_SelectAllHandles,_("Select All Handles\tCtrl+A"))
        menu_edit.Append(ID_UnselectAllHandles,_("Unselect All Handles\tCtrl+D"))
        menu_edit.AppendSeparator()
        menu_edit.Append(ID_InputDevices,_("Input Devices..."))
        menu_edit.Append(ID_Preferences,_("Preferences..."))

        # View menu
        menu_view = wx.Menu()

        # Canvas menu
        menu_canvas = wx.Menu()

        # Toolbox menu
        menu_toolbox = wx.Menu()

        # Layer menu
        menu_layer = wx.Menu()

        # Plug-Ins menu
        menu_plugins = wx.Menu()

        # Window menu
        menu_window = wx.Menu()

        # Help menu
        menu_help = wx.Menu()
        menu_help.Append(ID_Help, _("Help\tF1"))
        menu_help.AppendSeparator()
        menu_help.Append(ID_HelpTutorials, _("Tutorials"))
        menu_help.Append(ID_HelpReference, _("Reference"))
        menu_help.Append(ID_HelpFAQ, _("Frequently Asked Questions"))
        menu_help.AppendSeparator()
        menu_help.Append(ID_HelpSupport, _("Get Support"))
        menu_help.AppendSeparator()
        menu_help.Append(ID_HelpAbout, _("About Synfig Studio"))

        synfig_menubar.Append(menu_file, _("&File"))
        synfig_menubar.Append(menu_edit, _("&Edit"))
        synfig_menubar.Append(menu_view, _("&View"))
        synfig_menubar.Append(menu_canvas, _("&Canvas"))
        synfig_menubar.Append(menu_toolbox, _("Toolbox"))
        synfig_menubar.Append(menu_layer, _("&Layer"))
        synfig_menubar.Append(menu_plugins, _("Plug-Ins"))
        synfig_menubar.Append(menu_window, _("&Window"))
        synfig_menubar.Append(menu_help, _("&Help"))

        self.Bind(wx.EVT_MENU, self.OnNew, id=ID_New)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_HelpAbout)

        self.SetMenuBar(synfig_menubar)

        self.panel = self.CreatePanel()
        self._mgr.AddPane(self.panel, wx.aui.AuiPaneInfo().Name("work-area").CenterPane())

        # Notebook
        self.nb = wx.aui.AuiNotebook(self.panel)
        self.NewAnimationPage()

        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageSelected)

        sz = wx.BoxSizer()
        sz.Add(self.nb,2,wx.EXPAND)
        self.panel.SetSizer(sz)
        perspective_all = self._mgr.SavePerspective()
        all_panes = self._mgr.GetAllPanes()

        self._mgr.GetPane("work-area").Show()


    def CreatePanel(self):
        pnl = wx.Panel(self, -1)
        return pnl

    def OnPageSelected(self, event):
        text = self.nb.GetPageText(self.nb.GetSelection())
        self.SetTitle(_(text + " - " + self.sTitle))

    def NewAnimationPage(self):
        self.page_count = self.page_count + 1
        title = "Synfig Animation " + str(self.page_count)
        self.nb.AddPage(self.CreatePanel(),title)
        self.SetTitle(_(title + " - " + self.sTitle))

    def OnNew(self, event):
        self.NewAnimationPage()

    def OnAbout(self, event):
        about = About(self)
        about.show()