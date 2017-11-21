#------------------
#this script how to 
#make training data
#------------------
#mha_central_borneo_21112017_01:53 UTC
#------------------------------------

import arcpy
arcpy.env.workspace = r"your_env"
rgb = r'your_raster_data'
shp = r'your_vector_data'
field = 'your_field_name'
lyr = arcpy.MakeFeatureLayer_management(shp,"lyr")
row = [row[0] for row in arcpy.da.SearchCursor(shp,field)]
for r in row :
	exp = "\"your_field_name\" = '%s'" %r #myField : 'Name' contain number with string type
	shp1= arcpy.SelectLayerByAttribute_management(lyr,"NEW_SELECTION",exp)
	arcpy.Clip_management(rgb,"#","training_data"+str(r)+".tif",shp1,"0","ClippingGeometry")
