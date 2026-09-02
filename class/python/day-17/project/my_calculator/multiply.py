def product_of_numbers(*nums):
    result = 1

    for num in nums:
        result *= num

    return result