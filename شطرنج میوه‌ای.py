def fruits(tuple_of_fruits):
	result = dict()
	for fruit in tuple_of_fruits:
		if fruit['shape'] == 'sphere':
			if 300 <= fruit['mass'] <= 600:
				if 100 <= fruit['volume'] <= 500:
					if fruit['name'] not in result.keys():
						result[fruit['name']] = 1
					else:
						result[fruit['name']] += 1

	return result
