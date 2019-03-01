#!/usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = "Stalone Tray Clock"
__version__ = "0.1"
__author__  = "Alexandre C Vieira"
__license__ = "GNU GPL 2.0 or later"

import pygtk
pygtk.require('2.0')
import gtk, gobject, datetime, calendar, configparser, io, os

UPDATE_INTERVAL = 1  # in Seconds
SHOW_CALENDAR = False

def day_of_week(date):
    return calendar.day_abbr[date.weekday()]

def current_month(monthNumber):
    return calendar.month_abbr[monthNumber]  

def draw_window(label):
    widget = gtk.Layout()
    widget.put(label,0,ICON_SIZE / 4)
    widget.show()
    window = gtk.OffscreenWindow()
    window.set_default_size(ICON_SIZE, ICON_SIZE)
    window.set_opacity(0)
    window.add(widget)
    window.show_all()
    col = gtk.gdk.Color(BGCOLOR)
    widget.modify_bg(gtk.STATE_NORMAL, col)
    return window

def draw_padding_window():
    widget = gtk.Layout()
    widget.show()
    window = gtk.OffscreenWindow()
    window.set_default_size(ICON_SIZE, ICON_SIZE)
    window.set_opacity(0)
    window.add(widget)
    window.show_all()
    col = gtk.gdk.Color(BGCOLOR)
    window.present()
    widget.modify_bg(gtk.STATE_NORMAL, col)
    return window

def draw_calendar_window():
    global SHOW_CALENDAR
    SHOW_CALENDAR = True
    vbox = gtk.VBox(False, 5)
    cal = gtk.Calendar()
    cal.set_display_options(gtk.CALENDAR_SHOW_HEADING)
    halign1 = gtk.Alignment(0.5, 0.5, 0, 0)
    halign1.add(cal)
    valign = gtk.Alignment(0, 1, 0, 0)
    vbox.pack_start(halign1)
    window = gtk.Window()
    window.set_title("Calendário")
    window.set_size_request(200, 200)
    window.set_position(gtk.WIN_POS_CENTER)
    window.add(vbox)
    window.connect("destroy", set_show_calendar)
    window.show_all()

def set_show_calendar(gtkobject, data=None):
    global SHOW_CALENDAR
    SHOW_CALENDAR = False
    
def save_config():
    with open(os.path.expanduser('~/.stalone_tray_clockrc'), 'w') as f:
        f.write('%s\n%s\n%s\n%s\n%s\n%s' % ('icon_size' + ':'
                                                + str(ICON_SIZE), 'bgcolor' + ':' + BGCOLOR, 'fontcolor' + ':'
                                                + FONTCOLOR, 'fontsize' + ':' + FONTSIZE, 'font' + ':'
                                                + FONT, 'fontweight' + ':' + FONTWEIGHT))

def cb_allocate(label, allocation):
    label.set_size_request( ICON_SIZE, -1 )

def on_left_click(event):
    global SHOW_CALENDAR
    if not SHOW_CALENDAR:
        draw_calendar_window()
    
class ClockDayOfWeek:
    def __init__(self):
        self.icon = gtk.StatusIcon()
        self.icon.connect( "activate", on_left_click )
        self.dayofweek = day_of_week(datetime.date.today())
        self.label = gtk.Label()
        self.label.set_justify(gtk.JUSTIFY_CENTER)
        self.label.set_markup('<span color=\'' + FONTCOLOR + '\' font_weight=\'' + FONTWEIGHT
                              + '\' font=\'' + FONT + '\'>' + self.dayofweek + ', </span>')
        self.label.connect( "size-allocate", cb_allocate )
        self.window = draw_window(self.label)
        self.window.connect("damage-event", self.draw_complete_event)
        # self.window.present()

    def draw_complete_event(self, window, event):
        self.icon.set_from_pixbuf(window.get_pixbuf())

class ClockDay:
    def __init__(self):
        self.icon = gtk.StatusIcon()
        self.icon.connect( "activate", on_left_click )
        self.now = datetime.datetime.now()
        self.label = gtk.Label()
        self.label.set_justify(gtk.JUSTIFY_CENTER)
        self.label.set_markup('<span color=\'' + FONTCOLOR + '\' font_weight=\'' + FONTWEIGHT
                              + '\' font=\'' + FONT + '\'>' + str(self.now.day) + ' de</span>')
        self.label.connect( "size-allocate", cb_allocate )
        self.window = draw_window(self.label)
        self.window.connect("damage-event", self.draw_complete_event)
        # self.window.present()

    def draw_complete_event(self, window, event):
        self.icon.set_from_pixbuf(window.get_pixbuf())

class ClockMonth:
    def __init__(self):
        self.icon = gtk.StatusIcon()
        self.icon.connect( "activate", on_left_click )
        self.month = current_month(datetime.date.today().month)
        self.label = gtk.Label()
        self.label.set_justify(gtk.JUSTIFY_CENTER)
        self.label.set_markup('<span color=\'' + FONTCOLOR + '\' font_weight=\'' + FONTWEIGHT
                              + '\' font=\'' + FONT + '\'>' + self.month + '</span>')
        self.label.connect( "size-allocate", cb_allocate )
        self.window = draw_window(self.label)
        self.window.connect("damage-event", self.draw_complete_event)
        self.window.present()

    def draw_complete_event(self, window, event):
        self.icon.set_from_pixbuf(window.get_pixbuf())

class ClockTime:
    def __init__(self):
        self.icon = gtk.StatusIcon()
        self.icon.connect( "activate", on_left_click )
        self.label = gtk.Label()
        self.label.set_markup('<span color="white">time</span>')
        self.label.set_justify(gtk.JUSTIFY_CENTER)
        self.window = draw_window(self.label)
        self.window.connect("damage-event", self.draw_complete_event)
        self.update_clock()
        gobject.timeout_add(1000 * UPDATE_INTERVAL, self.update_clock)
        self.now = None
                   
    def update_clock(self):
        self.now = datetime.datetime.now()
        self.label.set_markup('<span color=\'' + FONTCOLOR + '\' font_weight=\'' + FONTWEIGHT
                              + '\' font=\'' + FONT + '\'>' + self.now.strftime("%H:%M") + '</span>')
        self.label.connect( "size-allocate", cb_allocate )
        self.window.present()
        return True

    def draw_complete_event(self, window, event):
        self.icon.set_from_pixbuf(window.get_pixbuf())

class ClockPadding:
    def __init__(self):
        self.icon = gtk.StatusIcon()
        window = draw_padding_window()
        window.connect("damage-event", self.draw_complete_event)

    def draw_complete_event(self, window, event):
        self.icon.set_from_pixbuf(window.get_pixbuf())
       
if __name__ == "__main__":
    try:
        user_config_dir = open(os.path.expanduser('~/.stalone_tray_clockrc'), 'r').read().split('\n')
        ICON_SIZE = int(user_config_dir[0].split(':')[1])
        BGCOLOR = user_config_dir[1].split(':')[1]
        FONTCOLOR = user_config_dir[2].split(':')[1]
        FONTSIZE = user_config_dir[3].split(':')[1]
        FONT = user_config_dir[4].split(':')[1]
        FONTWEIGHT = user_config_dir[5].split(':')[1] # One of 'ultralight', 'light', 'normal', 'bold',
                                                      # 'ultrabold', 'heavy', or a numeric weight
    except IOError:
        ICON_SIZE = 32
        BGCOLOR = '#111'
        FONTCOLOR = 'white'
        FONTSIZE = '9.5'
        FONT ='Ubuntu Regular'
        FONTWEIGHT = 'bold' # One of 'ultralight', 'light', 'normal', 'bold',
                            # 'ultrabold', 'heavy', or a numeric weight
        save_config()

    FONT = FONT + ' ' + FONTSIZE
    
    paddingleft = ClockPadding()
    appdayofweek = ClockDayOfWeek()
    appday = ClockDay()
    appmonth = ClockMonth()
    apptime = ClockTime()
    paddingright = ClockPadding()
    
    gtk.main()
