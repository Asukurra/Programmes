import folium, pandas

data = pandas.read_csv("C:/Users/shado/Desktop/pr_lat_lon.csv")
data.columns
# data.colums just returns all the colum names from the dataframe provided from pandas
map = folium.Map(location=[51.521162245848394, -0.6500991267427411], zoom_start=10.3, tiles= "Open Street Map") 

fgv = folium.FeatureGroup(name="PR locations")
pr = list(data["Proper"])
name = list(data["address"])
lon = list(data["Longitude"])
lat = list(data["Latitude"])
# we pass these as a list as it is quicker then working through a fataframe series



# the above is a better use as its modular, general convention is to moduleate most things so its easy to change/ expand on things

for lt,ln,pr,name in zip(lat,lon,pr,name):
 
    fgv.add_child(folium.CircleMarker(
    location=[lt,ln],
    popup=str(pr),
    tooltip=str(name),
    radius=10,
    opacity = 2.0,
    fill = True,
    fill_color = 'Green',
    fill_opacity = 0.7)
    )




map.add_child(fgv)


map.save("C:/Users/shado/Desktop/PR_map.html")

