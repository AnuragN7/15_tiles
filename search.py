import sys
import Node
import queue
from node_utils import *

open_list = queue.PriorityQueue()
closed_list = []


def create_path(node):
	"""
	Creates the path stack. The stack should reflect the path the search tree took from start to finish

	Args: 
	node: The goal node when the function is called first
	"""
	while not (node.parent_ID == 0):
		write_node_to_file(node)
		node = get_parent_node(node,closed_list)
	
	write_node_to_file(node) # We have reached the start node, so we need to print it

def a_star():
	""" 
	The A* search algorithm

	Args:
	node: the node object we begin our search from
	"""
	node = open_list.get()[2]
	node.expand()
	for child_node in node.children:
		if child_node.is_goal_node():
			print("Solution found! Please refer to \'output.txt\'")
			closed_list.append(node) 
			create_path(child_node)
		else:
			if not in_closed_list(child_node, closed_list):
				pre_existing_node = in_open_list(child_node, open_list) # Does the newly created child node already exist in the open_list
				if pre_existing_node: 
					if pre_existing_node.f_of_n > child_node.f_of_n:
						find_and_replace(pre_existing_node, child_node, open_list)
					else:
						continue	 
				else:
					open_list.put((child_node.f_of_n, child_node.state_ID, child_node)) # Add the node's children to open_list				
			else:
				continue
	closed_list.append(node) # Add the node itself to the closed list
	a_star()


if __name__=="__main__":	
	
	if len(sys.argv) == 33: # Must validate input 
		start_list = [sys.argv[x] for x  in range(1,17)]
		goal_list = [sys.argv[x] for x in range(17,33)]
		start_node_board, goal_node = process_input(start_list, goal_list) 
		start_node = Node.Node(start_node_board, goal_node)
		open_list.put((start_node.f_of_n, start_node.state_ID,start_node))		
	
		a_star()

	else:
		print("Cannot validate input.")
		
	




	
