import numpy as np


def calculate(list):

	if len(list) < 9:
		raise ValueError("List must contain nine numbers.")

	matrix = np.array(list).reshape(3, 3)

	calculations = {}

	# mean
	means = []
	means.append(np.mean(matrix, axis=0).tolist())
	means.append(np.mean(matrix, axis=1).tolist())
	means.append(np.mean(matrix).tolist())
	calculations['mean'] = means

	# variance
	variances = []
	variances.append(np.var(matrix, axis=0).tolist())
	variances.append(np.var(matrix, axis=1).tolist())
	variances.append(np.var(matrix).tolist())
	calculations['variance'] = variances

	# standard deviation
	stds = []
	stds.append(np.std(matrix, axis=0).tolist())
	stds.append(np.std(matrix, axis=1).tolist())
	stds.append(np.std(matrix).tolist())
	calculations['standard deviation'] = stds

	# max
	maxs = []
	maxs.append(np.max(matrix, axis=0).tolist())
	maxs.append(np.max(matrix, axis=1).tolist())
	maxs.append(np.max(matrix).tolist())
	calculations['max'] = maxs

	# min
	mins = []
	mins.append(np.min(matrix, axis=0).tolist())
	mins.append(np.min(matrix, axis=1).tolist())
	mins.append(np.min(matrix).tolist())
	calculations['min'] = mins

	# sum
	sums = []
	sums.append(np.sum(matrix, axis=0).tolist())
	sums.append(np.sum(matrix, axis=1).tolist())
	sums.append(np.sum(matrix).tolist())
	calculations['sum'] = sums

	return calculations
