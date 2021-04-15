
# Archive


#method 1

firstArchive = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3'
}

#method 2

secondArchive = {}

secondArchive['key4'] = 'value4'
secondArchive['key5'] = 'value5'
secondArchive['key6'] = 'value6'


# del secondArchive["key4"]

# firstArchive.pop('key1')

# print(firtArchive)

#Archive Loop

for key,value in firstArchive.items():
    print("I have " + key + " relating with " + value)