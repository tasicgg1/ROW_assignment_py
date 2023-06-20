#!/usr/bin/env python
# coding: utf-8

import geopandas as gp
import pandas as pd

splice = gp.read_file('splice_points.gpkg')
#splice.head()

row_path=gp.read_file('ROW_path.gpkg')
#row_path.head()

buildings = pd.read_csv('buildings.csv')
#buildings.head()

buildings['UniqueID'] = ''
#buildings.head()

for index, row in buildings.iterrows():
   buildings.at[index, 'UniqueID'] = index + 1

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#buildings

buildings = gp.GeoDataFrame(buildings, geometry=gp.points_from_xy(buildings.Longitude, buildings.Latitude))
#buildings.head()

row_path_new=row_path.sjoin_nearest(splice, how="left",max_distance = 0.0000000000001, distance_col="Distances_from_splice")
row_path_new = row_path_new[['geometry', 'name','Distances_from_splice']]
#row_path_new.head()

buildings_new = buildings.sjoin_nearest(row_path_new, how="left",max_distance = 0.0000000000001, distance_col="Distances_from_path")
#buildings_new.head()

buildings_new['ROW Distance 1 Access Point'] = buildings_new['name']
#buildings_new.head()

buildings_new = buildings_new.drop(['name','index_right'] ,axis=1)
#buildings_new

#duplicate_rows = buildings_new[buildings_new.duplicated(subset='UniqueID', keep=False)]
#duplicate_rows.to_csv('duplicate_rows.csv', index=False)
buildings_new = buildings_new.drop_duplicates(subset='UniqueID', keep='first')

#import fiona
#fiona.supported_drivers 
#buildings_new.to_file('buildings_new1.gpkg', driver='GPKG')  
buildings_new.to_csv('buildings_new.csv', index=False)
