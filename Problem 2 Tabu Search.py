# Tabu Search!

# Given sequence!
t = [[9,9,12,3], [10,8,5,28], [14,12,1,12]]

def arrange(seq):
	# Arranging the starting sequence with the given order.
	new_t = []
	for r in t:
		row = [0]*len(r)
		for i in range(len(r)):
			row[i] = r[seq[i]-1]
		new_t.append(row)
	return new_t

def tabu_search(seq):
	# Generates different tabu list
	minimum = None
	tabu_move = []
	min_list = []
	tabu_list = []
	last_move = ()
	count=0
	print ("Initial Sequence: ", end="")
	print (seq)
	print("\n")
	# Number of Iterations
	while count<5:
		print ("Iteration "+str(count+1))
		min_list = []
		minimum = None
		for i in range(len(seq)-1):
			iter_list = [j for j in seq]
			try:
				iter_list[i], iter_list[i+1] = iter_list[i+1], iter_list[i]
			except:
				pass
			new_t = arrange(iter_list)

			# Calculating Cj
			cj = []
			first_two = new_t[0][0] + new_t[0][1]
			cj.append(new_t[0][0])
			cj.append(first_two)
			for t in range(2, len(new_t[0])):
				# Generating cj for each new tabu list
				c = first_two + new_t[0][t]
				first_two = c
				cj.append(c)

			# Calculating the tj
			tj = []
			for k in range(len(new_t[1])):
				if new_t[1][k] < cj[k]:
					tj.append(cj[k]-new_t[1][k])
				else:
					tj.append(0)

			# Calculating wj*tj
			wj = []
			for w in range(len(new_t[2])):
				wj.append(new_t[2][w]*tj[w])

			# Summation of wj and creating the tabu move list
			if not minimum:
				minimum = sum(wj)
				tabu_move = [(iter_list[i+1],iter_list[i])]
				if last_move:
					tabu_list = [last_move, (iter_list[i+1],iter_list[i])]
				else:
					tabu_list = [(iter_list[i+1],iter_list[i])]
				min_list = iter_list
			else:
				if minimum > sum(wj):
					minimum = sum(wj)
					tabu_move = [(iter_list[i+1],iter_list[i])]
					tabu_list = [last_move, (iter_list[i+1],iter_list[i])]
					min_list = iter_list

		last_move = tabu_move[0]
		seq = min_list
		count+=1
		print ("Tabu Move: ", end='')
		print (tabu_move)
		print ("Tabu List: ", end='')
		print (tabu_list)
		print ("S"+str(count+1)+": ", end="")
		print (min_list)
		print ("\n")

	print ("Best Sequence at the end of Iteration : ", str(count))
	print (end="")
	print (min_list)

# Starting with the sequence!
tabu_search([3,1,4,2])
