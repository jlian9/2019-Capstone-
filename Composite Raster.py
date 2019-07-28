###############Raster calculate#####################################################################################################
import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.CheckOutExtension("Spatial")


def comp8(workpath):
    ##create list variable to store the file path name needed to be composited 
    Day1 = [ ]
    Day2 = [ ]
    Day3 = [ ] 
    Day4 = [ ]
    Day5 = [ ] 
    Day6 = [ ] 
    Day7 = [ ]
    Day8 = [ ]  
    ##generate a file name list from workpath
    File_list = [f for f in os.listdir(workpath) if f.endswith('.tif')]
    ##create a interator for name list 
    file = iter(File_list)
    arcpy.env.workspace = workpath
    ##loop through the iterator
    for i in file:
            ##filter the file already used 
            if i != Day2 and i != Day3 and i != Day4 and i != Day5 and i != Day6 and i != Day7 and i != Day8:
              try: 
                ##excute 8 successive files 
                Day1=i
                Day2=next(file)
                Day3=next(file)
                Day4=next(file)
                Day5=next(file)
                Day6=next(file)
                Day7=next(file)
                Day8=next(file)
                ##composite 8 days file and save, rename
                outFile= (Raster(Day1)+Raster(Day2)+Raster(Day3)+Raster(Day4)+Raster(Day5)+Raster(Day6)+Raster(Day7)+Raster(Day8))/8
                outFile.save('PRISM_tmean_stable_4kmD1_'+i[25:32]+'_8day.tif')
                print('PRISM_tmean_stable_4kmD1_'+i[25:32]+'_8day.tif'+ ' is done!')
              except: 
                ##if dont have 8 successive files, break the loop
                break 
