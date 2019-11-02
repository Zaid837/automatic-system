csv_file = open("january.csv","r")
data = csv_file.read()
print(data.split(",")[0])
logs_file = "logs.csv"
logs = open(logs_file,"w")

for i in data:
    print(i)

