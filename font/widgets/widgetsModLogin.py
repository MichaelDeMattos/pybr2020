#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WidgetsLogin(object):
    
    def startWidgets(self, builder, *args):
        """
            param: builder é o construtor do Gtk Builder
        """
        
        # Carregando o arquivo gerado pelo Glade
        builder.add_from_file("interface/login.ui")
        
        # Aqui é realizado o acesso aos widgets que serão manipulados
        self.windowLogin = builder.get_object("windowLogin")
        self.entryUser = builder.get_object("entryUser")
        self.entryPasswd = builder.get_object("entryPasswd")
        self.msgDialog = builder.get_object("msgDialog")
        
