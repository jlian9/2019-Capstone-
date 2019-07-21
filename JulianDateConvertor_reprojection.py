import arcpy
from arcpy import env
from arcpy.sa import *
import os
arcpy.env.overwriteOutput = True

arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r'D:\Fire data\2000-2018Raster\TEMP\PRISM_tmean_stable_4kmD1_20180101_20181130_bil'

infileName = [f for f in os.listdir(r'D:\Fire data\2000-2018Raster\TEMP\PRISM_tmean_stable_4kmD1_20180101_20181130_bil') if f.endswith('.bil')]

import datetime
from datetime import datetime

for i in infileName:
    print('Now it is working on '+ i)
    doy = datetime.strptime(i[25:33],'%Y%m%d')
    tt = doy.timetuple()
    outJdate = str('%d%03d' % (tt.tm_year, tt.tm_yday))
    
    print('Updated new file named: '+ i[0:25]+outJdate + '.tif')
    arcpy.ProjectRaster_management(i,
                               r'D:\Fire data\2000-2018Raster\TEMP\PRISM_tmean_stable_4kmD1_20180101_20181130_bil\output'+'\\'+i[0:25]+outJdate + '.tif',
                               r'C:\Users\jw\Desktop\code test\fire\fire2000_2017.shp')