""" 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
todo：添加id作为主键
"""
__author__ = "Lei gitwing"
__create__ = "2021-05-24"
__modified__ = "2021-05-25"
import mysql.connector


def connect_mysql(file_path):
    """Read a file and store the content in mysql

    There are 200 16 digits numbers in the file
    file_name: its content will be stored in mysql
    """
    cnx = mysql.connector.connect(user='root', host='localhost', password='password', database='sys', auth_plugin='mysql_native_password')
    cursor = cnx.cursor()
    # read the file
    file = open(file_path, 'r')
    for line in file:
        line = line.strip()
        # print(line)
        # store into mysql
        
        add_cupon = 'INSERT INTO `sys`.`new_table` (`cupon`) VALUES (%s)'
        data_cupon = [line]
        # insert new cupon data
        cursor.execute(add_cupon, data_cupon)
        # commit to the database
        cnx.commit()
    # close all the connections
    file.close()
    cursor.close()
    cnx.close()
        

if __name__ == '__main__':
    file_path = "coupon.txt"
    connect_mysql(file_path)
    print('ok')
