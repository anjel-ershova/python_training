from model.model_group import *
import random
import string
import os.path
import json
import getopt
import sys


try:
    # n - кол-во генерируемых данных
    # f - файл, куда данные помещаются
    # в [] - подсказка по функциям
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/data_groups.json"

for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", footer="", header="")] + [
    Group(name=random_string("name", 10), footer=random_string("footer", 20), header=random_string("header", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
