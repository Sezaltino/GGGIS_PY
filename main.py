import geopandas as gpd
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = (20, 10)
df_places = gpd.read_file('./Lisboa.geojson')