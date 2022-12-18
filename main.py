import pandas as pd

final_data = pd.read_csv("final_stars.csv")
print(final_data.columns)

del final_data["Unnamed: 0"]
del final_data["Unnamed: 6"]
del final_data["Star_name.1"]
del final_data["Distance.1"]
del final_data["Mass.1"]
del final_data["Radius.1"]
del final_data["Luminosity"]

final_data = final_data[final_data["Mass"].notna()]
final_data = final_data[final_data["Radius"].notna()]
final_data = final_data[final_data["Distance"].notna()]

print(final_data)

final_data.to_csv("data_cleaned.csv")