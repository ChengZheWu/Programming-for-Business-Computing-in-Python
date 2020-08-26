# read and prepare n, m, and p
n = int(input("Number of jobs: "))
m = int(input("Number of machines: "))
pStr = input("Processing times ")

p = pStr.split(" ")
for i in range(n):
	p[i] = int(p[i])

# machine loads and job assignment
loads = [0]*m
assignment = [0]*n

# in iteration j, assign job j to the least loaded machine
for j in range(n):

	# find the least loaded nachine
	leastLoadMachine = 0
	leastLoad = loads[0]
	for i in range(1, m):
		if loads[i] < leastLoad:
			leastLoadMachine = i
			leastLoad = loads[i]

	# schedule a job
	loads[leastLoadMachine] += p[j]
	assignment[j] = leastLoadMachine + 1

	# to check the process
	print(str(p[j]) + ": " + str(loads))

# the result
print("Job assignment: " + str(assignment))
print("machine loads: " + str(loads))