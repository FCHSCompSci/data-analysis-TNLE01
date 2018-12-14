import matplotlib.pyplot as plt
import csv

filename = 'Pokemon.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    Names, Totals = [], []
    for row in reader:
        Pokemon = (row[1])
        Names.append(Pokemon)
        Total = int(row[4])
        Totals.append(Total)

print(Names)
print(Totals)

Totalfig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(Names, Totals, c='red')

#testing
plt.title("Total", fontsize=24)
plt.xlabel('Pokemon Names', fontsize=16)
Totalfig.autofmt_xdate()
plt.ylabel('Stats', fontsize=16,)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()