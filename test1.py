# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Moerli1
###########################################################################

class Moerli1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Moerlis Testfenster", pos = wx.DefaultPosition, size = wx.Size( 281,361 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		chklst_namenChoices = []
		self.chklst_namen = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), chklst_namenChoices, 0 )
		bSizer1.Add( self.chklst_namen, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.lbl_name = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_name.Wrap( -1 )

		bSizer1.Add( self.lbl_name, 0, wx.ALL, 5 )

		self.txt_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer1.Add( self.txt_name, 0, wx.ALL, 5 )

		self.lbl = wx.StaticText( self, wx.ID_ANY, u"Vorname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl.Wrap( -1 )

		bSizer1.Add( self.lbl, 0, wx.ALL, 5 )

		self.txt_vorname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer1.Add( self.txt_vorname, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Speichern", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.btn1click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn1click( self, event ):
		event.Skip()


