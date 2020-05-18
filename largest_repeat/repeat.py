def largest_repeat_no_count(numbers):
    largest = 0
    for numb in numbers:
        if numbers.count(numb) == numb:
            largest = numb if numb > largest else largest
    return largest
    
def largest_repeat(numbers):
    largest = 0
    for numb in numbers:
        counter = 0
        for n in numbers:
            if n == numb:
                counter += 1
        if counter == numb:
            largest = numb if numb > largest else largest
    return largest
