# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect('/home/pi/prueba.db')
cursor = con.cursor()
cursor.execute
cursor.execute("INSERT INTO comments (post_id, name, email, website_url, comment) \
    VALUES (2,'Pedro Astigaraga', 'pedro@gmail.com', 'marca.com', 'Eres todo un cracl')")
con.commit()
con.close()
