def filter_even_numbers(list = []):
    even_numbers = []
    for i in list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

original = [1,2,3,4,5,6,7,8,9,10]
print("Original list: " + str(original))
print("List with even numbers only: " + str(filter_even_numbers(original)))