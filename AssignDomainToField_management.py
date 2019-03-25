#!/usr/bin/python
# -*- coding: utf-8 -*-

# Name: MakeDomain.py
# Description: Create an attribute domain to constrain pipe material values
# Author: ESRI


# Import system modules
import arcpy, os

try:
    # Set the workspace (to avoid having to type in the full path to the data every time)
    arcpy.env.workspace = os.path.join(os.getcwd(),"dynamic_domains_check.gdb")

    # Set local parameters
    domName = "Material8"
    gdb = "dynamic_domains_check.gdb"
    inFeatures = "Main_line"
    inField = "Type"

    # Process: Create the coded value domain
    arcpy.CreateDomain_management("dynamic_domains_check.gdb", domName, "Valid pipe materials", "SHORT", "CODED")

    # Store all the domain values in a dictionary with the domain code as the "key" and the
    # domain description as the "value" (domDict[code])
    domDict = {1: "Cast iron", 2: "Ductile iron", 3: "PVC", 4: "Asbestos concrete", 5: "Copper"}

    # Process: Add valid material types to the domain
    # use a for loop to cycle through all the domain codes in the dictionary
    for code in domDict:
        arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

    # Process: Constrain the material value of distribution mains
    arcpy.AssignDomainToField_management(inFeatures, inField, domName,'0: არხის მშენებლობა')

except Exception as err:
    print(err.args[0])