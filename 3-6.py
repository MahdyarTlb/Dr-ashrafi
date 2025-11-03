def print_pascal_optimized(n):

    for i in range(n):
        current_row = [1] * (i + 1)
        
        for j in range(1, i):
            current_row[j] = current_row[j-1] * (i - j + 1) // j
        
        spaces = ' ' * (n - i - 1)
        print(f"{spaces}{' '.join(map(str, current_row))}")

print_pascal_optimized(6)