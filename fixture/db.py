import mysql
import pymysql.cursors
from model.model_group import Group

class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

"""
    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, address2, phone2, notes FROM addressbook")
            for row in cursor:
                (id, firstname, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes) = row
                list.append(Contact(id=id, firstname=firstname, lastname=lastname, nickname=nickname, company=company, title=title, address=address, home=home, mobile=mobile, work=work, fax=fax, email=email, email2=email2, email3=email3, address2=address2, phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list
"""



