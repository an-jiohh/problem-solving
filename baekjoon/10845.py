import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

q = deque()

for i in range(n) :
    sel = sys.stdin.readline().rstrip().split()
    if sel[0] == "push" :
        q.append(int(sel[1]))
    elif sel[0] == "pop" :
        if len(q) == 0 :
            sys.stdout.write("%d\n" % -1)
        else :
            sys.stdout.write("%d\n" % q.popleft())
    elif sel[0] == "size" :
        sys.stdout.write("%d\n" % len(q))
    elif sel[0] == "empty" :
        sys.stdout.write("%d\n" % (1 if len(q) == 0 else 0))
    elif sel[0] == "front" :
        if len(q) == 0 :
            sys.stdout.write("%d\n" % -1)
        else :
            sys.stdout.write("%d\n" % q[0])
    elif sel[0] == "back" :
        if len(q) == 0 :
            sys.stdout.write("%d\n" % -1)
        else :
            sys.stdout.write("%d\n" % q[len(q) - 1])