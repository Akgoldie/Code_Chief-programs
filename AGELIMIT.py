# cook your dish here
n=int(input())      #n--> limit for no of times (for loop)
for i in range(n):
    min_age,max_age,cheif_age=map(int,input().split(" "))
    #print(max_age,cheif_age,min_age)
    if(cheif_age<max_age and cheif_age>=min_age):
        print("YES")    #Chef is eligible to take the exam.
    else:
        print("NO")     #Chef is not eligible to take the exam.
    