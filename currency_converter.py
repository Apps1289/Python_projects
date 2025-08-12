with open("data.txt") as f:
    lines = f.readlines()

dictlines = {}
for line in lines:
    data = line.split("\t")
    dictlines[data[0]] = data[1].strip()

print("Available currencies:\n")
for curr in dictlines.keys():
    print(curr)
    
userInp = input("Enter the exhange rate you want for NPR:")
for curr, rate in dictlines.items():
    if curr == userInp:
        print(f"1 NPR = {rate} {curr}")
        break

    


    
    