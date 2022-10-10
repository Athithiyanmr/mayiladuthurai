# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import folium
from osgeo import gdal
from folium import plugins,Vega
from folium import raster_layers
#from matplotlib import cm
import numpy as np
import branca.colormap as cm
#import branca
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
from folium.plugins import MarkerCluster,FloatImage, Draw, MeasureControl
# import osmnx as ox
# import geopandas
# import vincent
# from vincent import Bar,AxisProperties, PropertySet, ValueRef
import geopandas as gpd
import os
# import plotly.graph_objects as go
# import branca
# import plotly.io as pio
# from plotly.subplots import make_subplots
from matplotlib import colors


# %%
def get_rooted(stem):
    return "D:\\LiLa_Nagapattinam\\" + stem
def read_df_UT(stem):
    return gpd.read_file(get_rooted(stem)).to_crs(epsg = 4326)


# %%

# %%

substations =gpd.read_file("workdir\\_shp_dst_substations.shp")
substations = substations["geometry"]
substations = gpd.GeoDataFrame(substations)
substations = substations.to_crs(4326)
substations.head()
substations.to_file('substations.json', driver='GeoJSON')
substations = os.path.join('', 'substations.json')

_shp_district = read_df_UT("Practice\\Nagapattinam_proj32644.shp")
_shp_district.to_file('_shp_district.json', driver='GeoJSON')
_shp_district = os.path.join('', '_shp_district.json')




m= folium.Map(location=[11.18, 79.7071], zoom_start=10)

tile = folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = False,
        control = True
       ).add_to(m)

folium.GeoJson(
    substations,
     name='substations',
    show = False,
        style_function=lambda feature: {
        'fillColor':"#dd2c0e",
        'color' : "#dd2c0e",
        'weight' : 3,
        'fillOpacity' : 0.5,
        },
#          highlight_function=lambda x: {'weight':5,'color':'yellow'},
#          tooltip=folium.features.GeoJsonTooltip(fields=['area_acres'],labels=False, toLocaleString=True)
      #smooth_factor=2.0
           
    ).add_to(m)


folium.GeoJson(
    _shp_district,
     name='dist_boundary',
    show = True,
        style_function=lambda feature: {
        'fillColor': "none",
        'color' : "black",
        'weight' : 3,
        'fillOpacity' : 0.5,
        },
#          highlight_function=lambda x: {'weight':5,'color':'yellow'},
#          tooltip=folium.features.GeoJsonTooltip(fields=['AREA'],labels=False, toLocaleString=True)
      #smooth_factor=2.0
           
    ).add_to(m)



plugins.Fullscreen(
    position="topright",
    title="Expand me",
    title_cancel="Exit me",
    force_separate_button=True,
).add_to(m)

minimap = plugins.MiniMap()
m.add_child(minimap)



# Add drawinf controls
draw = Draw()
draw.add_to(m)
m.add_child(MeasureControl())


folium.LayerControl().add_to(m)

# plugins.Geocoder().add_to(m)
m.save('D:\\LiLa_Nagapattinam\\Supporting_info\\test.html')

# %%
