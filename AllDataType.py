# numeric formats
n = 2025
x = 12345.6789
text = "Hello, Max !"

print(f"String: {text}")                                                # string
print(f"Decimal: {n:d}")                                                # decimal
print(f"Binary: {n:b}")                                                 # binary
print(f"Octal: {n:o}")                                                  # octal
print(f"Hex (lower): {n:x}")                                            # hex
print(f"Hex (upper): {n:X}")                                            # HEX
print(f"With prefixes: int={n:d}, hex={n:#x}, oct={n:#o}, bin={n:#b}")  # prefixed bases
print(f"Fixed 2 decimals: {x:.2f}")                                     # fixed-point
print(f"Scientific: {x:.3e}")                                           # scientific
print(f"Percent: {0.756:.1%}")                                          # percentage
print(f"Thousands sep: {1234567890:,}")                                 # comma separator
print(f"Underscore groups (binary): {n:_b}")                            # underscore groupings



def to_roman(num: int) -> str:
    if not (0 < num < 4000):
        raise ValueError("Roman numerals defined for 1..3999")
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
    ]
    out = []
    for val, sym in mapping:
        count, num = divmod(num, val)
        out.append(sym * count)
    return "".join(out)

for i in (5, 10, 50, 200, 1000):
    print(f"Roman({i}) = {to_roman(i)}")


# Mr Max 