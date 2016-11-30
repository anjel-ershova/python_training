from model.model_group import *
import random
import string

constant = [
    Group(name="name1", footer="footer1", header="header1"),
    Group(name="name2", footer="footer2", header="header2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", footer="", header="")] + [
    Group(name=random_string("name", 10), footer=random_string("footer", 20), header=random_string("header", 20))
    for i in range(1)
]
