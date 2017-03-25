from pony.orm import *
from datetime import datetime
from model.model_group import Group
from model.model_contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp



class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        deprecated = Optional(datetime, column='deprecated')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str, column='title')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, database, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=database, user=user, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=group.id, name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def get_group_list(self):
        with db_session: # лечит ошибку pony.orm.core.TransactionError: db_session is required when working with the database
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=contact.id, firstname2=contact.firstname, middlename=contact.middlename, lastname=contact.lastname,
                                    nickname=contact.nickname, title=contact.title, company=contact.company, address=contact.address, home=contact.home, mobile=contact.mobile,
                                    work=contact.work, email=contact.email, email2=contact.email2, email3=contact.email3, address2=contact.address2,
                                    phone2=contact.phone2)
        return list(map(convert, contacts))

    @db_session # второй вариант лечения ошибки db_session is required when working with the database
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

        return self.convert_contacts_to_model(orm_group.contacts)