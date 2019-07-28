##import library
import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r"E:\VARI"

##generate a file list end with 'update.tif' from target folder
###all bands rasters are stored in same folder and the only difference part from file name is "b01"|'b02'|'b03'..etc 
fileList = [f for f in os.listdir(r'E:\VARI') if f.endswith('update.tif')]



###use raster b01 as the indicator and then excute the corespond b03 and b04
##crate list variable to store path name for each band
band1 = [ ]
band1 = [ ]
band3 = [ ]
band4 = [ ] 
band6 = [ ] 



##loop the all file list
for b1 in fileList:
    ##if this is band 1 file, append it to 'band1' list 
    if b1[23] == "1":
        band1.append(b1)
        
        ##replace the 'b01' by other bands number'b03' and 'b04' to get the file path name for band3 and band4
        b3=b1.replace('b01','b03')
        b4=b1.replace('b01','b04')
        ##append path name to 'band3' list
        band3.append(b3)
        band4.append(b4)

##get the file number of band1 
filenum = len(band1)

##loop the file base on the file number in the list 
for i in range(filenum):
    print('now is working on: '+ band1[i])
    try:
        ##excute the [i] order of the file in the list and do the raster calculation
        outVIG= (Raster(band4[i])-Raster(band1[i]))/(Raster(band4[i])+Raster(band1[i])-Raster(band3[i]))
        ##save the output and rename 
        outVIG.save('myd09a1.006_sur_refl_doy'+band1[i][28:35]+'VARI.tif')
        print('myd09a1.006_sur_refl_doy'+band1[i][28:35]+'_VARI.tif is done!')
    except:
        continue
