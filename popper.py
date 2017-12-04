from sets import Set

# Function that removes an input of indices from an array
# ex. popper([0,1,2,3,4], [1,0,2]) will remove elements of index 1,0,2 from [0,1,2,3,4]

def popper(arr, indicesToRemove):
	s = Set()

	for index in indicesToRemove:
		for num in s:
			if index > num:
				index -= 1
		arr.pop(index)
		s.add(index)

	return arr

popper([0,1,2,3,4], [4,2,3])
