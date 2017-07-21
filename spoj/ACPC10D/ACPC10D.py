count = 1
while True:
	no_rows = int(raw_input())

	if no_rows == 0:
		break

	grid = [[10000000 for x in range(3)] for y in range(2)]

	#[None None None,
	#[None None None] 2*3

	input_arr = map(int, raw_input().split())

	grid[0][0] = 10000000
	grid[0][1] = input_arr[1]
	grid[0][2] = input_arr[1] + input_arr[2]

	r = 1

	for i in range (0, no_rows-1):
		input_arr = map(int, raw_input().split())
		_r = r ^ 1
		grid[r][0] = input_arr[0] + min(grid[_r][0], grid[_r][1])
		grid[r][1] = input_arr[1] + min(min(grid[_r][0], grid[r][0]), min(grid[_r][1], grid[_r][2]))
		grid[r][2] = input_arr[2] + min(min(grid[_r][1], grid[r][1]), grid[_r][2])

		r = _r

	print str(count) + ". " + str(grid[(no_rows -1) & 1][1])

	count = count + 1




