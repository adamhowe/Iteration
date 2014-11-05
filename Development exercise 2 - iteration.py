
per_row = int(input("Enter the amount of stars you want per row: "))
lines = int(input("Enter how many lines of stars you want: "))

for counter in range (lines):
    stars = "*" * per_row
    print(stars)

