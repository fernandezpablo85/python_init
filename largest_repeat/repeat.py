def largest_repeat(numbers):
    largest = 0
    for numb in numbers:
        if numbers.count(numb) == numb:
            largest = numb if numb > largest else largest
    return largest
    
