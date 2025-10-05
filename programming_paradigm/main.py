import sys
from robust_division_calculator import safe_divide
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)
        numerator = sys.argv[1]
        denomitor = sys.ar[2]
        # Perform the division
        result = safe_divide(numerator, denomitor)
        print(result)