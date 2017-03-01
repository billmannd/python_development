#to connect MySQL to python
#sudo wget http://cdn.mysql.com//Downloads/Connector-Python/mysql-connector-python-2.1.3.tar.gz
#gunzip mysql-connector-python-2.1.3.tar.gz
#tar xf mysql-connector-python-2.1.3.tar
#cd mysql-connector-python-2.1.3
# sudo python3 setup.py install
# proven to be successful!!!!

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='db_wine')
cnx.close()