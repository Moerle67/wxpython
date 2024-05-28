from fenster1 import *
from testdbase import *
import sqlite3 as sl

class MainApp(wx.App):
    def OnInit(self):
        self.dbase = Testdbase()
        self.fenster1 = Fenster1(None, self.dbase)
        self.fenster1.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()