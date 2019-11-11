def gen_number(n):
	count = 0
	while count <= n:
		yield count
		count += 1
	print('Done')

g = gen_number(100)
for i in g:
	print(i)
