import csv

with open("csv_1/students.csv","r") as file:
    reader = csv.DictReader(file)

    with open("csv_1/aiml_students.csv","w", newline= "") as output:
        writer = csv.DictWriter(
            output,
            fieldnames = ["Name","Age","Branch"]
        )

        writer.writeheader()

        for row in reader:
            if row["Branch"] == "AIML":
                writer.writerow(row)

print("AIML file created!!!")                
