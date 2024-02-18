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
- **Data Pipeline**

Data range: 01/01/2018 - 12/31/2023
1. Automated US weather data accessing process by implementing API request from *National Centers for Environmental Information* (NCEI) website. Obtained data include 'WSF2', 'STATION', 'WSF5', 'SNOW', 'RHMX', 'ASLP', 'PRCP', 'RHAV',
       'SNWD', 'NAME', 'ASTP', 'DATE', 'RHMN', 'WDF2', 'AWND', 'WDF5', 'AWBT',
       'TMAX', 'ADPT', 'TAVG', 'TMIN', 'WT08', 'WT01', 'PGTM', 'WT02', 'WT03',
       'WT05', 'WT09', 'WT07', 'WT06', 'WT04', 'WT10', 'SX32', 'SN32', 'SX52',
       'SN52', 'PSUN', 'TSUN', 'TOBS', 'WT11', 'MDSF', 'DASF', 'WDFG', 'WSFG',
       'WESD' from 50 most populated cities (one from each state) in US.

2. Automated Canada weather data accessing process by implementing API request from *Open-Meteo* website. Obtained datat include 'temperature_2m_max', 'temperature_2m_min', 'temperature_2m_mean',
       'precipitation_sum', 'snowfall_sum', 'wind_speed_10m_max' from 18 most populated cities in Canada.

3. Downloaded csv file of Alberta specific weather data from *alberta.ca* website, which include 'township', 'air_temp._min._(°c)', 'air_temp._max._(°c)',
       'precip._(mm)', 'precip._accumulated_(mm)',
       'relative_humidity_avg._(%)', 'modelled_snow_water_equiv._(mm)',
       'incoming_solar_rad._total_(mj/m2)',
       'modelled_incoming_rad._total_(mj/m2)', 'wind_speed_10_m_avg._(km/h)'.

4. Daily natural Gas prices obtained from Uniper, and combined the csv file with daily electricity and NGTL data.

7. Monthly_Data csv file contains macro variables such as US and Canada inflation, WTI, crude oil prices, etc.

8. Other monthly data files are stored in *Other_natural_resources_data* folder, which contains oil, butane, ethane, etc. data that need to be clened in excel first before merging into 1 csv file.

---
- **Python cleaning**
1. US weather data:
- Instead of simply dropping missing values, we kept all observations (meaning we want data for each date) using the following method:
 Droped columns with more than 20,000 missing values and other irrelavent columns. For the remaining columns: 'SNOW', 'PRCP', 'SNWD', 'AWND', 'AWBT', 'TMAX', 'TMIN', used linear interpolation method for handling missing values

2. Canada weather data contains no missing values

3. For Alberta township weather data, 'Incoming Solar Rad. Total (MJ/m2)' is the only columns with missing values and linear interpolation method is used again for handling missing values.

4. For prices and other daily variable data, natural gas prices contain data from 1/1/2018 to 12/31/2023 while other variables contain data from 1/1/2017 to 11/30/2023. To keep observations consistent, we simply dropped all missing values. The cleaned dataset contains prices and other daily variable data from 1/1/2018 to 11/30/2023.

5. To keep consistency with prices, we kept observations from 1/1/2018 to 11/30/2023 only for all weather data (US,Canada,Alberta) as well


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