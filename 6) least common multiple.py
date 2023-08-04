a = int(input("enter 1st integer number: "))
b = int(input("enter 2nd integer number: "))
print ("")

divisors_a = []
divisors_b = []
common_divisors = []

# finding divisors of a:
for i in range (a):

    if a % (i+1) == 0:
        divisors_a.append(i+1)


# finding divisors of b:
for i in range (b):

    if b % (i+1) == 0:
        divisors_b.append(i+1)

# finding common divisors of a & b:
for i in range (len(divisors_a)):
    if divisors_a[i] in divisors_b:
        common_divisors.append(divisors_a[i])

print ("")

# greatest common divisor of a & b (gcd):
gcd = max (common_divisors)
# lest common multiple of a & b (lcm):
lcm = a*b / gcd

print ("✅ Lest common multiple of", a,"&", b, "is:", lcm)