# checks if all shps in a folder have the same field names and order

# ArcPy ListFields documentation
# http://pro.arcgis.com/en/pro-app/arcpy/functions/listfields.htm

import arcpy

# folder path
arcpy.env.workspace = r"PATH"

# takes first shp in a folder and codes field names to a list
for s in arcpy.ListFiles('*.shp'):
	fields = arcpy.ListFields(s)
	f_list = []
	for f in fields:
		f_list.append(f.name)
	break

c = 0
x = 0

# loops through folder coding field names to a new list and checking it against the original list
# if it doesn't match, it breaks the loop and prints a message
for s in arcpy.ListFiles('*.shp'):
	print s
	fields = arcpy.ListFields(s)
	f_s_list = []
	for f in fields:
		print f.name
		f_s_list.append(f.name)
	if f_list != f_s_list:
		print "FAIL"
		x = 1
		break
	else:
		print "same as before"
	c = c + 1
	print "--------------------"

# prints results
if x == 0:
	print "all shps have the same field names"
else:
	print "all shps DO NOT have the same field names"
	
