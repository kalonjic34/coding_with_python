# def count_down_from(number):
#     start = number 
#     while start > 0:
#         print(start)
#         start -=1

def count_down_from(number):
    if number <= 0:
        return
    
    print(number) #5
    count_down_from(number -1)

count_down_from(5)