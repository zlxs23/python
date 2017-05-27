# _*_coding:utf-8_*_
"""Spare.py is a starting point for a wxpython program"""
import wx


class Frame(wx.Frame):

    """docstring for Frame"""
    pass


class App(wx.App):

    """docstring for App"""

    def OnInit(self):
        self.frame = Frame(parent=None, title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
