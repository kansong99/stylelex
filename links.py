import spacy

nlp = spacy.load("en_core_web_md")
text = ("He wants to buy red apples, green grapes, and yellow bananas. I like Jill, Jane, and Mary. I have 32 dollars")
doc = nlp(text)

#A dictionary of all the errors contained throughout all the files
perrors = {1: " (oxford comma present or not here) ->", 2: "(spell out numbers less than or equal to 100)->" }

class Node:
	def __init__(self, start, end, error):
		self.next = None
		self.error = error #to tell for printing whether text is error or correct. If not correct error is 0,\if it is set to code in perror
		self.start = start #initial string index
		self.end = end #last string index


class LinkedList:
	def __init__(self, total): #meta info to know how long the initial string is for later functions
		self.head = Node(-25, -1, 0)
		self.head.next = Node(0, total, 0)



	def insert(self, index, ecode): #add error suggestion to linked list. will NEVER be head
		prev = self.head
		current = self.head.next
		while index > current.end or current.error != 0: #while you are at wrong index or at error node
			current = current.next
			prev = prev.next
		enode = Node(0, 0, ecode)
		if current.start < index:
			prev.next = Node(current.start, index, 0)
			current.start = index
			prev.next.next = enode
			enode.next = current
		else:
			assert current.start == index
			prev.next = enode
			enode.next = current

	def lprint(self): #function to print out string
		current = self.head.next
		while current:
			if current.error == 0:
				print(text[current.start: current.end], end = "")
			else:
				print(perrors[current.error], end = "")
			current = current.next



llist = LinkedList(len(text))



