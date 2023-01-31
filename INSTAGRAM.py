# cook your dish here
n=int(input())      #n--> limit for no of times (for loop)
for i in range(n):
    num_1,num_2=map(int,input().split(" "))
    if num_1>num_2*10:
        print("YES")
    else:
        print("NO")