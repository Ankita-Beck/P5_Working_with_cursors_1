"""
Three different type of cursors
1. Search cursor - reads only the attribute table
2. Update Cursor - updating the attribute table
3. Insert Cursor - Creating new row in the attribute data

"""

import arcpy
import os

gdb_path = r"D:\Programming_for_GIS_3\P5_Working_with_cursors_1\ProProject_Cursors\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join (gdb_path ,fc_name)

field_list = ["NAME","ESTAB","ZIP"]

#  use a search cursor to establish a read only access to the feature class

# search_cursor = arcpy.da.SearchCursor(fc_path,field_list)
#
# for row in search_cursor:
#     print("{},{},{}".format(row[0] , row[1] , row[2]))
#
# print("Process completed")
# 0 stands for the index number in the attribute table

with arcpy.da.SearchCursor(fc_path,field_list) as search_cursor:
    for row in search_cursor:
        print("{},{},{}".format(row[0],row[1],row[2]))

print("Process completed")