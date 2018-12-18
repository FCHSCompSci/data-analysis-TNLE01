import matplotlib.pyplot as plt
import csv

filename = 'Pokemon.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    Names, Totals,  HPs, Attacks, Defenses, SpAtks, SpDefs, Speeds, Generations = [], [], [], [], [], [], [], [], []
    for row in reader:
        Pokemon = (row[1])
        Names.append(Pokemon)

        Total = int(row[4])
        Totals.append(Total)

        HP = int(row[5])
        HPs.append(HP)

        Attack = int(row[6])
        Attacks.append(Attack)

        Defense = int(row[7])
        Defenses.append(Defense)

        SpAtk = int(row[8])
        SpAtks.append(SpAtk)

        SpDef = int(row[9])
        SpDefs.append(SpDef)

        Speed = int(row[10])
        Speeds.append(Speed)

        Generation = int(row[11])
        Generations.append(Generation)

print(Names)
print(Totals)
print(HPs)
print(Attacks)
print(Defenses)
print(SpAtks)
print(SpDefs)
print(Speeds)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(Names, Totals, label='Total', c='b')
plt.plot(Names, HPs, label='HP', c='r')
plt.plot(Names, Attacks, label='Attack', c='g')
plt.plot(Names, Defenses, label='Defenses', c='#FFAA00')
plt.plot(Names, SpAtks, label='SpAtk', c='#FFFF00')
plt.plot(Names, SpDefs, label='SpDef', c='#C4C433')
plt.plot(Names, Speeds, label='Speed', c='#00D1FF')
plt.plot(Names, Generations, label='Generation', c='k')


plt.title("Total", fontsize=24)
plt.xlabel('Pokemon Names', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Stats', fontsize=16,)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.legend()
plt.show()


