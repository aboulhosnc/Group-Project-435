from c_project import *

test_list = list()

test_seq = 'MTEITAAMVKELRESTGAGA'
test_result = '32132223311311222222'

for i in range(24):
    test_list.append(i)

# print (test_list)
# print (test_string)

# a = ''
# b = ''
# c = ''
a, b, c = ([] for i in range(3))
for num, value in enumerate(test_list):
    if (num  % 3 == 1):
        # a = a + ',' + str(value)
        a.append(value)
    elif (num % 3 == 2):
        # b = b + ',' + str(value) + str(value)
        b.append(value)
    elif (num % 3 == 0):
        # c = c + ',' + str(value)
        c.append(value)


print(a)
print(b)
print(c)
