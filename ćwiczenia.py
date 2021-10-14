value = '[gt]666'

if value.startswith('[gt]'):
    value = value[4::]
    print(value)