#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class MikeGtk(object):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#--> Simples MessageBox/MessageDialog
    def simple_msg_box(self, component, title, text, icon=None, *args):
        component.props.text = (title)
        component.props.secondary_text = (text)
        component.props.icon_name = (icon)
        component.show_all()
        component.run()
        component.hide()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#--> Estilos e Persolalização
    def style_app(self, style_path, set_screen, *args):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(style_path)
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(set_screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#--> Retorna a data atual em formato pt-br
    def format_current_date(self, *args):
        date_today = datetime.date.today()
        date_today_format = ("{}/{}/{}").format("0" + str(date_today.day) if int(date_today.day) < 10 else str(date_today.day),
                                                "0" + str(date_today.month) if int(date_today.month) < 10 else str(date_today.month),
                                                date_today.year)
        return str(date_today_format)
