import matplotlib.pyplot as plt
import csv
import pandas as pd

my_file = "nus_comments.csv"
df = pd.read_csv(my_file)

halls = df["body"].str.lower().str.contains('halls').sum()+df["body"].str.lower().str.contains('hall').sum()
rc = df["body"].str.lower().str.contains('rc').sum()
pgp = df["body"].str.lower().str.contains('pgp').sum()+df["body"].str.lower().str.contains('pgph').sum()
utr = df["body"].str.lower().str.contains('utr').sum()

labels = 'Halls of Residences', 'Residential Colleges', 'PGP/PGP Hall', 'UTR'
sizes = [halls, rc, pgp, utr]
colors = ['blue', 'green', 'grey','orange']

print('---------------------------------------------')
print('Frequency of Comments on Residential Options:')
print('Halls of Residences: ' + str(halls))
print('Residential Colleges: ' + str(rc))
print('PGP/PGP Hall: ' + str(pgp))
print('UTR: ' + str(utr))
print('---------------------------------------------')

# using matplotlib to plot the chart
plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
plt.title("Residential Options That Are Popular Among NUS Students")
plt.show()

