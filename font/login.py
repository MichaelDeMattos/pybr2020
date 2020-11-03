#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import sqlite3
import traceback, sys
from widgets.widgetsModLogin import WidgetsLogin
from model.modelLogin import ModelsLogin
from engineers.MikeUtil import MikeGtk

from finish import Finish as WindowFinish

import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

builder = Gtk.Builder()

class Login(WidgetsLogin, ModelsLogin, MikeGtk):
    """
        Aqui estão os modulos que a classe Login irá extender
    """
    
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        
        """
            Aqui é necessário carregar/acessar os widgets da interface
            que serão manipulados pelo sistema.
        """
        
        self.startWidgets(builder)
        
        """
            Aqui estou dando um Show na minha janela de Login
        """
        self.windowLogin.show_all()
        
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
        self.conexao = sqlite3.connect("../model/pybr.db")
        self.cursor = self.conexao.cursor()
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # >> Sinal ao fechar a janela de login
    # >> GtkWindow || destroy
    def on_window_login_destroy(self, *args):
        try:
            Gtk.main_quit()
        except Exception as ex:
            self.simple_msg_box(self.msgDialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # >> Sinal ao clicar em acessar
    # >> GtkButton || clicked
    def on_btLogin_clicked(self, *args):
        try:
            # >> usuário e senha digitados
            user = self.entryUser.get_text().upper()
            passwd = self.entryPasswd.get_text()
            
            # >> Transforma a senha digitada em base64
            passwdBase64 = base64.b64encode(passwd.encode('utf-8'))
            
            # >> Realiza a busca do usuário e senha
            searchLogin = self.checkLogin(user, passwdBase64, self.cursor)
            
            # >> Checa o login
            if searchLogin == []:
                 self.simple_msg_box(self.msgDialog, "Erro",
                                     "Usuário ou senha inválida")
            
            # >> Caso o login ocorra a nova janela é chamada
            else: 
                WindowFinish(builder, self.conexao, self.cursor)
                
        except Exception as ex:
            erro = traceback.print_exc(file=sys.stdout)
            print(str(erro))
            self.simple_msg_box(self.msgDialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
if __name__ == '__main__':
    builder.connect_signals(Login())
    Gtk.main()
