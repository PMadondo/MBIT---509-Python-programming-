def product_of_multiples(factor, limit):
    product = 1
    for number in range(factor, limit, factor):
        product *= number
    return product


# --- Example usage / quick test ---
if __name__ == "__main__":
    print(product_of_multiples(3, 15))   # 3 * 6 * 9 * 12 = 1944
    print(product_of_multiples(5, 20))   # 5 * 10 * 15 = 750
    print(product_of_multiples(2, 10))   # 2 * 4 * 6 * 8 = 384