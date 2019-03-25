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
    fields = ["ID", "NAME", "WORK_TYPE_NAME", "ACC_WORK_GROUP"]

    cursor = arcpy.da.SearchCursor(jobs_table, fields)
    sub_list = []
    for row in cursor:
        if row[-1] not in sub_list:
            sub_list.append(row[-1])
    sub_list = filter(None, sub_list)

    cursor = arcpy.da.SearchCursor(jobs_table, fields)
    for i in range(len(sub_list)):
        list = []
        for row in cursor:
            if row[-1] == sub_list[i]:
                list.append(row[0])
        print (str(i)+ ": ")
        print (list)

    # domains_Dict = {}
    # for i in range(len(sub_list)):
    #     stypeDict[i] = sub_list[i]


except Exception as err:
    print(err.args[0])
