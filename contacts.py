class General:
    def __init__(self, firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname", title="title",
                 company="company", address="address"):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address

class Telephone:
    def __init__(self, home='555-5678', mobile='8-800-200-555-500', work='555-work', fax='812-123-23-34'):
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
    def __init__(self, address2='Another address', home='home_secondary', notes='Some text'):
        self.address2 = address2
        self.home = home
        self.notes = notes