# Convert comma delimited csv to semicolon delimited (for compatibility with excel)
# Particularly useful if the csv file is big
# By Stephen Larroque, 2017
import sys
filepath = sys.argv[1]
with open(filepath, 'r') as f:
    a = f.read()

b = a.replace(',', ';')
with open(filepath[:-4]+'_excel.csv', 'w') as f2:
    f2.write(b)