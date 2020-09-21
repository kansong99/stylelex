import spacy
from links import *
#from find3 import *
#from names3 import *
from numb import *

text = "The site not only provides complimentary marketing services for people of color, but it also offers resources and information, like a link to a report from prosperitynow.org that found Black-owned businesses nationally average only $58,000 in annual revenue compared to $546,000 for white-owned businesses."

llist = LinkedList(text)
##names takes three booleans plus llist
#names_func( llist)
##numb takes 6 booleans plus llist
numb_func(True,True,True,True,True,True,llist)
##find takes one boolean plus list. Oxford comma true, no oxford false
#find_func(llist)


solution = llist.tostring()

print(solution)



