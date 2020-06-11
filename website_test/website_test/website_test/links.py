import spacy

nlp = spacy.load("en_core_web_md")

#A dictionary of all the errors contained throughout all the files
perrors = {1: " (oxford comma present or not here) ->",
2: "(spell out numbers less than or equal to 100)->",
4: "(Measurements should be symbols)->",
6: "(Measurements should be written out)->",
8: "(You should use symbol %)->",
10: "(percent should be written out)->",
12: "Spell out numbers when they start sentence->",
14: "Consider rephrasing sentence so it does not start with date->",
16: "write age as numeral->",
18: "spell out decades, e.g nineteen-sixties not '60s ->",
20: "spell out words less than or equal to 100->",
22: "You should use $ when money is numeral->",
24: "Write out round numbers and use dollars instead of $->",
26: "Write out round numbers e.g, twenty-seven thousand dollars->",
28: "spell out numbers less than 100 and use dollars instead of $->",
30: "Write out whole number and use dollars instead of $->",
32: "Write out whole number->",
34: "Use numerals to represent this number->",
36: "Use numerals to represent this number and use $->",
38: "use dollars in this instance->",
40: "don't spell out number greater than 100->",
42: "don't spell out number greater than 100 and use $ instead of dollars->",
44: "dollars should be used instead of $ for numbers less than or equal to 100->"
}


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

def binary(bool1, key1, key2, bool2, start, end):
	if bool1 is False and bool2 == 0:
		llist.insert(start, key1)
	elif bool1 is True and bool2 == 1:
		llist.insert(start, key2)



