"""
You are given a list of n jobs j1, j2, . . . , jn each with a time t(j) to perform a job and a weight
w(j). We want to order the jobs as jσ(1), jσ(2), . . . jσ(n) so as to minimize the weighted sum of the time each job has
to wait before being executed. Give an efficient greedy algorithm for this problem, analyze the
complexity, and prove its optimality
"""
def min_weight(jobs):
	sorted_jobs = []
	for index, job in enumerate(jobs):
		ratio = job[1]/job[0]
		sorted_jobs.append((index, ratio))
	sorted_jobs = list(reversed(sorted(sorted_jobs, key=itemgetter(1))))
	result = []
	while len(sorted_jobs):
		max_job = sorted_jobs.pop()
		result.append(jobs[max_job[0]])
	return result