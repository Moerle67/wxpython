import eyed3
import glob
import wx

class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        # List Control
        self.list_ctrl = wx.ListCtrl(
            self, size = ( -1, 100),
            style = wx.LC_REPORT | wx.BORDER_STATIC
        )
        self.list_ctrl.InsertColumn(0, 'Artist', width = 140)
        self.list_ctrl.InsertColumn(1, 'Album', width = 140)
        self.list_ctrl.InsertColumn(2, 'Title', width = 200)
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # Button
        edit_button = wx.Button(self, label = 'Edit')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.Center, 5)
        self.SetSizer(main_sizer)

    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)

class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title='Mp3 tag Editor')
        self.panel = Mp3Panel(self)
        self.create_menu()
        self.Show()

    def create_menu(self):
        menu_bar

if __name__ == '__main__':
    app = wx.App(False)
    frame = Mp3Frame()
    app.MainLoop()