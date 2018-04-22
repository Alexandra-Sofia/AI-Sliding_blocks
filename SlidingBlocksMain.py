from sys import *
from SlidingBlocks import *

while(True):
	level=int(input('Choose level for the sliding blocks game 2 or 3') )
	if ( level==2 or level==3 ) :
		break

print 'initialising'
p=Sliding_Blocks(level)

while(True):
	h=int(input('Choose heuristic function 1 or 2'))
	if h==2 or h==1:
		break
	print
if h==1:
	s=astar_search(p,h1)
else :
	s=astar_search(p,h2)
if s:
	path=s.path()
	print path,path.cost
else:
	print 'No solution.... Sorry'
