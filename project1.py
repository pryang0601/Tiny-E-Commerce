    # -*- coding: utf-8 -*-

    ###########################################################################
    ## Python code generated with wxFormBuilder (version 3.10.1-239-ge2e4764f)
    ## http://www.wxformbuilder.org/
    ##
    ## PLEASE DO *NOT* EDIT THIS FILE!
    ###########################################################################

import re
import wx
import wx.xrc
import sqlite3 as lite
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
    ###########################################################################
    ## Class MyFrame2
    ###########################################################################

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ,client_email,client_password,Updates,Charts):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.client_email=client_email
        self.client_password=client_password
        self.Updates=Updates
        self.Charts=Charts
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 8, 3, 10, 20 )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Are you a new client?", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        NewClientChoices = [ u"YES", u"NO" ]
        self.NewClient = wx.RadioBox( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, NewClientChoices, 1, wx.RA_SPECIFY_ROWS )
        self.NewClient.SetSelection( 0 )
        gSizer1.Add( self.NewClient, 0, wx.ALL, 5 )

        self.LogCommit = wx.Button( self.m_panel1, wx.ID_ANY, u"Commit", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.LogCommit, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        
        self.m_staticText10.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )
        self.m_staticText10.Hide()
        gSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.m_staticText7.Hide()

        gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.LogEmail = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
        self.LogEmail.Hide()
        gSizer1.Add( self.LogEmail, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        self.m_staticText12.Hide()

        gSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        self.m_staticText13.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.m_staticText13.Hide()
        gSizer1.Add( self.m_staticText13, 0, wx.ALL, 5 )

        
        self.LogPass = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
        self.LogPass.Hide()
        gSizer1.Add( self.LogPass, 0, wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Sign Up", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Hide()

        self.m_staticText14.Wrap( -1 )

        self.m_staticText14.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )

        self.m_staticText15 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        self.m_staticText15.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.m_staticText15.Hide()

        gSizer1.Add( self.m_staticText15, 0, wx.ALL, 5 )

        self.RegEmail = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
        self.RegEmail.Hide()
        gSizer1.Add( self.RegEmail, 0, wx.ALL, 5 )

        self.remind = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.remind.Wrap( -1 )

        self.remind.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.remind.Hide()

        gSizer1.Add( self.remind, 0, wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        self.m_staticText18.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.m_staticText18.Hide()
        gSizer1.Add( self.m_staticText18, 0, wx.ALL, 5 )

        self.RegPass = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
        self.RegPass.Hide()
        gSizer1.Add( self.RegPass, 0, wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        self.m_staticText19.Hide()

        gSizer1.Add( self.m_staticText19, 0, wx.ALL, 5 )

        self.m_staticText20 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Birthday", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        self.m_staticText20.Hide()
        self.m_staticText20.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )

        gSizer1.Add( self.m_staticText20, 0, wx.ALL, 5 )
        
        self.RegBirth = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
        self.RegBirth.Hide()
        gSizer1.Add( self.RegBirth, 0, wx.ALL, 5 )

        self.m_staticText22 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        self.m_staticText22.Hide()

        gSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )

        self.m_staticText23 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        
        self.m_staticText23.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.m_staticText23.Hide()

        gSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )

        ReggenderChoices = [ u"Male", u"Female" ]
        self.Reggender = wx.RadioBox( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, ReggenderChoices, 1, wx.RA_SPECIFY_ROWS )
        self.Reggender.SetSelection( 0 )
        self.Reggender.Hide()
        gSizer1.Add( self.Reggender, 0, wx.ALL, 5 )

        self.m_staticText25 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        self.m_staticText25.Hide()

        gSizer1.Add( self.m_staticText25, 0, wx.ALL, 5 )

        self.Log_button = wx.Button( self.m_panel1, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Log_button.Hide()
        gSizer1.Add( self.Log_button, 0, wx.ALL, 5 )

        self.m_staticText24 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        self.m_staticText24.Hide()

        gSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )


        self.m_panel1.SetSizer( gSizer1 )
        self.m_panel1.Layout()
        gSizer1.Fit( self.m_panel1 )
        self.m_notebook2.AddPage( self.m_panel1, u"Log In / Register", False )
        self.m_panel2 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        

        gSizer2 = wx.GridSizer( 5, 3, 0, 0 )
        self.m_staticText17 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        self.m_staticText17.Hide()

        gSizer2.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.m_staticText191 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Product", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText191.Wrap( -1 )

        self.m_staticText191.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer2.Add( self.m_staticText191, 0, wx.ALL, 5 )

        self.m_staticText201 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText201.Wrap( -1 )

        self.m_staticText201.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer2.Add( self.m_staticText201, 0, wx.ALL, 5 )

        self.m_staticText181 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Kitchen Utensil", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText181.Wrap( -1 )

        self.m_staticText181.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer2.Add( self.m_staticText181, 0, wx.ALL, 5 )

        kitchenChoices = [ u"Plate", u"Knife", u"Spoon", u"Fork", u"Timer", u"Bowl", u"Turner", u"Cooker" ]
        self.kitchen = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, kitchenChoices, 0 )
        gSizer2.Add( self.kitchen, 0, wx.ALL, 5 )

        self.kitchen_num = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer2.Add( self.kitchen_num, 0, wx.ALL, 5 )


        self.m_staticText29 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Bathroom Utensil", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        self.m_staticText29.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer2.Add( self.m_staticText29, 0, wx.ALL, 5 )

        bathroomChoices = [ u"Tissue", u"Toothbrush", u"Toothpaste", u"Shampoo", u"Soap", u"Trash can", u"Plunger", u"Mop" ]
        self.bathroom = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, bathroomChoices, 0 )
        gSizer2.Add( self.bathroom, 0, wx.ALL, 5 )

        self.bathroom_num = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer2.Add( self.bathroom_num, 0, wx.ALL, 5 )

        self.m_staticText30 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Room Utensil", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        self.m_staticText30.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )

        roomChoices = [ u"Fan", u"Curtain", u"Mirror", u"Table", u"Remote", u"Lamp", u"Cusion", u"Vase" ]
        self.room = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, roomChoices, 0 )
        gSizer2.Add( self.room, 0, wx.ALL, 5 )

        self.room_num = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer2.Add( self.room_num, 0, wx.ALL, 5 )

        self.Daily_CButton = wx.Button( self.m_panel2, wx.ID_ANY, u"Check Storehouse", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.Daily_CButton, 0, wx.ALL, 5 )

        self.DailyEnough = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.DailyEnough.Wrap( -1 )

        self.DailyEnough.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.DailyEnough.Hide()

        gSizer2.Add( self.DailyEnough, 0, wx.ALL, 5 )

        self.Daily_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Add to Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.Daily_button, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( gSizer2 )
        self.m_panel2.Layout()
        gSizer2.Fit( self.m_panel2 )
        self.m_notebook2.AddPage( self.m_panel2, u"Daily Necessities", True )
        self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer3 = wx.GridSizer( 4, 3, 0, 0 )

        self.m_staticText33 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )

        self.m_staticText33.Hide()

        gSizer3.Add( self.m_staticText33, 0, wx.ALL, 5 )

        self.m_staticText1911 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Product", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1911.Wrap( -1 )

        self.m_staticText1911.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer3.Add( self.m_staticText1911, 0, wx.ALL, 5 )

        self.m_staticText2011 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2011.Wrap( -1 )

        self.m_staticText2011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer3.Add( self.m_staticText2011, 0, wx.ALL, 5 )

        self.m_staticText292 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"For School", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText292.Wrap( -1 )

        self.m_staticText292.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer3.Add( self.m_staticText292, 0, wx.ALL, 5 )

        studentChoices = [ u"Scissor", u"Glue", u"Folder", u"Notebook", u"Highlighter", u"Pencil", u"Pen", u"Calculator" ]
        self.student = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, studentChoices, 0 )
        gSizer3.Add( self.student, 0, wx.ALL, 5 )

        self.student_num = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer3.Add( self.student_num, 0, wx.ALL, 5 )

        self.m_staticText291 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"For Office", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText291.Wrap( -1 )

        self.m_staticText291.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer3.Add( self.m_staticText291, 0, wx.ALL, 5 )

        officeChoices = [ u"Envelope", u"Fax", u"Keyboard", u"Clipboard", u"Sticky note", u"Mouse", u"Paper clip", u"Stapner" ]
        self.office = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, officeChoices, 0 )
        gSizer3.Add( self.office, 0, wx.ALL, 5 )

        self.office_num = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer3.Add( self.office_num, 0, wx.ALL, 5 )


        self.Stationery_check = wx.Button( self.m_panel3, wx.ID_ANY, u"Check Storehouse", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.Stationery_check, 0, wx.ALL, 5 )

        self.Stationery_enough = wx.StaticText( self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Stationery_enough.Wrap( -1 )

        self.Stationery_enough.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.Stationery_enough.Hide()

        gSizer3.Add( self.Stationery_enough, 0, wx.ALL, 5 )

        self.Stationery_button = wx.Button( self.m_panel3, wx.ID_ANY, u"Add to Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.Stationery_button, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( gSizer3 )
        self.m_panel3.Layout()
        gSizer3.Fit( self.m_panel3 )
        self.m_notebook2.AddPage( self.m_panel3, u"Stationery", False )
        self.m_panel4 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer31 = wx.GridSizer( 4, 3, 0, 0 )

        self.m_staticText331 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText331.Wrap( -1 )

        self.m_staticText331.Hide()

        gSizer31.Add( self.m_staticText331, 0, wx.ALL, 5 )

        self.m_staticText19111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Product", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19111.Wrap( -1 )

        self.m_staticText19111.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer31.Add( self.m_staticText19111, 0, wx.ALL, 5 )

        self.m_staticText20111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20111.Wrap( -1 )

        self.m_staticText20111.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer31.Add( self.m_staticText20111, 0, wx.ALL, 5 )

        self.m_staticText2921 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Cookies", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2921.Wrap( -1 )

        self.m_staticText2921.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer31.Add( self.m_staticText2921, 0, wx.ALL, 5 )

        cookiesChoices = [ u"Cheetos", u"Doritos", u"Oreo", u"Lay's", u"Kid-O", u"Lotus Biscoff", u"Chocochip Cookies", u"Digestive cookies" ]
        self.cookies = wx.ComboBox( self.m_panel4, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, cookiesChoices, 0 )
        gSizer31.Add( self.cookies, 0, wx.ALL, 5 )

        self.cookies_num = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer31.Add( self.cookies_num, 0, wx.ALL, 5 )

        self.m_staticText2911 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Chocolate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2911.Wrap( -1 )

        self.m_staticText2911.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer31.Add( self.m_staticText2911, 0, wx.ALL, 5 )

        chocolateChoices = [ u"Hershey's", u"Snickers", u"Bueno", u"Kit-Kat", u"Toblerone", u"FERRERO ROCHER", u"GHIRADELL", u"M&M" ]
        self.chocolate = wx.ComboBox( self.m_panel4, wx.ID_ANY, u"Pick Me!", wx.DefaultPosition, wx.DefaultSize, chocolateChoices, 0 )
        gSizer31.Add( self.chocolate, 0, wx.ALL, 5 )

        self.chocolate_num = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
        gSizer31.Add( self.chocolate_num, 0, wx.ALL, 5 )

        self.Snack_check = wx.Button( self.m_panel4, wx.ID_ANY, u"Check Storehouse", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer31.Add( self.Snack_check, 0, wx.ALL, 5 )

        self.Snack_enough = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Snack_enough.Wrap( -1 )

        self.Snack_enough.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Maku" ) )
        self.Snack_enough.Hide()

        gSizer31.Add( self.Snack_enough, 0, wx.ALL, 5 )

        self.snack_button = wx.Button( self.m_panel4, wx.ID_ANY, u"Add to Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer31.Add( self.snack_button, 0, wx.ALL, 5 )

        
        self.m_panel4.SetSizer( gSizer31 )
        self.m_panel4.Layout()
        gSizer31.Fit( self.m_panel4 )
        self.m_notebook2.AddPage( self.m_panel4, u"Snack", False )
        
        self.m_panel6 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer7 = wx.GridSizer( 3, 4, 0, 0 )

        self.show_button = wx.Button( self.m_panel6, wx.ID_ANY, u"Show My Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer7.Add( self.show_button, 0, wx.ALL, 5 )

        self.chart = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,100 ), wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL )
        gSizer7.Add( self.chart, 0, wx.ALL, 5 )

        self.m_staticText72 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText72.Wrap( -1 )

        self.m_staticText72.Hide()

        gSizer7.Add( self.m_staticText72, 0, wx.ALL, 5 )

        self.pay_button = wx.Button( self.m_panel6, wx.ID_ANY, u"Pay Now", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer7.Add( self.pay_button, 0, wx.ALL, 5 )

        self.success = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.success.Wrap( -1 )

        self.success.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )
        self.success.Hide()

        gSizer7.Add( self.success, 0, wx.ALL, 5 )

        self.refill = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Add Cash", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.refill.Wrap( -1 )

        self.refill.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )
        self.refill.Hide()

        gSizer7.Add( self.refill, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

        self.amount = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
        self.amount.Hide()

        gSizer7.Add( self.amount, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

        self.refill_button = wx.Button( self.m_panel6, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.refill_button.Hide()
        gSizer7.Add( self.refill_button, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


        self.m_staticText68 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Leave Comments...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText68.Wrap( -1 )

        self.m_staticText68.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Maku" ) )

        gSizer7.Add( self.m_staticText68, 0, wx.ALL, 5 )

        self.comment = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,100 ), 0 )
        gSizer7.Add( self.comment, 0, wx.ALL, 5 )

        self.m_staticText69 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText69.Wrap( -1 )

        self.m_staticText69.Hide()

        gSizer7.Add( self.m_staticText69, 0, wx.ALL, 5 )

        self.bye = wx.Button( self.m_panel6, wx.ID_ANY, u"Bye Bye", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer7.Add( self.bye, 0, wx.ALL, 5 )


        self.m_panel6.SetSizer( gSizer7 )
        self.m_panel6.Layout()
        gSizer7.Fit( self.m_panel6 )
        self.m_notebook2.AddPage( self.m_panel6, u"Check", False )

        bSizer2.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.LogCommit.Bind( wx.EVT_BUTTON, self.LogShow )
        self.Log_button.Bind( wx.EVT_BUTTON, self.Login )
        self.Daily_CButton.Bind( wx.EVT_BUTTON, self.DailyCheck )
        self.Daily_button.Bind( wx.EVT_BUTTON, self.DailyAdd )
        self.Stationery_check.Bind( wx.EVT_BUTTON, self.StationeryCheck )
        self.Stationery_button.Bind( wx.EVT_BUTTON, self.StationAdd )
        self.Snack_check.Bind( wx.EVT_BUTTON, self.SnackCheck )
        self.snack_button.Bind( wx.EVT_BUTTON, self.SnackAdd )
        self.show_button.Bind( wx.EVT_BUTTON, self.ShowChart )
        self.pay_button.Bind( wx.EVT_BUTTON, self.pay )
        self.refill_button.Bind( wx.EVT_BUTTON, self.GoRefill )
        self.bye.Bind( wx.EVT_BUTTON, self.End )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def LogShow( self, event ):
        if self.NewClient.GetSelection()==0:
            self.m_staticText10.Hide()
            self.m_staticText7.Hide()
            self.m_staticText13.Hide()
            self.LogEmail.Hide()
            self.LogPass.Hide()
            self.m_staticText14.Show()
            self.m_staticText15.Show()
            self.RegEmail.Show()
            self.m_staticText18.Show()
            self.RegPass.Show()
            self.m_staticText20.Show()
            self.RegBirth.Show()
            self.m_staticText23.Show()
            self.Reggender.Show()
        else:
            self.m_staticText10.Show()
            self.m_staticText7.Show()
            self.m_staticText13.Show()
            self.LogEmail.Show()
            self.LogPass.Show()
            self.m_staticText14.Hide()
            self.m_staticText15.Hide()
            self.RegEmail.Hide()
            self.m_staticText18.Hide()
            self.RegPass.Hide()
            self.m_staticText20.Hide()
            self.RegBirth.Hide()
            self.m_staticText23.Hide()
            self.Reggender.Hide()
        self.Log_button.Show()
    def Login( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        FirstTime=self.NewClient.GetSelection()
        if FirstTime==0:
            email=self.RegEmail.GetValue()
            e=re.search("@gmail.com",email)
            if e==None:
                self.remind.Show()
                self.remind.SetLabel("Your email should \ncontained with @gmail.com")
            else:
                password=self.RegPass.GetValue()
                birthday=self.RegBirth.GetValue()
                gender=self.Reggender.GetSelection()
                gender=self.Reggender.GetString(gender)
                self.client_email=email
                self.client_password=password
                self.remind.SetLabel("Sign Up Successfully!")
                self.remind.Show()
                cur.execute(f"Insert into Clients (Email,Password,Birthday,Gender) Values ('{email}','{password}','{birthday}','{gender}')")
                con.commit()
        else:
            self.client_email=self.LogEmail.GetValue()
            self.client_password=self.LogPass.GetValue()
            cur.execute(f"SELECT Password FROM Clients WHERE Email ='{self.client_email}'")
            passw=cur.fetchone()[0]
            if passw!=self.client_password:
                self.remind.SetLabel("Login Unsuccessfully\nCheck you password again...")
            else:
                self.remind.SetLabel("Login Successfully!")
            self.remind.Show()


    def DailyCheck( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        k_index=self.kitchen.GetSelection()
        if k_index!=-1:
            k_uten=self.kitchen.GetString(k_index)
            k_num=int(self.kitchen_num.GetValue())
        b_index=self.bathroom.GetSelection()
        if b_index!=-1:
            b_uten=self.bathroom.GetString(b_index)
            b_num=int(self.bathroom_num.GetValue())
        r_index=self.room.GetSelection()
        if r_index!=-1:
            r_uten=self.room.GetString(r_index)
            r_num=int(self.room_num.GetValue())
        warning=""
        update={}
        if k_index!=-1:
            cur.execute("Select * from Kitchen")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==k_uten:
                    if int(k_num)>row[1]:
                        warning+=(k_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[k_uten]=[k_num,row[2]]
        if b_index!=-1:
            cur.execute("Select * from Bathroom")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==b_uten:
                    if b_num>row[1]:
                        warning+=(b_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[b_uten]=[b_num,row[2]]
        if r_index!=-1:
            cur.execute("Select * from Room")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==r_uten:
                    if r_num>row[1]:
                        warning+=(r_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[r_uten]=[r_num,row[2]]
        if warning=="":
            self.DailyEnough.SetLabel("All products are available!")
            self.DailyEnough.Show()
            self.Updates=update
        else:
            self.DailyEnough.SetLabel(warning)
            self.DailyEnough.Show()
        
    def DailyAdd( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        self.kitchen_num.ChangeValue("")
        self.bathroom_num.ChangeValue("")
        self.room_num.ChangeValue("")
        self.kitchen.SetSelection(-1)
        self.bathroom.SetSelection(-1)
        self.room.SetSelection(-1)
        self.kitchen.SetValue("Pick Me!")
        self.bathroom.SetValue("Pick Me!")
        self.room.SetValue("Pick Me!")
        self.Charts.append(self.Updates)
        keys=list(self.Updates.keys())
        values=list(self.Updates.values())
        current=0
        cur.execute("Select * from Kitchen")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=str(int(row[1])-int(values[current][0]))
                    cur.execute(f"update Kitchen set Num={n} where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        cur.execute("Select * from Bathroom")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=str(int(row[1])-int(values[current][0]))
                    cur.execute(f"update Bathroom set Num={n} where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        cur.execute("Select * from Room")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=str(int(row[1])-int(values[current][0]))
                    cur.execute(f"update Room set Num={n} where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        self.DailyEnough.SetLabel("Add to chart done!")
        self.DailyEnough.Show()
        
    def StationeryCheck( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        s_index=self.student.GetSelection()
        if s_index!=-1:
            s_uten=self.student.GetString(s_index)
            s_num=int(self.student_num.GetValue())
        o_index=self.office.GetSelection()
        if o_index!=-1:
            o_uten=self.office.GetString(o_index)
            o_num=int(self.office_num.GetValue())
        warning=""
        update={}
        if s_index!=-1:
            cur.execute("Select * from School")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==s_uten:
                    if s_num>row[1]:
                        warning+=(s_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[s_uten]=[s_num,row[2]]
        if o_index!=-1:
            cur.execute("Select * from Office")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==o_uten:
                    if o_num>row[1]:
                        warning+=(o_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[o_uten]=[o_num,row[2]]
        if warning=="":
            self.Stationery_enough.SetLabel("All products are available!")
            self.Stationery_enough.Show()
            self.Updates=update
        else:
            self.Stationery_enough.SetLabel(warning)
            self.Stationery_enough.Show()

    def StationAdd( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        self.student_num.ChangeValue("")
        self.office_num.ChangeValue("")
        self.student.SetSelection(-1)
        self.office.SetSelection(-1)
        self.student.SetValue("Pick Me!")
        self.office.SetValue("Pick Me!")
        self.Charts.append(self.Updates)
        keys=list(self.Updates.keys())
        values=list(self.Updates.values())
        current=0
        cur.execute("Select * from School")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=int(row[1])-int(values[current][0])
                    cur.execute(f"update School set Num={n} where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        cur.execute("Select * from Office")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=int(row[1])-int(values[current][0])
                    cur.execute(f"update Office set Num={n} where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        self.Stationery_enough.SetLabel("Add to chart done!")
        self.Stationery_enough.Show()
    def SnackCheck( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        cook_index=self.cookies.GetSelection()
        if cook_index!=-1:
            cook_uten=self.cookies.GetString(cook_index)
            cook_num=int(self.cookies_num.GetValue())
        cho_index=self.chocolate.GetSelection()
        if cho_index!=-1:
            cho_uten=self.chocolate.GetString(cho_index)
            cho_num=int(self.chocolate_num.GetValue())
        warning=""
        update={}
        
        if cook_index!=-1:
            cur.execute("Select * from Cookies")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==cook_uten:
                    if cook_num>row[1]:
                        warning+=(cook_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[cook_uten]=[cook_num,row[2]]
        if cho_index!=-1:
            cur.execute("Select * from Chocolate")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==cho_uten:
                    if cho_num>row[1]:
                        warning+=(cho_uten+" only "+ str(row[1])+" left\n")
                    else:
                        update[cho_uten]=[cho_num,row[2]]
        if warning=="":
            self.Snack_enough.SetLabel("All products are available!")
            self.Snack_enough.Show()
            self.Updates=update
        else:
            self.Snack_enough.SetLabel(warning)
            self.Snack_enough.Show()

    def SnackAdd( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        self.cookies_num.ChangeValue("")
        self.chocolate_num.ChangeValue("")
        self.cookies.SetSelection(-1)
        self.chocolate.SetSelection(-1)
        self.cookies.SetValue("Pick Me!")
        self.chocolate.SetValue("Pick Me!")
        self.Charts.append(self.Updates)
        keys=list(self.Updates.keys())
        values=list(self.Updates.values())
        current=0
        cur.execute("Select * from Cookies")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=int(row[1])-int(values[current][0])
                    cur.execute(f"Update Cookies set Num={n} Where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        cur.execute("Select * from Chocolate")
        rows=cur.fetchall()
        for row in rows:
            if current<len(keys):
                if row[0]==keys[current]:
                    n=int(row[1])-int(values[current][0])
                    cur.execute(f"Update Chocolate set Num={n} Where Product='{keys[current]}'")
                    con.commit()
                    current+=1
        self.Snack_enough.SetLabel("Add to chart done!")
        self.Snack_enough.Show()
    def ShowChart( self, event ):
        total=0
        with open("chart.txt","w") as f:
            for i in range(len(self.Charts)):
                dic=self.Charts[i]
                keys=list(dic.keys())
                values=list(dic.values())
                for j in range(len(keys)):
                    f.write(keys[j]+" "+str(values[j][0])+" : "+str(values[j][0]*values[j][1])+" dollars\n")
                    total+=values[j][0]*values[j][1]
            f.write("Total : "+str(total)+" dollars\n")
        self.chart.LoadFile("chart.txt")
        
    def pay( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        cur.execute(f"SELECT Balance FROM Clients WHERE Email ='{self.client_email}' and Password='{self.client_password}'")
        balance=cur.fetchone()[0]
        with open("chart.txt","r") as f:
            files=f.readlines()
        payment=0
        for i in range(len(files)-1):
            payment+=int(files[i].split()[-2])
        if payment>balance:
            self.success.SetLabel("Sorry, you only have "+str(balance)+" dollars in your account"+'\n'+"Please add some money to your account!")
            self.success.Show()
            self.refill.Show()
            self.amount.Show()
            self.refill_button.Show()
        else:
            cur.execute(f"update Clients set Balance='{balance-payment}' where Email ='{self.client_email}' and Password='{self.client_password}'")
            con.commit()
            self.success.SetLabel("Done! Thank you! Have a nice day! :)")
            self.success.Show()
    def GoRefill( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        self.success.SetLabel("Adding money successfully!")
        refill_amount=int(self.amount.GetValue())
        cur.execute(f"SELECT Balance FROM Clients WHERE Email ='{self.client_email}' and Password='{self.client_password}'")
        current_balance=cur.fetchone()[0]
        current_balance+=refill_amount
        cur.execute(f"update Clients set Balance='{current_balance}' where Email ='{self.client_email}' and Password='{self.client_password}'")
        con.commit()
        self.refill_button.Hide()
        self.amount.ChangeValue("")
        self.amount.Hide()
        self.refill.Hide()
    def End( self, event ):
        con=lite.connect("project1.db")
        cur=con.cursor()
        com=self.comment.GetValue()
        total=0
        recepit=""
        for i in range(len(self.Charts)):
            dic=self.Charts[i]
            keys=list(dic.keys())
            values=list(dic.values())
            for j in range(len(keys)):
                recepit+=(keys[j]+" "+str(values[j][0])+" : "+str(values[j][0]*values[j][1])+" dollars\n")
                total+=values[j][0]*values[j][1]
        recepit+=("Total : "+str(total)+" dollars")
        if com!="":
            with open("comment.txt","w") as f:
                f.write(com)
            cur.execute(f"Insert into Comment Values('{self.client_email}','{com}')")
            con.commit()
            msg="Thank you for leaving the comments! Hope you enjoy our products!\nHere is the recepit :\n"
            msg+=recepit
                          #郵件內容
        else:
            msg="Hope you enjoy our products!\nHere is the recepit :\n"
            msg+=recepit
        content = MIMEMultipart()                       #建立MIMEMultipart物件
        
        if com!="":
            content["subject"] = "Comments Received!"             #郵件標題
        else:
            content["subject"]="Thanks for buying our products!"
        content["from"] = "clairepryang@gmail.com"      #寄件者
        content["to"] = self.client_email                           #收件者
        content.attach(MIMEText(msg))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("clairepryang@gmail.com", "mladlremwbxnlljz")
            server.send_message(content)
        except:
            print('Something went wrong...')
        # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # 設定SMTP伺服器
        #     try:
        #         print(msg)
        #         #smtp.ehlo()                             # 驗證SMTP伺服器
        #         smtp.starttls()                         # 建立加密傳輸
        #         #zvvxajaglzpavqua
                
        #         smtp.login("clairepryang@gmail.com", "mladlremwbxnlljz")  # 登入寄件者gmail
        #         smtp.send_message(content)              # 寄送郵件
        #         print("Complete!")
        #     except Exception as e:
        #         print("Error message: ", e)
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame2(None,"","",{},[])
    frm.Show()
    app.MainLoop()



