from urllib.request import urlopen
import json
import requests
import pandas as pd
import numpy as np
filename = "Motor_Vehicle_Collisions_-_Crashes.csv"


def get_yearly_data(df, filename):
    '''
    Extract yearly data and write into seperate csv files

    Keyword arguments:
        df: the dataframe of the original dataset
        filename: the filename of the csv file
    '''
    g = df.groupby(df['CRASH DATE'].dt.year)
    for year in g.groups.keys():
        subdf = df[df['CRASH DATE'].dt.year == year]
        subdf.to_csv(f"data/{filename[0: -4]}_{year}.csv", sep=',')


# credit: https://stackoverflow.com/questions/73044138/plotly-how-to-draw-a-zip-code-level-choropleth-map
def get_zip_json():
    '''
    get new york city zip code
    '''
    # New York Zip code
    url = 'https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/ny_new_york_zip_codes_geo.min.json'

    with urlopen(url) as response:
        ny_zip_json = json.load(response)

#     zip_code = []
#     for i in range(len(ny_zip_json['features'])):
#         code = ny_zip_json['features'][i]['properties']['ZCTA5CE10']
#         zip_code.append(code)

#     df = pd.DataFrame({'zip_code': zip_code, 'value': np.random.randint(0, 30, len(ny_zip_json['features']))})
#     df['zip_code'] = df['zip_code'].astype(str)

    return ny_zip_json


def get_contributing_factor(crashes):
    cfv1 = crashes.groupby("CONTRIBUTING FACTOR VEHICLE 1").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    cfv2 = crashes.groupby("CONTRIBUTING FACTOR VEHICLE 2").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    cfv3 = crashes.groupby("CONTRIBUTING FACTOR VEHICLE 3").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    cfv4 = crashes.groupby("CONTRIBUTING FACTOR VEHICLE 4").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    cfv5 = crashes.groupby("CONTRIBUTING FACTOR VEHICLE 5").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    c = cfv1
    c = c.add(cfv2, fill_value=0)
    c = c.add(cfv3, fill_value=0)
    c = c.add(cfv4, fill_value=0)
    c = c.add(cfv5, fill_value=0)
    c.sort_values("CRASH DATE", ascending=False)

    return c


def get_vehicle_type(crashes):
    vtc1 = crashes.groupby("VEHICLE TYPE CODE 1").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    vtc2 = crashes.groupby("VEHICLE TYPE CODE 2").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    vtc3 = crashes.groupby("VEHICLE TYPE CODE 3").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    vtc4 = crashes.groupby("VEHICLE TYPE CODE 4").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    vtc5 = crashes.groupby("VEHICLE TYPE CODE 5").count()["CRASH DATE"].sort_values(ascending=False).to_frame()
    v = vtc1
    v = v.add(vtc2, fill_value=0)
    v = v.add(vtc3, fill_value=0)
    v = v.add(vtc4, fill_value=0)
    v = v.add(vtc5, fill_value=0)
    v.sort_values("CRASH DATE", ascending=False)

    return v


def read_csv_of_year(year):
    '''
    read the csv file of the given year
    '''
    # put csv filenames into a dict, with year being the key
    crashes_filename_dict = dict.fromkeys(range(2012, 2024))
    for y in crashes_filename_dict.keys():
        crashes_filename_dict[y] = f"{filename[0: -4]}_{y}.csv"

    return pd.read_csv(f"data/{crashes_filename_dict[year]}")


def time_processing(crashes):
    '''
    add three columns: month, day and hour to the dataframe
    '''
    crashes['CRASH DATE'] = pd.to_datetime(crashes['CRASH DATE'])  # , format='%m/%d/%Y')

    month = []
    day = []
    for i in crashes["CRASH DATE"]:
        month.append(i.strftime("%m"))
        day.append(i.strftime("%d"))

    crashes["CRASH MONTH"] = month
    crashes["CRASH DAY"] = day
    crashes["CRASH HOUR"] = pd.to_datetime(crashes['CRASH TIME'], format='%H:%M').dt.hour
    crashes["DAYOFWEEK"] = crashes['CRASH DATE'].dt.dayofweek