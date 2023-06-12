class Node:
	def __init__(self, data):
		self.data = data
		self.isEndOfString = False
		self.left = None
		self.eq = None
		self.right = None


def insert(root, word):
	if not root:
		root = Node(word[0])
	if word[0] < root.data:
		root.left = insert(root.left, word)
	elif word[0] > root.data:
		root.right = insert(root.right, word)
	else:
		if len(word) > 1:
			root.eq = insert(root.eq, word[1:])
		else:
			root.isEndOfString = True
	return root


def searchTST(root, word):
	if not root:
		return False
	if word[0] < root.data:
		return searchTST(root.left, word)
	elif word[0] > root.data:
		return searchTST(root.right, word)
	else:
		if len(word) > 1:
			return searchTST(root.eq, word[1:])
		else:
			return root.isEndOfString

def display(root, s, level):
	if not root:
		return

	display(root.left, s, level)
	s[level] = root.data

	if (root.isEndOfString):
		s[level+1] = ''
		print(''.join(s[:level+1]))

	display(root.eq, s, level+1)
	display(root.right, s, level)


# function to delete a string in TST

def isFreeNode(root):
	return not (root.left or root.eq or root.right)


def delete_node(root, s, level):
	if not root:
		return False

	# CASE 4 data present in TST, having atleast
	# one other data as prefix data.
	if level + 1 == len(s):
		# Unmark leaf node if present
		if root.isEndOfString:
			root.isEndOfString = False
			return isFreeNode(root)

		# else string is not present in TST and
		# return 0
		return False

	# CASE 3 data is prefix data of another long
	# data in TST.
	if s[level] < root.data:
		return delete_node(root.left, s, level)
	if s[level] > root.data:
		return delete_node(root.right, s, level)

	# CASE 1 data may not be there in TST.
	if s[level] == root.data and delete_node(root.eq, s, level + 1):
		# delete the last node, neither it has
		# any child nor it is part of any other
		# string
		root.eq = None
		return not root.isEndOfString and isFreeNode(root)

	return False

root = Node('')
insert(root, "cat")
insert(root, "dog")
insert(root, "apple")
insert(root, "banana")
insert(root, "orange")
insert(root, "grape")


'''
print("Found" if searchTST(root, "apple") else "Not Found")
print("Found" if searchTST(root, "jicama") else "Not Found")
print("Found" if searchTST(root, "iceapple") else "Not Found")'''

level = 0;s=['']*20
display(root, s, 0)

while(True):
	print("-------------------------------------------")
	print("Ternary Search Trie")
	print('''select an operation:1 , 2 , 3 , 4 , 5
1)insert
2)delete
3)search
4)display
5)exit''')

	n = int(input())
	if n == 1:
		print("-------------------------------------------")
		word=input("enter a word to insert")
		insert(root,word)
		print("inserted succefully")
		print("-------------------------------------------")
	elif n == 2:
		print("-------------------------------------------")
		word = input("enter a word to delete")
		delete_node(root, word, level)
		print("deletion succefully")
		print("-------------------------------------------")
	elif n == 3:
		print("-------------------------------------------")
		word = input("enter a word to search")
		print("Found" if searchTST(root, word) else "Not Found")
		print("-------------------------------------------")
	elif n == 4:
		print("-------------------------------------------")
		display(root, s, level)
		print("-------------------------------------------")
	else:
		exit()
