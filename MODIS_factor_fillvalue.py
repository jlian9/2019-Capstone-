import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = r"D:\Fire data\2000-2018Raster\SR Band12346\band4"
flist = [f for f in os.listdir(r'D:\Fire data\2000-2018Raster\SR Band12346\band4') if f.endswith('.tif')]

inConstant = 0.0001
for i in flist:
    print('working on: '+i)
    inRaster = ExtractByAttributes(i,'VALUE>= -100 and VALUE<=16000' ) 
    outTimes = Times(inRaster,inConstant)
    outTimes.save('MYD09A1.006_sur_refl_b04_doy'+i[28:35]+'_aid0001_update.tif')