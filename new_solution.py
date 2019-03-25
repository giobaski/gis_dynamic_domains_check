import arcpy, os

arcpy.env.workspace = os.path.join(os.getcwd(),"dynamic_domains_check.gdb")


# #subtype list
# subs = arcpy.da.ListSubtypes('Main_line')
# sub_dict = {}
# for k,v in subs.items():
#     sub_dict[k] = v["Name"]
# print (sub_dict)

#საბტაიპების სია დინამიურად უნდა ამოვიღოთ ListSubtypes-ს საშუალებით
subtype_list = {0: 'არხის მშენებლობა',
                1: 'კაბელის მონტაჟი',
                2: 'P2P ინსტალაცია',
                3: 'კარადის მონტაჟი',
                4: 'ბოძის მონტაჟი',
                5: 'ქურო',
                6: 'ODF-ი',
                7: 'ჭის მონტაჟი',
                8: 'სპლიტერი'}

#ეს სია უნდა შეიქმნას სამუშაოების ცხრილიდან დინამიურად:
domain_list = {
        "არხის მშენებლობა": {
                            1314 : "გოფრირებული მილი 25მმ",
                            1307 : "ქვიშის ბალიშის მოწყობა (#PX0.35X0.1)",
                            1310 : "გოფრირებულdsdsი მილი 25მმ",
                            1301 : "ქვიშის ბdsdsალიშის მოწყობა (#PX0.35X0.1)"
                            },
        "კაბელის მონტაჟი" : {
                            2363 : "კაბელი/ტპპ/7/4/მეორადი-ის დემონტაჟი",
                            2394 : "კაბელი ოპტიკური/ADSS/12-ის მონტაჟი ტრანზიტულად"
                            },
        "P2P ინსტალაცია": {
                            1253 : "როუტერი/D-Link/4port/Dir100/Router-ის მონტაჟი",
                            1285 : "ONT/GPON/4 port/HG850a/HUAWEI მონტაჟი"
                            },
        "კარადის მონტაჟი": {
                            1160 : "გამანაწილებელი კარადა 600X2-ის მონტაჟი",
                            1122 : "GPON-ის სასადგურე კარადის მონტაჟი FIST-GR3-900-1"
                            },
        "ბოძის მონტაჟი":  {
                             2007 : "ბოძი/ძირითადი/8.1მ-ის მონტაჟი",
                             2206 : "ბოძი/ხის/მეორადი"
                            },
        "ქურო":          {
                            2346 : "ქუროს სამონტაჟო კომპლექტი/FOSC-A/B-UNI-MOUNT-A-ის მონტაჟი",
                            2076 : "ქურო გამანაწილებელი/500/2-600/2/6 თითიანი/6MRP 5/6-ის მონტაჟი"
                            },
        "ODF-ი":          {
                            1314 : "გოფრირებული მილი 25მმ",
                            1307 : "ქვიშის ბალიშის მოწყობა (#PX0.35X0.1)"
                            },
        "ჭის მონტაჟი":   {
                            1314 : "გოფრირებული მილი 25მმ",
                            1307 : "ქვიშის ბალიშის მოწყობა (#PX0.35X0.1)"
                            },
        "სპლიტერი":     {
                            1677 : "ოპტიკური სპლიტერი/PLC/1:4/კონექტორის გარეშე -  მონტაჟი",
                            1683 : "ოპტიკური სპლიტერი/PLC/1:8/SC/PC/კასეტით -  მონტაჟი "
                            }
        }
#ბეჭდავს ბაზაში არსებული დომეინების სიას, რა ტრაკში სატხრეალდ მინდა ჯერ არ ვიცი
dom = arcpy.da.ListDomains("test.gdb")
for d in dom:
    print(d.name)


#დომეინების შექმნა ბუღალტრული კატეგორიის სახელების მიხედვით
# for key, value in domain_list.items():
#     arcpy.CreateDomain_management("test.gdb",key,key,"SHORT", "CODED", "DEFAULT", "DEFAULT")

#დომეინებისთვის კოდების მინიჭება სამუშაოების ID/Name მიხედვით
# for key, value in domain_list.items():
#     for value_key, value_value in value.items():
#         arcpy.AddCodedValueToDomain_management("test.gdb",key, value_key,value_value)



#subtype list
subs = arcpy.da.ListSubtypes(r'C:\Users\gtsipuria\Desktop\GITHUB_clone\gis_dynamic_domains_check\test.gdb\Main_line')
sub_dict = {}
for k,v in subs.items():
    print(v)
    name = v["Name"]
    subname = str(k) + ":" + v["Name"]
    print(subname)
    # sub_dict[k] = v["Name"]
    arcpy.AssignDomainToField_management(r'C:\Users\gtsipuria\Desktop\GITHUB_clone\gis_dynamic_domains_check\test.gdb\Main_line', "type",name,subname)
print(sub_dict)


#
# for code in domDict:
#     arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

# dom_list = ['rigitoba', 'rigitoba2']
# sub_list = ['1: first_subtype', '2: second_subtype']
#
#
# for k,v in subtype_list.items():
#     print(domain_list[v])
#
# # arcpy.AssignDomainToField_management("Main_line","type",dom_list[i],sub_list[i])
#
#     arcpy.AssignDomainToField_management("Main_line","type",domain_list[v])