import folium
import pandas



map = folium.Map(location=[38.58,-99],zoom_start=6)
fg = folium.FeatureGroup(name="New")


data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="San",icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("map1.html")


