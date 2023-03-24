import numpy as np

def calculate(list):
	
	if len(list) < 9:
		raise ValueError("List must contain nine numbers.")
		
	matrix = np.array(list).reshape(3, 3)

	calculations = {}
	
	# mean
	means = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
	calculations['mean'] = means

	# variance
	variances = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
	calculations['variance'] = variances

	# standard deviation
	stds = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
	calculations['standard deviation'] = stds

	# max
	maxs = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
	calculations['max'] = maxs

	# min
	mins = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
	calculations['min'] = mins

	# sum
	sums = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
	calculations['sum'] = sums

	return calculations