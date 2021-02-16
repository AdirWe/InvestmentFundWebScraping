import csv

"""
with open("data.csv", "r") as csv_data:
    csv_reader = csv.reader(csv_data)
    # print(csv_reader)
    for row in csv_reader:
        print(row)
"""
array = []

with open("data.csv", "r") as csv_data:
    csv_dict_reader = csv.DictReader(csv_data)
    # print(csv_reader)
    for row in csv_dict_reader:
        age = int(row["age"])
        gender = row["gender"]
        if age >= 20 and gender == "male":
            array.append({
                "name": row["name"],
                "lastName": row["lastName"]
            })

with open("onlyBigMales.csv", "w", newline="") as newFile:
    fieldNames = ["name", "lastName"]
    csv_dict_writer = csv.DictWriter(newFile, fieldnames=fieldNames)
    csv_dict_writer.writeheader()

    for person in array:
        csv_dict_writer.writerow(person)
        

def main():
    pass

if __name__=="__main__":
    main()