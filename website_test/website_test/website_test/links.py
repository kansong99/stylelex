import spacy

nlp = spacy.load("en_core_web_sm")
#text = ("He wants to buy red apples, green grapes, and yellow bananas. I like Jill, Jane, and Mary. I have 32 dollars")
#doc = nlp(text)

#A dictionary of all the errors contained throughout all the files
perrors = {1: " (<- remove oxford comma)", 2: " (<- insert oxford comma)", 3: " (Use last name as shortened reference ->)", 
		   5: " (<- Use full name on first reference ->)", 7: " (Potentially misspelled name ->)"  }

class Node:
	def __init__(self, start, end, error):
		self.next = None
		self.error = error #to tell for printing whether text is error or correct. If not correct error is 0,\if it is set to code in perror
		self.start = start #initial string index
		self.end = end #last string index


class LinkedList:
	def __init__(self, text): #meta info to know how long the initial string is for later functions
		self.head = Node(-25, -1, 0)
		self.head.next = Node(0, len(text), 0)
		self.text = text
		self.doc = nlp(text)



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
				print(self.text[current.start: current.end], end = "")
			else:
				print(perrors[current.error], end = "")
			current = current.next

	def tostring(self): #function to change LinkedList to list
		output = ""
		current = self.head.next
		while current:
			if current.error == 0:
				output = output + self.text[current.start: current.end]
			else:
				output = output + perrors[current.error]
			current = current.next
		
		return output




#llist = LinkedList(article)



