class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def pre_order_traversal(node):
	if node is None:
		return []
	left_subtree_traversal = pre_order_traversal(node.left)
	right_subtree_traversal = pre_order_traversal(node.right)

	return [node.val] + left_subtree_traversal + right_subtree_traversal

def in_order_traversal(node):
	if node is None:
		return []
	left_subtree_traversal = in_order_traversal(node.left)
	right_subtree_traversal = in_order_traversal(node.right)

	return left_subtree_traversal + [node.val] + right_subtree_traversal

def post_order_traversal(node):
	if node is None:
		return []
	left_subtree_traversal = post_order_traversal(node.left)
	right_subtree_traversal = post_order_traversal(node.right)

	return left_subtree_traversal + right_subtree_traversal + [node.val]

def level_traversal(node):
	queue = [node]
	current_idx = 0
	result = list()

	while current_idx < len(queue):
		current_node = queue[current_idx]
		if current_node is not None:
			result.append(current_node.val)
			queue.append(current_node.left)
			queue.append(current_node.right)
		current_idx += 1

	return result


