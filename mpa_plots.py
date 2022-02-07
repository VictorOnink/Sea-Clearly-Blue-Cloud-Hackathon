"""
Data source: https://www.emodnet-humanactivities.eu/search-results.php?dataname=Natura+2000

Unzip the folder and set its path
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon

home_folder = "Hackathon/"
gdb_file = home_folder + "EMODnet_HA_Environment_Natura2000_end2020_20210909/EMODnet_HA_Environment_Natura2000_end2020_20210909.gdb"

top_lat, bottom_lat = 46, 30
left_lon, right_lon = -6, 37

full_data = gpd.read_file(gdb_file, bbox=(left_lon, bottom_lat, right_lon, top_lat))
data = full_data[full_data.COAST_MAR == 1]

print(data.columns)

shapes = data.geometry

fig = plt.figure()
Map_BOUNDS = [left_lon, right_lon, top_lat, bottom_lat]
plt.suptitle(
    "Natura 2000 sites in the Mediterranean Sea\n Source: EMODnet Human Activities")
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines(resolution='50m')
ax.stock_img()
# ax.set_global()
ax.set_extent(Map_BOUNDS)
ax.gridlines(draw_labels=True)


def plot_mpa(shape):
    for geom in shape.geoms:
        xs, ys = Polygon(geom).exterior.coords.xy
        ax.fill(xs, ys, c="red", alpha=0.8, edgecolor='k', linewidth=0.2)


[plot_mpa(s) for s in shapes]

plt.show()
