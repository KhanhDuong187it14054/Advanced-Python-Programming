# Chương 3
# 1a
a = min(2,3,4)
print("min: ",a)
# 1b 
b = max(2, -3, 4, 7, -5)
print("max: ",b)
# 1c 
c = max(2, -3, min(4, 7), -5)
print("max: ",c)

#2a
a = min(max(3, 4), abs(-5))
print("min: ",a)
#2b
b = abs(min(4, 6, max(2, 8)))
print("abs: ",b)
#2c
c = round(max(5.572, 3.258), abs(-2))
print("round: ",c)