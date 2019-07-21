import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r"E:\VARI"

fileList = [f for f in os.listdir(r'E:\VARI') if f.endswith('update.tif')]

#print(varilist)

#flist=['myd09a1.006_sur_refl_b01_doy2016361_aid0001.tif','myd09a1.006_sur_refl_b01_doy2017001_aid0001.tif','myd09a1.006_sur_refl_b01_doy2017009_aid0001.tif',
#       'myd09a1.006_sur_refl_b03_doy2016361_aid0001.tif','myd09a1.006_sur_refl_b03_doy2017001_aid0001.tif','myd09a1.006_sur_refl_b03_doy2017009_aid0001.tif',
#       'myd09a1.006_sur_refl_b04_doy2016361_aid0001.tif','myd09a1.006_sur_refl_b04_doy2017001_aid0001.tif','myd09a1.006_sur_refl_b04_doy2017009_aid0001.tif']

##find unique id 1
print(fileList[0][23])


###use raster b01 as the indicator and then excute the corespond b03 and b04

band1 = [ ]
band1 = [ ]
band3 = [ ]
band4 = [ ] 
band6 = [ ] 




for b1 in fileList:
    if b1[23] == "1":
        band1.append(b1)
        #b6=b1.replace('b02','b06')
        b3=b1.replace('b01','b03')
        b4=b1.replace('b01','b04')
        band3.append(b3)
        #band6.append(b6)
        band4.append(b4)

#print(band1)
#print('=======================\n')
#print(band3)
#print('=======================\n')
#print(band4)
filenum = len(band1)
print(filenum)

for i in range(filenum):
    print('now is working on: '+ band1[i])
    try:
        outVIG= (Raster(band4[i])-Raster(band1[i]))/(Raster(band4[i])+Raster(band1[i])-Raster(band3[i]))
        outVIG.save('myd09a1.006_sur_refl_doy'+band1[i][28:35]+'VARI.tif')
        print('myd09a1.006_sur_refl_doy'+band1[i][28:35]+'_VARI.tif is done!')
    except:
        continue
