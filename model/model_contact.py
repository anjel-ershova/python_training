class General:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address

class Telephone:
    def __init__(self, home=None, mobile=None, work=None, fax=None):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax

class Email:
    def __init__(self, email, email2, email3):
        self.email = email
        self.email2 = email2
        self.email3 = email3

class Secondary:
    def __init__(self, address2=None, home=None, notes=None):
        self.address2 = address2
        self.home = home
        self.notes = notes