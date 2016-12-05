# Ben Woodfield
# run it as it is to make a 15 star wide pyramid
# if you just run pyramid() you get 8 stars wide
# change the number in the argument when you run it, so:
# pyramid(10) makes a 10 star wide pyramid

# This was a Youtube tutorial I made, the same code may be linked to another repo and the video
# I ended up putting it onto trinketio

def pyramid(rows=8):
    for i in range(rows):
        print ' '*(rows-i-1) + '*'*(2*i+1)
 
#pyramid()       
pyramid(15)
