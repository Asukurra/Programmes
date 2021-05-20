import os
import pandas
from geopy.geocoders import ArcGIS

df1=pandas.read_csv("C:/Users/shado/Desktop/Python jazz/MegaC folder/Programmes/CCS webmap/all_pr.csv", encoding='windows-1252')

nom = ArcGIS()

# df1["Address"] =df1["Town/City"]+ ", " + df1["County"]+", " + df1["PostCode"]

df1["Coordinates"]=df1["address"].apply(nom.geocode)

df1["Latitude"] = df1["Coordinates"].apply(lambda x:x.latitude)
df1["Longitude"] = df1["Coordinates"].apply(lambda x:x.longitude)

df1.to_csv("C:/Users/shado/Desktop/allpr_lat_lon.csv")