

"""
Right now, its an offset 6 by 8 grid.

       2         4         6
  1         3         5
       8(B)      10        12
  7         9         11
       14        16(X)     18(X)
  13        15        17 
       20        22        24
  19        21        23
       26        28        30
  25        27        29
       32        34        36
  31        33        35
       38        40        42
  37        39        41
       44        46        48
  43        45        47

"""
order = [
       1,        3,        5,
  0,        2,        4,
       7,        9,        11,
  6,        8,        10,
       13,       -1,       -1,
  12,       14,       16, 
       19,       21,       23,
  18,       20,       22,
       25,       27,       29,
  24,       26,       28,
       31,       33,       35,
  30,       32,       34,
       37,       39,       41,
  36,       38,       40,
       43,       45,       47,
  42,       44,       46,
]






def maplights(array):
	"""
	Given a list of n tuples in the form of (R,G,B), return a list of the same size,
	corresponding to how they're arranged on the ceiling.
	"""
	out = [(0,0,0)]*len(order)
	for i in range(len(order)):
	  try:
	    out[i] = array[order[i]]
	  except IndexError:
	    pass
	
	return out
	
