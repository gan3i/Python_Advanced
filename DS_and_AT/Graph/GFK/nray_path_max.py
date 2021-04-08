
'''
given a root of a nray tree find the maximum path sum from root to leafe node
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def max_path_sum_from_root(root : TreeNode):
    if not root:
        return 0

    child_path_max = float('-inf')

    for child in root.children:
        child_path_sum = max_path_sum_from_root(child)
        child_path_max = max(child_path_max, child_path_sum)

    return child_path_max + root.val

