# cook your dish here
n=int(input())      #n--> limit for no of times (for loop)
for i in range(n):
    patties,buns=map(int,input().split(" "))    #get values (patties,buns)
    #print(patties,buns)
    if(buns<=patties):
        print(buns)
    else:
        print(patties)