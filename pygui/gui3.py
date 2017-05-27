# -*-coding:utf-8-*-
# create a min empty wxpython program 空程序
import wx


class App(wx.App):

    """docstring for App 子化类 wxpy class"""

    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
