# print a pyramid
a = int(input("enter the rows of the pyramid: "))
# input回傳的資料型態為字串，但range()裡面不能塞字串
# 只能是int
# 所以必須用int()來做資料的強制轉換
for i in range(a):
	print(" "*(a-i-1), end="")
	print("*"*(2*i+1))
