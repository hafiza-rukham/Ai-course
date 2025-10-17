P = float(input("Enter Principal Amount (P): "))
R = float(input("Enter Annual Interest Rate in % (R): "))
T = float(input("Enter Time in Years (T): "))
CI = P * (1 + R / 100) ** T - P
print("The Compound Interest is:", round(CI, 2))