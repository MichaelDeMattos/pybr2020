#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from widgets.widgetsModFinish import WidgetsFinish
from engineers.MikeUtil import MikeGtk

import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Finish(WidgetsFinish, MikeGtk):
    """
        Aqui estão os modulos que a classe Login irá extender
    """
    
    def __init__(self, builder, conexao, cursor, *args, **kwargs):
        super(Finish, self).__init__(*args, **kwargs)
        """
            param: conexao => Herdado do modulo anterior
            param: cursor => Herdado do modulo anterior
            param: builder => Herdado do modulo anterior
        """
        
        """
            Aqui é necessário carregar/acessar os widgets da interface
            que serão manipulados pelo sistema.
        """
        
        self.startWidgets(builder)
        
        """
            Aqui estou dando um Show na minha janela de Login
        """
        self.windowFinish.show_all()
        
        """
            Aqui estou carregando o arquivo CSS
            para personalizar o estilo da aplicação
        """
        pathStyle = "../static/style.css"
        screen = Gdk.Screen()
        self.style_app(style_path=pathStyle, set_screen=screen)
        
        """
            Aqui estou realizando a conexao com o banco de dados
        """
        self.conexao = conexao
        self.cursor = cursor
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # >> Sinal ao fechar a janela final
    # >> GtkWindow || destroy
    def on_windowFinish_destroy(self, *args):
        try:
            window = self.windowFinish
            window.destroy
            
        except Exception as ex:
            self.simple_msg_box(self.msgDialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
