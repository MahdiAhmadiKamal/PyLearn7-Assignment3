numbers = []

m = int(input("enter number of numbers in your list: "))
print ("")
print ("You should enter the numbers from small to large. ⬆")

for i in range (m):
    n = float(input ("enter your number:"))
    numbers.append(n)

print ("your numbers list: ", numbers)

sorted_numbers = sorted (numbers)

if sorted_numbers == numbers:
    print ("your numbers are in order ✅")
else:
    print ("your numbers are not in order ❌")
    print ("This is how your numbers should be sorted:",sorted_numbers)
