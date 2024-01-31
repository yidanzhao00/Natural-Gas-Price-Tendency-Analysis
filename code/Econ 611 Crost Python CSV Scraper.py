#CSV Scraper for US and Canada weather 

import os
import pandas as pd

#Set the path to the folder containing the CSV files
path = r"C:\Users\matth\OneDrive\Desktop\US_weather_data"

#Get a list of all the CSV files in the folder
csv_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

#Read the first CSV file into a DataFrame
df = pd.read_csv(csv_files[0])

#Loop through the remaining CSV files and append them to the first DataFrame
for file in csv_files[1:]:
    df_new = pd.read_csv(file)
    df = pd.concat([df, df_new], axis=1)

#Write the combined DataFrame to the first CSV file which is the master CSV file
#That will contain all the weather data
df.to_csv(csv_files[0], index=False)
