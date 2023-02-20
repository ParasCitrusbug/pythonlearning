import csv
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
with open("csvone.csv", "w") as csvdata:
    csvwrite = csv.writer(csvdata) 
    csvwrite.writerow(df.keys())
    csvwrite.writerow(df.loc[0])
    csvwrite.writerow(df.loc[1])
    csvwrite.writerow(df.loc[2])
    