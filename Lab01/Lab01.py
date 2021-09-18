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

#3 function: num*3
def triple(num):
 return num * 3
print(triple(2))

#4 function: 2 num , abs
def absolute_difference(number1, number2):
 return abs(number1 - number2)
print(absolute_difference(1,5))

#5 function: km -> miles
def km_to_miles(km):
 return km / 1.6
print(km_to_miles(10))

#6 function: 3num, average
def average_grade(grade1, grade2, grade3):
 return (grade1 + grade2 + grade3) / 3
print(average_grade(2,3,4))

#7 function: 4num, average of 3 max num
def top_three_avg(grade1, grade2, grade3, grade4):
    total = grade1 + grade2 + grade3 + grade4
    top_three = total - min(grade1, grade2, grade3, grade4)
    return top_three / 3
print(top_three_avg(50,60,70,80))

 #other solution
def top_three_avg_2(grade1, grade2, grade3, grade4):
    return max(average_grade(grade1, grade2, grade3),
           average_grade(grade1, grade2, grade4),
           average_grade(grade1, grade3, grade4),
           average_grade(grade2, grade3, grade4))
print(top_three_avg_2(50,60,70,80))

#8 day1 and day2 are days in the same year. Return the number of full weeks
#that have elapsed between the two days.
def weeks_elapsed(day1, day2):
    days = max(day1,day2) - min(day1,day2)
    weeks = days // 7;
    return weeks
print(weeks_elapsed(20,3))

#9 #10 : function: square of num
def square(num):
    return num ** 2
print(square(4))