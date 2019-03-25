import arcpy, os

dom_list = ['rigitoba', 'rigitoba2']
sub_list = ['1: first_subtype', '2: second_subtype']


for i in range(len(dom_list)):
    print dom_list[i]


for i in range(len(dom_list)):
    arcpy.AssignDomainToField_management("Main_line","type",dom_list[i],sub_list[i])

