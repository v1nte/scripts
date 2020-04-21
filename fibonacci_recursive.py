fibonacci_cache = {}

def fibonnaci(n):
	#If we have cached the value, the, return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonnaci(n-1) + fibonnaci(n-2)

	# Cache the value and return it
	fibonacci_cache[n] = value
	return value


for n in range(1,501):
	print(f"{n} = {fibonnaci(n)}")