def even_generator(limit):
    for i in range(2,limit+1,2):
        # print(i)
        yield i
       
for num in even_generator(10):
    print(num)

    # The yield keyword in Python is used to create generators—functions 
    # that return values one at a time and maintain their state between calls, instead of returning all values at once like a regular function.