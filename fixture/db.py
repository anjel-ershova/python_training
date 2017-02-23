import mysql.connector
from model.model_group import Group
from model.model_contact import Contact


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        self.connection.autocommit = True # должно снять кеширование бд, но не работает с pymysql.cursors


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

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, email, email2, email3, address2, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address,
                 home, mobile, work, email, email2, email3, address2, phone2) = row
                list.append(Contact(id=str(id), firstname2=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, title=title, company=company, address=address, home=home, mobile=mobile,
                                    work=work, email=email, email2=email2, email3=email3, address2=address2,
                                    phone2=phone2))
        finally:
            cursor.close()
        return list

