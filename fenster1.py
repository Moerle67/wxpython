import wx
import wx.xrc

from test1 import Moerli1

class Fenster1(Moerli1):
    def __init__(self, parent, dbase):
        super().__init__(parent)
        self.dbase = dbase

    def btn1click(self, event):
        name = self.txt_name.Value
        vorname = self.txt_vorname.Value
        self.dbase.save_name(name, vorname)
        self.txt_name = ""
        self.txt_vorname = ""
        return super().btn1click(event)