# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import geopandas as gpd

# Load the shapefile
gdf = gpd.read_file(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\QGIS Visualizations\New\DISTRICT_BOUNDARY.shp')

# Loop through each column in the GeoDataFrame
for col in gdf.columns:
    # Only apply the replacement to columns with string values
    if gdf[col].dtype == 'object':
        gdf[col] = gdf[col].str.replace("|", "I", regex=False)


# Save the modified GeoDataFrame to a new shapefile
gdf.to_file(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\QGIS Visualizations\New2\DISTRICT_BOUNDARY.shp')
