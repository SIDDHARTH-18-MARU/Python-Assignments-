import csv
dict = {"Date": [], "Subject": []}

while True:
    date = input("Enter the date or type 'stop' to exit: ")
    if date.lower() == "stop":
        break
    subject = input("Enter the subject: ")
    dict["Date"].append(date)
    dict["Subject"].append(subject)

    print("\nCurrent Data:")
    for i in range(len(dict["Date"])):
        print("Date:", dict["Date"][i], ", Subject:", dict["Subject"][i])


with open("data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Subject"])
    for i in range(len(dict["Date"])):
        writer.writerow([dict["Date"][i], dict["Subject"][i]])
print("Data successfully written to 'data.csv'")
