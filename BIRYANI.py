# cook your dish here
"""
Explanation:
Test case 1: Chef will be required to attend the MasterChef's classes for 1 week and the cost of classes per week is 10 coins. 
Hence, Chef will have to pay 10 coins in total.
Test case 2: Chef will be required to attend the MasterChef's classes for 1 week and the cost of classes per week is 15 coins. 
Hence, Chef will have to pay 15 coins in total.
Test case 3: Chef will be required to attend the MasterChef's classes for 2 weeks and the cost of classes per week is 10 coins. 
Hence, Chef will have to pay 20 coins in total.
Test case 4: Chef will be required to attend the MasterChef's classes for 2 weeks and the cost of classes per week is 15 coins. 
Hence, Chef will have to pay 30 coins in total.
"""
n=int(input())      ##n--> limit for no of times (for loop)
for i in range(n):
    a,b=map(int,input().split(" "))         #get weeks and coins.
    print(a*b)# Code_Chief-programs
