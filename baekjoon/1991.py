n = int(input())

tree = {}
inorder = []
preorder = []
postorder = []

for i in range(n) :
    node, left, right = input().split()
    tree[node] = [left, right]

def check(node, w):
    if w == 0 : inorder.append(node) 
    if tree[node][0] != "." :
        check(tree[node][0],w)
    if w == 1 : preorder.append(node)  
    if tree[node][1] != "." :
        check(tree[node][1],w)
    if w == 2 : postorder.append(node) 
check("A",0);
check("A",1);
check("A",2);

print(''.join(inorder))
print(''.join(preorder))
print(''.join(postorder))