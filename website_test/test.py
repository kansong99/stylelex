import spacy
import json
from links import *
#from find3 import *
from names3 import names_func
#from numb import *

text = "Mr. Smith did it for me."
llist = LinkedList(text)
##names takes three booleans plus llist
names_func(llist, option1=True)
##numb takes 6 booleans plus llist
#numb_func(True,True,True,True,True,True,llist)
##find takes one boolean plus list. Oxford comma true, no oxford false
#find_func(llist)


solution = llist.toarray()
check = json.dumps(solution)
print(check)



