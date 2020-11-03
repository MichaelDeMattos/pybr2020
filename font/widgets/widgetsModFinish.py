#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WidgetsFinish(object):
    
    def startWidgets(self, builder, *args):
        """
            param: builder é o construtor do Gtk Builder
        """
        
        # Carregando o arquivo gerado pelo Glade
        builder.add_from_file("interface/windowFinish.ui")
        
        # Aqui é realizado o acesso aos widgets que serão manipulados
        self.windowFinish = builder.get_object("windowFinish")
        self.windowFinish.set_modal(True)
        self.windowFinish.set_title("Obrigado Python Brasil 2020")
        self.imgFinish = builder.get_object("imgFinish")
        
