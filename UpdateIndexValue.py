import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True
import os
import matplotlib.pyplot as plt
from statistics import mean 


fields= ['FID','Julian_Dat','Aspct_Mean','Elev_Mean','ET_Mean','EVI_Mean','LAI_Mean','LFM_EVI','LFM_Mean','NDVI_Mean','NDWI_Mean','PPT_Mean','Temp_Mean','VIgreen','VARI']

tempSHP = r"C:\Users\jw\Desktop\code test\testOutput\temp22.shp"


Index_List = [f for f in os.listdir(r'E:\PPT 8DAY RESAMPLE 250') if f.endswith('S250.tif')]
arcpy.env.workspace = r'E:\PPT 8DAY RESAMPLE 250'


def updateIndex(fcs):
    with arcpy.da.UpdateCursor(fcs, fields) as cursor:
        for row in cursor:
                expression = 'FID=' + str(row[0])  
                row[11]=999
                cursor.updateRow(row)
                try:
                    #get the day of fire event
                    fireD = int(row[1][4:8])
                    #get the year of fire event 
                    fireY = int(row[1][0:4])

                    print('The fire day is '+str(fireD))
                    print('The fire year is '+str(fireY))

                ##create a temp mask to select with
                    try:
                        arcpy.MakeFeatureLayer_management(fcs,'temp')
                        tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
                        arcpy.CopyFeatures_management(tempMask, tempSHP)
                        #create a list to store raters name
                        tempMask = []
                        for i in Index_List:  #loop through the ETfile list 
                            ###CHANGE

                            fileDateStrDouble = i[23:30] # when i =0: "2016353"     '2017001'
                            fileDateStr = str(fileDateStrDouble)
                            fileY = int(fileDateStr[0:4])#2016                '2017'
                            fileD = int(fileDateStr[4:7])#353                 '1'
                     
                        ##get precondition period: 32 DAYS ahead of fire   
                        #no need to worry about leap year situation
                                     
                            if fireD > 32:                                              
                                day = fireD -32
                                year = fireY
                                #fireRange = str(year)+str(day)
                                #print(timePeriod)
                                #use file date comepare with timePeriod to get file fall into 32 range but 7 day(ET in this case) before fire date
                                if fileD > day and fileD <fireD-7 and fileY==fireY:
                                        print('This is the file within the range: ' + fileDateStr)
                                        tempMask.append(i)



                        #if the fire day is less than 32 it will deal with the leap year situation 
                            elif fireD < 32:
        
                                if fireY == 2001 or 2005 or 2009 or 2013 or 2017:                     #if the day is less than 32 and it is the next year of a leap year
                                    rangeY = fireY -1                                                   #set the year back 1 year 
                                    rangeD  = 366 - (32-fireD)                                           #leap year 366 days 
                                    #fireRange=str(rangeY)+str(rangeD )                                     #get 32 day ahead of fire date and creat new julian date
                                else:
                                   rangeY = fireY -1                                        
                                   rangeD = 365 - (32-fireD)                               
                                   #fireRange = str(rangeY)+str(rangeD )      
           
                                   
                                if (fileY <= fireY) and (fileY >= rangeY):
                            #files year is one year before fire
                                    if (fileY < fireY) and (fileY == rangeY):
                                        if fileD > rangeD:
                                            print("this file is within the range, the file date is "+ fileDateStr)
                                            tempMask.append(i)
                            #files year number == fire year number                                              
                                    elif fileY == fireY:
                                        if fileD < fireD-7:
                                            print("this file is within the range and has the same year number with the fire event, file date is "+ fileDateStr)
                                            tempMask.append(i)
                        
                        print(tempMask)
                        MeanValue = []
                        #loop through the selected rasters 
                        for inRaster in tempMask:

                            try:
                                outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
                                print('working on feature ID: '+ str(row[0]))
   
                                arcpy.CalculateStatistics_management(outClipMask)
                                                              
                                IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
                                MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
                                print('Mean value: ' + str(mean(MeanValue)))
                                #CHANGE THE TARGET FIELD HERE
                                row[11]=mean(MeanValue)
                                cursor.updateRow(row)
                            except:
                                continue
                    except:
                        continue
                except:
                    continue
updateIndex(r'C:\Users\jw\Desktop\code test\codeTest_Fire2017\1000NonFire.shp')
