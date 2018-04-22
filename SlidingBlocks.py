from search import *

_Level_=2
class Sliding_Blocks(Problem):

    def __init__(self, level, initial=None):
		#level of the problem inquiring 2 or 3
		_Level_=level
		#randomising initial state
		#representing as
		#'b' the blank tiles
		#'y' the yellow single-block tiles
		#'v' the vertical double-block tiles 
		#'h' the horizontal double-block tiles
		#'r' the red poly-block tiles
		if initial==None:
			if _Level_==2 :
				initial=[['v','b','y','b'],['v','y','r','r'],['h','h','y','y']]
				#initial=[['v','y','y','y'],['v','b','r','r'],['h','h','y','b']] #->deadlock
				#initial=[['v','y','y','y'],['v','y','r','r'],['h','h','b','b']]
				#initial=[['y','v','b','y'],['b','v','r','r'],['y','y','h','h']] #->possible deadlock
			else :
				#because of geometry it is more unlikely to get to a deadlock state in this level
				#despite the possibility of a user going round and round in cycles
				initial=[['y','v','r','r'],['y','v','r','r'],['b','y','h','h'],['y','b','y','y']]
		base = tuple(tuple(x) for x in initial)
		super(Sliding_Blocks, self).__init__(base, None)

    def actions(self, state):
		"""Return the actions that can be executed in the given
		state. The result would typically be a list, but if there are
		many actions, consider yielding them one at a time in an
		iterator, rather than building them all at once."""
		#moving blank blocks around is really fun and messed up
		#if self.level==2: 
		#	x,y=3,4
		#elif self.level==3:
		#	x,y=4,4
		Actions=[]
		count=0
		l=list(list(x) for x in state)
		for i in range(_Level_+1):
			for j in range(4):
				if count==2:
					break
				if l[i][j]=='b':
					count=count+1
					
					if i>0 : 								#vertical up
						a=[1,'u',i,j,-1,-1]
						Actions.append(a)
						if j<3 and (l[i][j+1]=='b'):
							a=[2,'u',i,j,i,j+1]
							Actions.append(a)
					
					if i<_Level_: 						#vertical down	
						a=[1,'d',i,j,-1,-1]
						Actions.append(a)
						if j<3 and (l[i][j+1]=='b'):
							a=[2,'d',i,j,i,j+1]
							Actions.append(a)
					
					if j<3:									#horizontal right
						a=[1,'r',i,j,-1,-1]
						Actions.append(a)
						if i<_Level_ and (l[i+1][j]=='b'):
							a=[2,'r',i,j,i+1,j]
							Actions.append(a)
						
					if j>0:									#horizontal left
						a=[1,'l',i,j,-1,-1]
						Actions.append(a)
						if i<_Level_ and (l[i+1][j]=='b'):
							a=[2,'l',i,j,i+1,j]
							Actions.append(a)
							
			if count==2:
				break
		if Actions:
			return tuple(tuple(x) for x in Actions)
		else :
			print 'No available actions -> deadlock ! Im trying backing up'
			return ()
		
    def result(self, state, action):
		"""Return the state that results from executing the given
		action in the given state. The action must be one of
		self.actions(state)."""
		st=list(list(x) for x in state)
		l=list(action)
		if l[0]==1: #one blank tile to be moved
			if l[1]=='u':
				if st[l[2]-1][l[3]]=='y':
					st[l[2]-1][l[3]]='b' #altering the one that needs to change
					st[l[2]][l[3]]='y'
					return tuple(tuple(x) for x in st)
				if st[l[2]-1][l[3]]=='v':
					st[l[2]-2][l[3]]='b' #altering the one that needs to change
					st[l[2]][l[3]]='v'
					return tuple(tuple(x) for x in st)

			if l[1]=='d':
				if st[l[2]+1][l[3]]=='y':
					st[l[2]+1][l[3]]='b' #altering the one that needs to change
					st[l[2]][l[3]]='y'
					return tuple(tuple(x) for x in st)
				if st[l[2]+1][l[3]]=='v':
					st[l[2]+2][l[3]]='b' #altering the one that needs to change
					st[l[2]][l[3]]='v'
					return tuple(tuple(x) for x in st)
					
			if l[1]=='r':
				if st[l[2]][l[3]+1]=='y':
					st[l[2]][l[3]+1]='b' #altering the one that needs to change
					st[l[2]][l[3]]='y'
					return tuple(tuple(x) for x in st)
				if st[l[2]][l[3]+1]=='h':
					st[l[2]][l[3]+2]='b' #altering the one that needs to change
					st[l[2]][l[3]]='h'
					return tuple(tuple(x) for x in st)
				if st[l[2]][l[3]+1]=='r':
					st[l[2]][l[3]+2]='b' #altering the one that needs to change
					st[l[2]][l[3]]='r'
					return tuple(tuple(x) for x in st)
					
			if l[1]=='l':
				if st[l[2]][l[3]-1]=='y':
					st[l[2]][l[3]-1]='b' #altering the one that needs to change
					st[l[2]][l[3]]='y'
					return tuple(tuple(x) for x in st)
				if st[l[2]][l[3]-1]=='h':
					st[l[2]][l[3]-2]='b' #altering the one that needs to change
					st[l[2]][l[3]]='h'
					return tuple(tuple(x) for x in st)
				if st[l[2]][l[3]-1]=='r' and _Level_ != 3:# if lvl==3 cant move the red block
					st[l[2]][l[3]-2]='b' #altering the one that needs to change
					st[l[2]][l[3]]='r'
					return tuple(tuple(x) for x in st)
					
		else : #two blank tiles to be moved 
			if l[1]=='u':
				if st[l[2]-1][l[3]]=='h' and st[l[2]-1][l[3]+1]=='h':
					st[l[2]-1][l[3]],st[l[2]-1][l[3]+1] = 'b','b' #altering the one that needs to change
					st[l[2]][l[3]],st[l[2]][l[3]+1] = 'h','h'
					return tuple(tuple(x) for x in st)
				if st[l[2]-1][l[3]]=='r' and st[l[2]-1][l[3]+1]=='r':
					if _Level_==2:
						st[l[2]-1][l[3]],st[l[2]-1][l[3]+1] = 'b','b' #altering the one that needs to change
						st[l[2]][l[3]],st[l[2]][l[3]+1] = 'r','r'
						return tuple(tuple(x) for x in st)
					else :
						st[l[2]-2][l[3]],st[l[2]-2][l[3]+1] = 'b','b' #altering the one that needs to change
						st[l[2]][l[3]],st[l[2]][l[3]+1] = 'r','r'
						return tuple(tuple(x) for x in st)
		
			if l[1]=='d':
				if st[l[2]+1][l[3]]=='h' and st[l[2]+1][l[3]+1]=='h':
					st[l[2]+1][l[3]],st[l[2]+1][l[3]+1] = 'b','b' #altering the ones that needs to change
					st[l[2]][l[3]],st[l[2]][l[3]+1] = 'h','h'
					return tuple(tuple(x) for x in st)
				if st[l[2]+1][l[3]]=='r' and st[l[2]+1][l[3]+1]=='r':
					if _Level_==2:
						st[l[2]+1][l[3]],st[l[2]+1][l[3]+1] = 'b','b' #altering the ones that needs to change
						st[l[2]][l[3]],st[l[2]][l[3]+1] = 'r','r'
						return tuple(tuple(x) for x in st)
					else :
						st[l[2]+2][l[3]],st[l[2]+2][l[3]+1] = 'b','b' #altering the ones that needs to change
						st[l[2]][l[3]],st[l[2]][l[3]+1] = 'r','r'
						return tuple(tuple(x) for x in st)
			
			if l[1]=='r':
				if st[l[2]][l[3]+1]=='v' and st[l[2]+1][l[3]+1]=='v':
					st[l[2]][l[3]+1],st[l[2]+1][l[3]+1]='b','b' #altering the ones that needs to change
					st[l[2]][l[3]],st[l[2]+1][l[3]]='v','v'
					return tuple(tuple(x) for x in st)
				if st[l[2]][l[3]+1]=='r' and st[l[2]+1][l[3]+1]=='r': #lvl 3 is sure
					st[l[2]][l[3]+2],st[l[2]+1][l[3]+2]='b','b' #altering the ones that needs to change
					st[l[2]][l[3]],st[l[2]+1][l[3]]='r','r'
					return tuple(tuple(x) for x in st)
								
			if l[1]=='l':
				if st[l[2]][l[3]-1]=='v' and st[l[2]+1][l[3]-1]=='v':
					st[l[2]][l[3]-1],st[l[2]+1][l[3]-1]='b','b' #altering the ones that needs to change
					st[l[2]][l[3]],st[l[2]+1][l[3]]='v','v'
					return tuple(tuple(x) for x in st)
				if st[l[2]][l[3]-1]=='r' and st[l[2]+1][l[3]-1]=='r': #lvl 3 is sure
					st[l[2]][l[3]-2],st[l[2]+1][l[3]-2]='b','b' #altering the ones that needs to change
					st[l[2]][l[3]],st[l[2]+1][l[3]]='r','r'
					return tuple(tuple(x) for x in st)
								

    def goal_test(self, state):
		"""Return True if the state is a goal. The default method compares the
		state to self.goal, as specified in the constructor. Override this
		method if checking against a single self.goal is not enough."""
		#lvl 2 and 3 considered with concrete red block of 4 or 2 tiles oriented horizontically
		l=list(list(x) for x in state)
		flag=True
		for i in range(_Level_ - 1):
			for j in range (2):
				if l[i][j]!='r':
					flag=False
					break
			if flag==False:
				break
		return flag

    def path_cost(self, c, state1, action, state2):
		"""Return the cost of a solution path that arrives at state2 from
		state1 via action, assuming cost c to get up to state1. If the problem
		is such that the path doesn't matter, this function will only look at
		state2.  If the path does matter, it will consider c and maybe state1
		and action. The default method costs 1 for every step in the path."""
		l=list(action)
		return (c+l[0])
#______________________________________________________________________________
# HEURESTIC FUNCTIONS
def	h1(n):
	print n.state
	#if n.state:
	s=list(list(x) for x in n.state)
	for i in range(_Level_+1):
		flag=False
		for j in range(4):
			if flag==False and s[i][j]=='r':
				flag=True
				pi=i
				pj=j
	return _Level_-pi+pj
	#return 100000
		
#number of moves for red block - Manhattan * 2
def h2(n):
	state=list(list(x) for x in n.state)
	for i in range(_Level_+1):
		flag=False
		for j in range(4):
			if flag==False and state[i][j]=='r':
				flag=True
				pi=i
				pj=j
	if _Level_==3:
		if state[pi][pj-1]=='b' and state[pi-1][pj-1]=='b': #can move left
			return 2*(_Level_-pi+pj)-1
	if state[pi+1][pj]=='b' and state[pi+1][pj+1]=='b':
		return 2*(_Level_-pi+pj)-1
	return 2*(_Level_-pi+pj)
#
#______________________________________________________________________________