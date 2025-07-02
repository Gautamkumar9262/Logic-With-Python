#write a python script bto create a dict object from a list of city names in such a way the alphabets are keys of the dictionary and list of the city names starting from that alphabet will be its data value.
cities =[
    "bhopal",
    "patna",
    "jaipur",
    "pune",
    "kanpur",
    "panjab",
    "bikaner",
    "japan"
]
d={}
for alpha in "abcdefghijklmnopqrstuvwxyz":
    names=[]
    for city in cities:
        if city.startswith(alpha):
            names.append(city)
    if len(names)>0:
     d[alpha] = names
for k,v in d.items():
    print(k,v)