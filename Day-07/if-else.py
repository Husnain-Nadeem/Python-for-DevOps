import sys 

type = sys.argv[1]

if type == "t2.micro":
    print("t2.micro is a low-cost, general-purpose instance type suitable for small workloads.")
elif type == "t2.small":
    print("t2.small is a low-cost, general-purpose instance type suitable for small workloads.")
elif type == "t2.medium":
    print("t2.medium is a low-cost, general-purpose instance type suitable for small workloads.")   
else:
    print("Unknown instance type. Please provide a valid instance type (t2.micro, t2.small, t2.medium).")
    