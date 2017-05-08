'''
Break Continue Pass
'''
counter = 0
while counter < 100:
	if counter == 4:
		break # stop whenever you reach the destination
	else:
		pass # a filler statement
	print(counter)
	counter = counter + 1

#Continue method
for i in "python":
	if i == "h":
		continue
	print (i)

for i in range(0,5):
	if i < 2:
		continue # jump or exclude a certain code
	print(i)