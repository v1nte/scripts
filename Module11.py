import sys

rut = sys.argv[1]
n = rut[::-1]

x,s = 2, 0
for i in n:
    aux = int(i)
    s = s + aux*x
    x = x+1
    if x>7:
        x=2

mod11 = str(11 - (s%11))
if mod11 == '10':
    mod11 = 'k'

print(f"{rut}-{mod11}")

