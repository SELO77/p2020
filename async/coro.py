def coro():
	hello = yield 1
	foo = yield 'bar'
	yield foo 
	print("Done!!")

c = coro()
print(next(c))
print(next(c))
print(c.send('World'))
print(next(c))

