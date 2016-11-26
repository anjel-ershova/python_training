from sys import maxsize

class General:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

class Telephone:
    def __init__(self, home=None, mobile=None, work=None, fax=None):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax

class Email:
    def __init__(self, email=None, email2=None, email3=None):
        self.email = email
        self.email2 = email2
        self.email3 = email3

class Secondary:
    def __init__(self, address2=None, home=None, notes=None):
        self.address2 = address2
        self.home = home
        self.notes = notes


