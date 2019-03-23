subtypes = {
    1: {
         'Default': True,
         'Name': u'first_subtype',
         'SubtypeField': u'subtype',
         'FieldValues': {
                     u'subtype': (None, '<Workspace Domain object object at 0x07DF44A0>'),
                     u'SHAPE': (None, None),
                     u'type': (None, None),
                     u'SHAPE_Length': (None, None),
                     u'OBJECTID': (None, None)
                     }
            },
     2: {
         'Default': False,
         'Name': u'second_subtype',
         'SubtypeField': u'subtype',
         'FieldValues': {
                     u'subtype': (None, '<Workspace Domain object object at 0x07DF4530>'),
                     u'SHAPE': (None, None),
                     u'type': (None, None),
                     u'SHAPE_Length':(None, None),
                     u'OBJECTID': (None, None)
                     }
         }
}



for stcode, stdict in list(subtypes.items()):
    print('Code: {0}'.format(stcode))
    for stkey in list(stdict.keys()):
        if stkey == 'FieldValues':
            print('Fields:')
            fields = stdict[stkey]
            for field, fieldvals in list(fields.items()):
                print(' --Field name: {0}'.format(field))
                print(' --Field default value: {0}'.format(fieldvals[0]))
                if not fieldvals[1] is None:
                    print(' --Domain name: {0}'.format(fieldvals[1].name))
        else:                    
            print('{0}: {1}'.format(stkey, stdict[stkey]))
