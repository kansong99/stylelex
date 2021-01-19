import spacy
import json
from links import *
#from find3 import *
#from names3 import names_func
from numb import numb_func

text = "It is the '60s.."
llist = LinkedList(text)
##names takes three booleans plus llist
##numb takes 6 booleans plus llist
numb_func(llist, False,False,False,False, False, True)
##find takes one boolean plus list. Oxford comma true, no oxford false
#find_func(llist)


solution = llist.toarray()
#check = json.dumps(solution)
print(solution)



