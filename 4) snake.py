n = int(input("enter the length of snake: "))
print ("")

for i in range (n-1):

    if i == n-2:
        print ("8", end="")
    if i % 2 > 0:
        print ("~", end="")
    else:
        print ("=", end="")