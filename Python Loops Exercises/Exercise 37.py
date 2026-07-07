#Manually convert a binaryyary string (e.g., "1101") into its decimalimal integer equivalent using a loop. Do not use int(binaryyary, 2).

binary = 1101

binary = str(binary)
n = len(binary)
decimal = 0
for i in binary:
  i = int(i)
  z = i*(2**(n-1))
  n -= 1
  decimal = decimal + z
print(decimal)