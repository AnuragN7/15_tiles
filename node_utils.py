
def get_coordinates(val):
	""" This function simply returns a tuple containing the coordinates of a certain value
	
	Args:
	val: a number ranging from 0 to 15
 	Example: the value 13 would correspond to (3,1)
	"""
	row_val = val // 4
	col_val = val % 4	
	return row_val, col_val


def copy_board(source_list, target_list):
		""" Copies a list into another list

		Args:
		target_list: The list we want to insert data into 
		"""

		for item in source_list:
			target_list.append(item)



def process_input(source_list_one, source_list_two):
	"""
	Process the command line arguments to return two lists, one will be the root node object. The other, by the goal_node
	
	Args:
	source_list_one: The board of the root node
	source_list_two: The board of the goal_node
	"""
	strip_list(source_list_one)
	strip_list(source_list_two)
	start_node_list = [int(x) for x in source_list_one]
	goal_list = [int(x) for x in source_list_two]
	return start_node_list, goal_list

def strip_list(target_list):
	"""Removes the '[' and ']' from the list we are trying to process
	
	Args:
	target_list: List we need to process
	"""
	target_list[0] = target_list[0][1] # Remove the '[' 
	target_list[-1] = target_list[-1][:-1] # Remove the ']'


def get_parent_node(node, closed_list):
	"""
	Returns the parent node of the node currently being examined
	
	Args:

	node: Node object whose parent we are trying to find
	"""
	parent_candidate = None
	for candidate_node in closed_list:
		if node.parent_ID == candidate_node.state_ID:
			return candidate_node

def write_node_to_file(node):
	"""Writes the properties of the node object to the file output.txt

	Args:
	node: the node object whose properties we are trying to print out
	"""
	with open('output.txt', 'a') as output_file:
		output_file.write('Node_ID: ' + str(node.state_ID) + '\n')
		output_file.write("Node board: " + str(node.board) + '\n'),
		output_file.write('g(n): ',)
		output_file.write(str(node.g_of_n) + '\n')
		output_file.write('h(n): ',)
		output_file.write(str(node.h_of_n) + '\n')
		output_file.write('f(n): ',)
		output_file.write(str(node.f_of_n) + '\n')

def in_open_list(node, open_list):
	"""
	Checks to see if a node is in the open_list (the frontier)
	
	Args:

	node: The Node object we want to check
	open_list: The open list

	returns: True or False depending or whether or not the node exists in the open list
	"""

	for i in range(open_list.qsize()):
		if open_list.queue[i][2].board == node.board:
			return open_list.queue[i][2]
	return None

def find_and_replace(pre_existing_node, child_node, open_list):
	"""
	Finds the location of the node in the open_list
	
	Args:
	pre_existing_node: The node already within the open_list
	child node: The node we want to replace the pre-existing node with
	open_list: The open list
	"""
	for i in range(open_list.qsize()):
		if open_list.queue[i][2].board == child_node.board:
			open_list.queue[i] = (child_node.f_of_n, child_node.state_ID, child_node)
			
						
def in_closed_list(node, closed_list):
	"""
	Checks to see if a node is within the closed list

	Args:
	
	node: The Node object we are trying to check
	closed_list: the closed list 
	
	returns: True or False depending on whether or not we have found a node
	"""
	for ref_node in closed_list:
		if node.board == ref_node.board:
			return True
	return False


def calculate_h_of_n(current_state, goal_node):
	"""
	Our heuristic function that calculates the h(n) value of a child node.

	Args:
	current_state: the state in the search tree we are at
	goal_node: The goal node

	returns: The h(n) of the particular state we are in
	"""	
	overall_count = 0
	for num in current_state:
		source_x, source_y = get_coordinates(current_state.index(num)) # Where is that element currently?
		target_x, target_y = get_coordinates(goal_node.index(num)) # Where that element is supposed to be
		difference = abs(target_x - source_x) + abs(target_y - source_y);
		if difference > 1:	
			overall_count += difference
	
	return overall_count 



