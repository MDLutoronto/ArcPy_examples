# example script for adding/deleting the same fields to multiple shps in a folder

# ArcPy delete field documentation = http://pro.arcgis.com/en/pro-app/tool-reference/data-management/delete-field.htm
# ArcPy add field documentation = http://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm

import arcpy

# directory path
arcpy.env.workspace = r"PATH"

count = 0

# loop through shps in the directory
for f in arcpy.ListFiles('*.shp'):
	print f

	# deleting fields "AREA" and "PERIMETER"
	arcpy.DeleteField_management(f, ["AREA","PERIMETER"])

	# adding fields "CT_NAME" and "CTUID" with lengths 7 and 11 and as type text
	arcpy.AddField_management(f, "CT_NAME", "TEXT", "", "", 7)
	arcpy.AddField_management(f, "CTUID", "TEXT", "", "", 11)

	count = count + 1

print "------------------------------"
print "number of shps checked:"
print count
