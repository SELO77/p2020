def simple_gen():
	print("Generator Start")
	yield 'Foo'
	yield 'Bar'
	print("Generator Done")

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
