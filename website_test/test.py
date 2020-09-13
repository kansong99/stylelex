import spacy
from .links import *
from . import links
from .find3 import *
from .names3 import *
from .numb import *

text = ""

llist = LinkedList(text)
#names takes three booleans plus llist
names_func( llist)
#numb takes 6 booleans plus llist
numb_func(, llist)
#find takes one boolean plus list. Oxford comma true, no oxford false
find_func(llist)


solution = llist.tostring()

print(solution)



