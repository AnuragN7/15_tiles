from node_utils import *
from random import randint

class Node(object):
	"""
	Represents a node in the search tree
	"""

	goal_node = [] # A 'static' variable will serve to hold the goal node
	COL_SIZE = 4 # Can be resized if user wants to play a variation of the game
	ID_list = [] # Ensures that every random number generated serves as a unique identifier to a node object. 

	heuristic_flag = 0 # We need this flag to determine which heuristic to use


	def __init__(self, board_list, goal_node):
		"""
		Node constructor

		Args:
		board_list: The board we need to store in the Node object


		Member Variables of a Node object:
	
		state_ID: ID of the current Node
		parent_ID: ID of the parent Node
		board: list representing the actual board
		children: a list of Node objects, that Node's children
		priority_value: That node's priority value

		"""
		Node.goal_node = goal_node
		self.state_ID = self.generate_unique_ID()
		self.parent_ID = 0 
		self.board = board_list
		self.children = []
		self.g_of_n = 0
		self.h_of_n = calculate_h_of_n(board_list, goal_node)
		self.f_of_n = self.g_of_n + self.h_of_n 

	def generate_unique_ID(self):
		"""
		This method generates a unique state ID for a node
		"""
		num = randint(0,1000)
		while num in Node.ID_list: # We need to ensure we generate a unique number everytime we call this method
			num = randint(0,1000)
		Node.ID_list.append(num)
		return num

	def is_goal_node(self):
		""" Returns True if we have found the goal node and False otherwise """
		return self.board == Node.goal_node

	def move_right(self, zero_index):
		""" Moves a zero to the right of the board 

		Args:
		zero_index: Index where zero lies in the list
		
		"""

		if zero_index % Node.COL_SIZE < Node.COL_SIZE - 1:
			new_lst = []
			copy_board(self.board,new_lst)
			new_lst[zero_index], new_lst[zero_index+1] = new_lst[zero_index+1], new_lst[zero_index]
			child = Node(new_lst, Node.goal_node) 
			child.parent_ID = self.state_ID
			child.g_of_n = self.g_of_n + 2 # Whatever is at zero_index will have swapped with zero
			child.f_of_n = child.g_of_n + child.h_of_n
			self.children.append(child)

	def move_left(self, zero_index):
		""" Moves a zero to the left of the board and adds that corresponding child node to the the current node list of children
		
		Args:
		zero_index: Index where zero lies in the list

		"""
		
		if zero_index % Node.COL_SIZE > 0:
			new_lst = []
			copy_board(self.board,new_lst)
			new_lst[zero_index], new_lst[zero_index-1] = new_lst[zero_index-1], new_lst[zero_index]
			child = Node(new_lst, Node.goal_node)
			child.parent_ID = self.state_ID
			child.g_of_n = self.g_of_n + 2 # Whatever is at zero_index will have swapped with zero
			child.f_of_n = child.g_of_n + child.h_of_n
			self.children.append(child)

	def move_up(self, zero_index):
		""" Moves a zero up the board and adds that corresponding child node to the the current node list of children 
	
		Args:
		zero_index: Index where zero lies in the list

		"""
		
		if zero_index >= Node.COL_SIZE:
			new_lst = []
			copy_board(self.board,new_lst)
			new_lst[zero_index], new_lst[zero_index-Node.COL_SIZE] = new_lst[zero_index-Node.COL_SIZE], new_lst[zero_index]
			child = Node(new_lst, Node.goal_node)
			child.parent_ID = self.state_ID
			child.g_of_n = self.g_of_n + 2 # Whatever is at zero_index will have swapped with zero
			child.f_of_n = child.g_of_n + child.h_of_n
			self.children.append(child)
	
	def move_down(self, zero_index):
		""" Moves a zero down the board and adds that corresponding child node to the the current node list of children

		Args: 
		zero_index: Index where zero lies in the list
		
		"""

		if zero_index < Node.COL_SIZE*(Node.COL_SIZE-1):
			new_lst = []
			copy_board(self.board,new_lst)
			new_lst[zero_index], new_lst[zero_index+Node.COL_SIZE] = new_lst[zero_index+Node.COL_SIZE], new_lst[zero_index]
			child = Node(new_lst, Node.goal_node)
			child.parent_ID = self.state_ID
			child.g_of_n = self.g_of_n + 2 # Whatever is at zero_index will have swapped with zero
			child.f_of_n = child.g_of_n + child.h_of_n
			self.children.append(child)

	def expand(self):
		"""
		Expands the current node to produce all possible states the board can reach from that node 
		"""
		zero_index = self.board.index(0)
		self.move_right(zero_index)
		self.move_left(zero_index)
		self.move_up(zero_index)
		self.move_down(zero_index)

	
	


	
