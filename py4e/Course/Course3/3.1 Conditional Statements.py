# the exmaple showed in the course
x = 5
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

# nested decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')

# two-way descisions with else:
x = 4
if x > 2 :
    print('Bigger') 
else :
    print('Smaller')
print('All done')