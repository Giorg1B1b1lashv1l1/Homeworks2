##ticket price is 25$,but tickets are free for children
#we have 13 person,10 adult and 3 child
#and they want to buy ticket,how much they should  pay for all of this tickets
sum=0
i=25
x=13
while x>0:
    sum+=i
    x-=1 
    if x==3:
        break  
print(sum)

