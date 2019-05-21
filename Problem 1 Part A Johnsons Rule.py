# Johnsons rule.
'''
1. Find the minimum among the time taken by machine 1 and 2 for all the jobs.
2a. If the minimum processing time is required by machine 1 to complete the job, place the associated job in the first available position in the final sequence.
	go the step 3. If tie you may choose either of the one.
2b. If the minimum processing time is required by machine 2 to complete the job, place the associated job in the last available position in the final sequence.
	go the step 3. If tie you may choose either of the one.
3. Remove the assigned job from consideration and return to step 1 until all the positions in the sequence are filled.
'''
def johnsonsrule(m):

	# final sequence for each machine
	m_for_p1 = []
	m_for_p2 = []
	# current job sequence for each machines
	p1 = m[0]
	p2 = m[1]
	while p1:
		# Choosing the minimum among the machines.
		minp1 = min([ i[0] for i in p1])
		minp2 = min([ i[0] for i in p2])
		if minp1 < minp2:
			# get index of the minimum in p1
			for p in p1:
				if minp1 == p[0]:
					pos = p1.index(p)
					# Append the job in the final sequence
					m_for_p1.append(p[1])
					# Remove that job from the list
					p1.pop(pos)
					p2.pop(pos)
		elif minp1 > minp2:
			# get index of the minimum in p2
			for p in p2:
				if minp2 == p[0]:
					pos = p2.index(p)
					# Append the job in the final sequence
					m_for_p2.insert(0, p[1])
					# Remove that job from the list
					p1.pop(pos)
					p2.pop(pos)
		elif minp1 == minp2:
			# get index of the minimum in p1
			for p in p1:
				if minp1 == p[0]:
					pos = p1.index(p)
					# Append the job in the final sequence
					m_for_p1.append(p[1])
					# Remove that job from the list
					p1.pop(pos)
					p2.pop(pos)
	final = m_for_p1 + m_for_p2
	print ("Best Sequence is: ", final)

m = [[3,6,4,3,4,2,7,5,5,6,12], [4,5,5,2,3,3,6,6,4,7,2]]

for i in range(0, len(m)):
	c = 1
	for j in range(0, len(m[i])):
		m[i][j] = (m[i][j], c)
		c+=1
johnsonsrule(m)











