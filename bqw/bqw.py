# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"槽口体积选择", pos = wx.DefaultPosition, size = wx.Size( 450,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer1.SetMinSize( wx.Size( 400,300 ) )
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer1.SetMinSize( wx.Size( 500,40 ) )
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"输入目标施肥量：", wx.DefaultPosition, wx.Size( 115,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 115,-1 ), 0 )
		self.m_textCtrl1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"（单位：克）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( fgSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.SHAPED|wx.TOP, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"确 定", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_button1.SetLabelMarkup( u"确 定" )
		self.m_button1.SetDefault()
		self.m_button1.SetBitmapMargins( wx.Size( 0,0 ) )
		self.m_button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )

		bSizer1.Add( self.m_button1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.SHAPED, 0 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( 500,200 ) )
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"可选择的槽口体积：", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		fgSizer2.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"不可选择的槽口体积：", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		fgSizer2.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.m_textCtrl2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.m_textCtrl3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.FertilizerCalculation )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def FertilizerCalculation( self, event ):
		event.Skip()


