# PROJECT Description:

Organization: Uniper Trading Canada Ltd

Project Title: How do weather conditions and natural gas production levels in Alberta impact natural gas
prices?

Problem Statement: Weather conditions have a large impact on natural gas prices through their effect
on heating fuel consumption and electricity generation. A good understanding of the impact of weather
on gas prices is needed to inform trading strategies.

Objective: Determine if there is a correlation between weather patterns (like cold snaps or heat waves)
and natural gas prices, analyze the relationship between production levels and prices. Forecast
Scenarios. This is an El Nino year - outline some extraordinary weather scenarios accompanied by some
possible expected prices.

Data: There are numerous public datasets that may be useful in the analysis. Some examples are
provided here - feel free to look for others.

- Alberta Natural Gas Prices: The Alberta government provides historical natural gas reference
prices from 1994 to the present. These prices are available monthly by year and can be a vital
source for analyzing price trends. Access the data at: https://www.alberta.ca/alberta-natural-gas-reference-price

- Alberta Historical Weather Data: The Alberta Climate Information Service (ACIS) offers an online
interactive Historical Weather Data Viewer. This tool allows users to view daily meteorological
records for numerous points across the province dating back to 1961. The data can be viewed as
tables or graphs and downloaded for further analysis. Access the data at:
https://www.alberta.ca/acis-find-historic-climate-data

- Alberta Natural Gas Production Data: The Alberta Energy Regulator provides detailed
information on the average daily production of marketable natural gas in Alberta. The data
includes historical trends and forecasts for future production. The data is available in an XLSX
format, which is suitable for analysis. Access the data at: https://www.aer.ca/providing-information/data-and-reports/statistical-reports/st98

## Data Analysis Outline

### 1. Data Preparation and Cleaning
- **Excel file cleaning**
1. In *data_files* folder, created seperated folders for daily, monthly, quarterly, and yearly folders.

2. In *Daily_data* folder, <font color='red'><u>**Daily_data**</u></font> csv file is created with natural gas prices, electricity data, and NGTL data. Other daily data files are stored in *Other_daily_data* folder; these files have different number of observations (e.g., weekends and holidays have already been excluded) which cannot be directly merged with *Daily_data* csv file.

3. In *Monthly_data* folder, two seperated weather data folders are created for US and Canada

4. Used Python CSV Scraper code to combine all 50 US weather data files into one csv file: <font color='red'><u>**combined_us_weather_data**</u></font> (deleted "Station code" column). **File directory: *data files* > *Monthly_data* > *US_weather_data***

5. Used Python CSV Scraper code to combine all 19 Canada weather data files into one csv file: <font color='red'><u>**combined_ca_weather_data**</u></font> (deleted "Longitude (x)", "Latitude (y)", "Climate ID", "Data Quality", "Max Temp Flag", "Min Temp Flag", "Mean Temp Flag", "Heat Deg Days Flag", "Cool Deg Days Flag", and other "flag" columns). **File directory: *data files* > *Monthly_data* > *CA_weather_data***

6. In <font color='red'><u>**alberta_weather**</u></font> csv file, which contains weather data of Alberta townships, deleted: "Air_Temp._Min._(°C)_interpolation_flags", and other "flags" columns. **File directory: *data files* > *Monthly_data* > *CA_weather_data***

7. <font color='red'><u>**Monthly_Data**</u></font> csv file contains macro variables such as US and Canada inflation, WTI, crude oil prices, etc.

8. Other monthly data files are stored in *Other_natural_resources_data* folder, which contains oil, butane, ethane, etc. data that need to be clened in excel first before merging into 1 csv file.

- **Python cleaning**
1. Check the data type of all columns:

Example: daily_df.dtypes

2. Convert date column into datetime objects if they are not in datetime type already:

Example: 
price_df['Date'] = pd.to_datetime(price_df['Date'])

3. Renaming all columns to add underscores

Example: 
daily_df.columns=daily_df.columns.str.replace(' ', '_')

4. Handling missing values
If it's reasonble to assume the last missing value is similar to the last available value, replace missing values (NaNs) using forward fill or backward fill

Example: 
df.fillna(method='ffill')  # Forward fill
df.fillna(method='bfill')  # Backward fill


### 2. Exploratory Data Analysis
* Summary statistics overview (mean, median)
* Weather pattern analysis (categorize temperature, extraordinary weather conditions, etc)
* Trend detection (seasonal trends or pattern)

### 3. Correlation Analysis
* Scatter plots
* Heatmaps
* Linear regression

### 4. Forecasting
* ARIMA
* Mchine learning
* El Niño impact