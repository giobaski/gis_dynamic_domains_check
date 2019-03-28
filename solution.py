import arcpy, os

# Set the workspace
arcpy.env.workspace = os.path.join(os.getcwd(),"test.gdb")

# Set local parameters
GDB = "test.gdb"
featureClass = "test"

jobs_table = r"C:\Users\gtsipuria\Desktop\GITHUB_clone\gis_dynamic_domains_check\dynamic_domains_check.gdb\I_Shesasrulebeli_Samushaoebi"
fields = ["ID", "NAME", "WORK_TYPE_NAME", "ACC_WORK_GROUP"]


###ეს ბლოკი ქმნის ცხრილიდან დომეინების სახელებს და შესაბამის CODE?DESCRIPTION სამუშაოების მიხედვით
                                                # მაგ:.      "ჭის მონტაჟი":{
                                                #                          1314 : "გოფრირებული მილი 25მმ",
                                                #                          1307 : "ქვიშის ბალიშის მოწყობა (#PX0.35X0.1)"
                                                #                          },

subtype_list = []
with arcpy.da.SearchCursor(jobs_table, fields) as cursor:
    for row in cursor:
        ACC_WORK_GROUP = row[3]
        if ACC_WORK_GROUP not in subtype_list:
            if ACC_WORK_GROUP:
                subtype_list.append(ACC_WORK_GROUP)
    #print(subtype_list)


domains_dict = {}
for sub in subtype_list:
    dict = {}
    with arcpy.da.SearchCursor(jobs_table, fields) as cursor:
        for row in cursor:
            ACC_WORK_GROUP = row[3]
            if ACC_WORK_GROUP == sub:
                JOB_ID = int(row[0])
                JOB_NAME = row[1]
                dict[JOB_ID] = JOB_NAME
    domains_dict[sub] = dict
# print(domains_dict)




#### SUBTYPES: ###
try:
    # Process: Set Subtype Field...
    arcpy.SetSubtypeField_management(featureClass, "subtype")

    # Process: Add Subtypes...
    # Store all the suptype values in a dictionary with the subtype code as the "key" and the
    # subtype description as the "value" (stypeDict[code])
    # stypeDict = {"0": "'ODF-ი'","1": "P2P ინსტალაცია","2": "არხის მშენებლობა","3": "ბოძის მონტაჟი","4": "კაბელის მონტაჟი","5": "კარადის მონტაჟი","6": "სპლიტერი","7":"ქურო","8": "ჭის მონტაჟი",}
    #Create dict from list!!!
    subtypeDict = {}
    for i in range(len(subtype_list)):
        subtypeDict[str(i)] = subtype_list[i]
    print(subtypeDict)

    # use a for loop to cycle through the dictionary
    for code in subtypeDict:
        arcpy.AddSubtype_management(featureClass, code, subtypeDict[code])

    # Process: Set Default Subtype...
    # arcpy.SetDefaultSubtype_management(featureClass, 4)
except Exception as err:
    print(err.args[0])





#### DOMAINS: ###
try:
    # დომეინების შექმნა ბუღალტრული კატეგორიის სახელების მიხედვით
    for key, value in domains_dict.items():
        domain_name = key
        domain_description = key
        arcpy.CreateDomain_management(GDB,domain_name,domain_description,"SHORT", "CODED", "DEFAULT", "DEFAULT")

    # დომეინებისთვის კოდების მინიჭება სამუშაოების ID/Name მიხედვით
    for key, value in domains_dict.items():
        for value_ID, value_name in value.items():
            domain_name = key
            code = value_ID
            code_description = value_name
            arcpy.AddCodedValueToDomain_management(GDB, domain_name, code, code_description)

    #არსებული დომეინების მინიჭება საბტაიპის შესაბამის კოდებზე
    ListSubtypes = arcpy.da.ListSubtypes(featureClass)
    sub_dict = {}
    for k,v in ListSubtypes.items():
        field_name = "Type"
        domain_name = v["Name"] #საბტაიპის სახელი უნდა დაემთხვეს დომეინის სახელს, პითონ 2-ში სხვანაირად უნდა აიღო სახელი
        subtype_code = str(k) + ":" + v["Name"]
        print(subtype_code)
        arcpy.AssignDomainToField_management(featureClass, field_name, domain_name, subtype_code)
except Exception as err:
    print(err.args[0])