from model.model_contact import Contact
import random
import string

constant = [
Contact(firstname2="firstname2", middlename="middlename", lastname="lastname", nickname="nickname", title="title",
                           company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                           address2="address2", phone2="phone2", notes="notes")
]


def random_string(prefix, maxlen):
    cont_symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10

    return prefix + "".join([random.choice(cont_symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname2="", middlename="", lastname="", nickname="", title="",
                           company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                           address2="", phone2="", notes="")] + [Contact
                            (firstname2=random_string("firstname", 10),
                             middlename=random_string("middlename", 20),
                             lastname=random_string("lastname", 20),
                             nickname=random_string("nickname", 20),
                             title=random_string("title", 20),
                             company=random_string("company", 20),
                             address=random_string("address", 30),
                             home=random_string("homephone", 20), mobile=random_string("mobilephone", 20), work=random_string("workphone", 20),
                             fax=random_string("fax", 20),
                             email=random_string("email1", 20), email2=random_string("email2", 20), email3=random_string("email3", 20),
                             address2=random_string("Another_address", 20),
                             phone2=random_string("home_secondary", 20),
                             notes=random_string("notes", 50))
for i in range(1)
]
