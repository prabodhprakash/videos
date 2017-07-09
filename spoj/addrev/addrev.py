no_inputs = int(raw_input())

for i in range(0, no_inputs):
	input_value = raw_input().split()

	a = int(input_value[0][::-1])
	b = int(input_value[1][::-1])

	c = str(a + b)[::-1].lstrip("0")


	print (c)