def get_sum(numbers):
    total=0
    for number in numbers:
        if number & 1 ==0:
            total += number
    return total

numbers=[0,1,2,3,4]
print(get_sum(numbers))


#number & 1 == 0 --> checks whether the number is even. 
#number & 1 == 1 --> checks whether number is odd.