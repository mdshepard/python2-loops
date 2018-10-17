sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712, 71, 456, 21, 398,
               339, 882, 848, 179, 535, 940, 472]


# 1.print 1-20
for i in range(1, 21):
    print i


# 2. print the even numbers between 1 and 20
for i in range(2, 21, 2):
    print i

# 3. print the odd numbers between 1 and 20
for i in range(1, 20, 2):
    print i

# 4 print multiples of 5 up to 100
for i in range(5, 101, 5):
    print i

# 5 print the square numbers up to 100
for i in range(1, 11):
    print i**2

# 6 print the numbers from 1-20 backwards
for i in range(20, 0, -1):
    print i

# 7 print the even numbers backward from 20
for i in range(20, 0, -2):
    print i

# 8 print the odd numbers backward from 20
for i in range(19, 0, -2):
    print i

# 9 print multiples of 5 down from 100
for i in range(100, 0, -5):
    print i

# 10 print square numbers down from 100
for i in range(10, 0):
    print i**2

# 11 print the 20 elements of the sample array
for i in sampleArray:
    print i

# 12 print the even numbers contained in sample array
for i in sampleArray:
    if i % 2 == 0:
        print i

# 13 print the odd numbers contained in the sample array
for i in sampleArray:
    if i % 2 != 0:
        print i

# 14 print the squares of the numbers in the sample array
for i in sampleArray:
    print i**2

# 15 print the sum of all the numbers in the sample array
print sum(range(1, 21))

# 16 print the sum of all the numbers in the sample array
print sum(sampleArray)

# 17 print the smallest number in the sameple array
print min(sampleArray)

# 18 print the largest number in the sample array
print max(sampleArray)