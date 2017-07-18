import fileinput

#will be used for memoization
dict_max_value = {}

def find_maximum(num):

	#if the current num is present in dictionay, we simply return the value and do not compute it all over again
	if num in dict_max_value.keys():
		return dict_max_value[num]

	max_value = 0

	if num == 0:
		max_value = 0
	elif num == 1:
		max_value = 1
	elif num == 2:
		max_value = 2
	else:
		other_value = find_maximum(int(num/2)) + find_maximum(int(num/3)) + find_maximum(int(num/4))

		# checks if it is okay to break the number into n/2, n/3 and n/4 or not
		if other_value > num:
			max_value = other_value
		else:
			max_value = num #this is where we know that we do not need to break the number further


	dict_max_value[num] = max_value
	return max_value


for coin_value in fileinput.input():
	if len(coin_value.strip()) == 0:
		break

	print (find_maximum(int(coin_value)))

