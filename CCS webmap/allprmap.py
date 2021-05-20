import folium, pandas, webbrowser

data = pandas.read_csv("C:/Users/shado/Desktop/allpr_lat_lon.csv")
data.columns
map = folium.Map(location=[51.521162245848394, -0.6500991267427411], zoom_start=10.3, tiles= "Open Street Map") 

pr = list(data["name"])
name = list(data["address"])
lon = list(data["Longitude"])
lat = list(data["Latitude"])
need = list(data["Need "])


fgh = folium.FeatureGroup(name="PR high")
fgm = folium.FeatureGroup(name="PR medium")
fgl = folium.FeatureGroup(name="PR low")
fgo = folium.FeatureGroup(name="PR other")


def add_child(pr_need):
    if  need == '1':
        fgl.add_child(folium.CircleMarker(
        location=[lt,ln],
        popup= '<a href="https://www.google.co.uk/maps/place/%s,%s" target="_blank">G Maps</a>' %(lt,ln),
        tooltip=str(pr) + ' ' + (name),
        radius=5,
        color = color_producer(need),
        opacity = 2.0,
        fill = True,
        fill_color = color_producer(need),
        fill_opacity = 0.7)
        )
    elif need == '2' :
        fgm.add_child(folium.CircleMarker(
        location=[lt,ln],
        popup= '<a href="https://www.google.co.uk/maps/place/%s,%s" target="_blank">G Maps</a>' %(lt,ln),
        tooltip=str(pr) + ' ' + (name),
        radius=5,
        color = color_producer(need),
        opacity = 2.0,
        fill = True,
        fill_color = color_producer(need),
        fill_opacity = 0.7)
        )
    elif need == '3'  :
        fgh.add_child(folium.CircleMarker(
        location=[lt,ln],
        popup= '<a href="https://www.google.co.uk/maps/place/%s,%s" target="_blank">G Maps</a>' %(lt,ln),
        tooltip=str(pr) + ' ' + (name),
        radius=5,
        color = color_producer(need),
        opacity = 2.0,
        fill = True,
        fill_color = color_producer(need),
        fill_opacity = 0.7)
        )
    else:
        fgo.add_child(folium.CircleMarker(
        location=[lt,ln],
        popup= '<a href="https://www.google.co.uk/maps/place/%s,%s" target="_blank">G Maps</a>' %(lt,ln),
        tooltip=str(pr) + ' ' + (name),
        radius=5,
        color = color_producer(need),
        opacity = 2.0,
        fill = True,
        fill_color = color_producer(need),
        fill_opacity = 0.7)
        )

def color_producer(pr_type):
    if  need == '1':
        return 'green'
    elif need == '2' :
        return 'orange'
    elif need == '3'  :
        return 'red'
    else:
        return 'yellow'
    

for lt,ln,pr,name,need in zip(lat,lon,pr,name,need):
    add_child(need)


map.add_child(fgh)
map.add_child(fgm)
map.add_child(fgl)
map.add_child(fgo)
map.add_child(folium.LayerControl())





map.save("C:/Users/shado/Desktop/AllPR_map.html")

