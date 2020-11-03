#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ModelsLogin(object):
    def __init__(self, *args, **kwargs):
        super(ModelsLogin, self).__init__(*args, **kwargs)
    
    def checkLogin(self, user, password, cursor):
        """
            param: user => Usuário 
            param: password => Senha
            param: cursor => Cursor do banco de dados
        """
        
        sqlquery = (" select l.user,"
                    " l.password"
                    " from login l"
                    " where l.user = ?"
                    " and l.password = ?")
        
        sqlargs = ([user, password.decode('utf-8')])
        cursor.execute(sqlquery, sqlargs)
        
        return self.cursor.fetchall()
        
