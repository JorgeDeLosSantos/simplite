# -*- coding: utf-8 -*-
#
# Simplite 0.1.0-dev
# License: MIT License
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com 
# Code: https://github.com/JorgeDeLosSantos/simplite
#
#~ from __future__ import absolute_import

import wx

class Simplite(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,title="Simplite",size=(800,400))
        # Display on center
        
        self.initMenu()
        
        self.Centre(True)
        self.Show()
    
    def initMenu(self):
        m_file = wx.Menu()
        open_db = m_file.Append(-1, "Open SQLite DB... \tCtrl+I")
        quit_app = m_file.Append(-1, "Quit \tCtrl+Q")
        
        m_help = wx.Menu()
        _help = m_help.Append(-1, "Help")
        about = m_help.Append(-1, "About...")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(m_file, "File")
        menu_bar.Append(m_help, "Help")
        self.SetMenuBar(menu_bar)
        
        #~ self.Bind(wx.EVT_MENU, self.OnSave, save)
        

class App(wx.App):
    """
    Override OnInit
    """
    def OnInit(self):
        frame = Simplite(None)
        return True

def run():
    """
    Entry point for Simplite
    """
    REDIRECT = False
    LOG_FILE = "simplite.log"
    app = App(REDIRECT)
    app.MainLoop()


if __name__=='__main__':
    run() # Run app
