#!/usr/bin/python
# -*- coding: utf-8 -*-

# Name: ManageSubtypes.py
# Purpose: Create a subtype definition
# Author: ESRI

# Import system modules
import arcpy, os
 
try:
    # Set the workspace (to avoid having to type in the full path to the data every time)
    arcpy.env.workspace = os.path.join(os.getcwd(),"dynamic_domains_check.gdb")
    
    
    # Set local parameters
    inFeatures = "Main_line"

    # Create domain list from jobs table
    jobs_table = "I_Shesasrulebeli_Samushaoebi"
    fields = ["ID","NAME","WORK_TYPE_NAME","ACC_WORK_GROUP"]

    cursor = arcpy.da.SearchCursor(jobs_table, fields)
    sub_list = []
    for row in cursor:
        if row[-1] not in sub_list:
            sub_list.append(row[-1])
    sub_list = filter(None, sub_list)


    # Process: Set Subtype Field...
    arcpy.SetSubtypeField_management(inFeatures, "subtype")

    # Process: Add Subtypes...
    # Store all the suptype values in a dictionary with the subtype code as the "key" and the
    # subtype description as the "value" (stypeDict[code])
    # stypeDict = {"0": "'ODF-ი'","1": "P2P ინსტალაცია","2": "არხის მშენებლობა","3": "ბოძის მონტაჟი","4": "კაბელის მონტაჟი","5": "კარადის მონტაჟი","6": "სპლიტერი","7":"ქურო","8": "ჭის მონტაჟი",}
    stypeDict = {}
    for i in range(len(sub_list)):
        stypeDict[i] = sub_list[i]


    # use a for loop to cycle through the dictionary
    for code in stypeDict:
        arcpy.AddSubtype_management(inFeatures, code, stypeDict[code])

    # Process: Set Default Subtype...
    arcpy.SetDefaultSubtype_management(inFeatures, 4)
 
except Exception as err:
    print(err.args[0])
