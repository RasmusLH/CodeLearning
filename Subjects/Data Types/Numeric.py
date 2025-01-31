# Nurmic data types include integers, floats, and complex numbers

# Intgers
a_int = 1

# Arithmetic: +, -, *, // (integer division), % (modulus), ** (exponentiation).
# Division:
# Single slash / performs floating-point division (even between two ints).
# Double slash // performs integer (floor) division.
# Bitwise: & (AND), | (OR), ^ (XOR), << (left shift), >> (right shift).

x = 7
y = 3
print(x / y)   # 2.3333333333 (float result)
print(x // y)  # 2 (integer (floor) division)
print(x % y)   # 1 (remainder)
print(x ** y)  # 343

# Floats
a_float = 1.0

# Rounding Errors: Operations like 0.1 + 0.2 can yield unexpected results (e.g., 0.30000000000000004). 
# This is due to binary floating-point representation.
# To avoid this, use the decimal module or round the result.
pi = 3.1415926535
small_num = 1.23e-4      # 0.000123
large_num = 1.23e+4      # 12300.0


# Complex numbers
# A complex number has a real part and an imaginary part, in Python typically written with a j suffix for the imaginary part.
# Complex numbers are created using the complex() function or by using the j suffix.
# The real and imaginary parts can be accessed using the .real and .imag attributes.

a_complex = 1 + 2j
b_complex = complex(1, 4)
c_complex = b_complex + a_complex # (2+6j)


# Type Conversion
x = 3
y = 3.7
z = 1 + 2j

# Convert int to float
float_x = float(x)  # 3.0

# Convert float to int (truncates towards zero)
int_y = int(y)      # 3

# Convert float to complex
complex_y = complex(y)  # (3.7+0j)

# Convert int to Decimal
from decimal import Decimal
decimal_x = Decimal(x)  # Decimal('3')

# Convert float to Fraction
from fractions import Fraction
fraction_y = Fraction(y) # Fraction(37, 10)
