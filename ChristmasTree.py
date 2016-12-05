# Ben Woodfield
# A Tree drawing using Python
# I found this on Stack Exchange - I wanted something Christmasy for my Python Community page
# Uses characters to draw a little tree!

import sys
w = sys.stdout.write
def t(n,s):
    for i in range(n):
        for a in range(n-i):
            w(" ")
        w("[")
        for l in range(i<<1):
            if i==n-1:
                w("_")
            else:
                w("~")
        w("]")
        print("")
    for o in range(s):
        for i in range(n):
            w(" ")
        print("[]")

t(10, 2)







