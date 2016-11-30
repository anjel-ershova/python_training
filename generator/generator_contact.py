from model.model_contact import *
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    # n - кол-во генерируемых данных
    # f - файл, куда данные помещаются
    # в [] - подсказка по функциям
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)
n = 1
f = "data/contacts.json"

for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


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
for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))