print("Welcome to the tip calculator")

bill = float(input("What was your total bill?\n"))
tip = int(input("How much percent of tip you wanna give?\n"))
ppl = int(input("How many people to split the bill?\n"))

total = bill * ((1+tip)/100)
final = round(total/ppl,2)

print(f"Now each one should pay: {final}")