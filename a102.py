import random
lotto=[i for i in range(1,43)]
random.shuffle(lotto)	#隨機打亂
print(lotto[:6])	#串列切片