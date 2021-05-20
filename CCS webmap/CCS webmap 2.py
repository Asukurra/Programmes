# import folium
# map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles= "Stamen Terrain")

# fg = folium.FeatureGroup(name="My Map")

# for coor in [[38.2, -99.1],[32.2, -92.1]]:
#     fg.add_child(folium.Marker(location=coor, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

# # this for loop is intering through a lists of lists, adding many markers together in one go
# # then using the coor vari for the location

# map.add_child(fg)
# # this feature is the better way apparntly, using a feature group and passing this as a argument to the .add_child


# # map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# # # the above is adding a child marker to the map layer, the location needs to be long lat, popup is a string/ what happens when pop up
# # # the icon is using a built in folium icon set in the color green in this case 
# # this is apparntly a bad way to do this, use the feature groups above 

# map.save("Map1.html")

# the above is the loading from non files ,below is from a file


import folium, pandas

data = pandas.read_csv("Volcanoes.txt")
data.columns
# data.colums just returns all the colum names from the dataframe provided from pandas
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles= "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanos")
name = list(data["NAME"])
ele = list(data["ELEV"])
lat = list(data["LAT"])
lon = list(data["LON"])
# we pass these as a list as it is quicker then working through a fataframe series

#the below function is from the videos, my selection is the below
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif elevation <3000:
        return 'orange'
    else:
        return 'red'

# the above is a better use as its modular, general convention is to moduleate most things so its easy to change/ expand on things

for lt,ln,nm,ele in zip(lat,lon,name,ele):
    # if ele <1000:
    #     col = folium.Icon(color='green')
    # elif ele <3000:
    #     col = folium.Icon(color='orange')
    # elif ele >3000:
    #     col = folium.Icon(color='red')
    # the above if elif was my solution, the above method is from video

    #fgv.add_child(folium.Marker(
    # location=[lt,ln],
    #  popup="Volcano Name: \n"+(str(nm)+"\n The elevation is \n"+str(ele)+ "m")
    # , icon=folium.Icon(color=color_producer(ele)))
    # )


    fgv.add_child(folium.CircleMarker(
    location=[lt,ln],
    popup=str(ele),
    tooltip=str(nm),
    radius=10,
    color = color_producer(ele),
    opacity = 2.0,
    fill = True,
    fill_color = color_producer(ele),
    fill_opacity = 0.7)
    )
# because we are interating through 2 lists at the same time we need to pass 2 vari and use the zip function so the iterations gos
# index 0 in first list, index 0 in second list, then index 1 in first list, index 1 in second list etc
# pass these varis as the location for the .Marker method

# I have passed the for loop to have 3 args and using the name column and passing it as a str into the popup time
# I have added a varibule colour scale based on height 

fgp = folium.FeatureGroup(name="Pop map")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
 else 'purple' if x['properties']['POP2005'] <20000000
 else 'red'}))
# the lambda is a function written in a single line as apose to a def function 
# loading the world pop data from the json file - need to create a object so setting data as open *file object* because folium needs a string
# we are passing this as a .read() item at the end to make into a str, not a dict of tuples
# this dataset is loading polygons onto the map tiles as a new layer, this data is included in the json file itself and is being passed 
#through the folium.GeoJson method




map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
#the layer control adds a layer control icon in the top right of the screen 
# this has to take the function group as the layer argument so it MUST go after the add_child
# to split these layers into multipule we have split each map into its own feature group

map.save("Map2.html")

