# bill=int(input())
# tip=20/100*bill
# print(tip)

# user_num=int(input("enter any number: "))
# if user_num>10:
#     print("metia 10 ze")
# elif user_num==10:
#     print("tolia 10 is")
# else:
#     print("naklebia  10ze")

math_point=int(input("Enter your point in math: "))
literature_point=int(input("Enter your point in literature: "))
biology_point=int(input("Enter your point in biology: "))
chemistry_point=int(input("Enter your point in chemistry: "))
physics_point=int(input("Enter your point in physic: "))
history_point=int(input("Enter your point in history: "))
geography_point=int(input("Enter your point in geography: "))
sum_of_points=math_point+literature_point+biology_point+chemistry_point+physics_point+history_point+geography_point
arithmetic_average=sum_of_points//7
if arithmetic_average>=9 and arithmetic_average<=10:
    print("შენი ქულაა "+str(arithmetic_average)+" გილოცავ მატრიცელო შენ მოიგე 300 ლარიანი leptop-ი")
elif arithmetic_average<=5 and arithmetic_average>=0:
    print("გილოცავ შენი ქულაა "+(arithmetic_average)+" და შენ გაექეცი მატრიცას")
elif arithmetic_average>5 and (arithmetic_average)<9:
    print(" შენი ქულაა "+str(arithmetic_average)+" YOU ARE MID")
else:
    print("you did something wrong")








