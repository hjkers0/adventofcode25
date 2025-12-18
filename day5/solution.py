file_text = ''
with open("input") as f:
    file_text = f.read()

class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None

def insert(root, interval):
    if root is None:
        return Node(Interval(interval.low, interval.high))
    
    if interval.low < root.interval.low:
        root.left = insert(root.left, interval)
    else:
        root.right = insert(root.right, interval)
    
    if root.max < interval.high:
        root.max = interval.high

    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print("[" + str(root.interval.low) + ", " + str(root.interval.high) + "]" + " max = " + str(root.max))
    inorder(root.right)

def search(root, id):
    if root is None:
        return 0
    if root.interval.low <= id and id <= root.interval.high:
        return 1
    
    if root.left is not None and root.left.max >= id:
        return search(root.left, id)
    
    return search(root.right, id)

ranges, ids = file_text.split('\n\n')
total = 0
ranges_fresh = ranges.split()
root = None

for rang in ranges_fresh:
    min_v, max_v = map(int, rang.split('-'))
    root = insert(root, Interval(min_v, max_v))

inorder(root)

ids_list = ids.split()
for id in ids_list:
    total += search(root, int(id))

print('total fresh food:', total)
