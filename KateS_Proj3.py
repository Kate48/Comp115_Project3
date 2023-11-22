f = open('BC census 2016 data.csv', 'r')
lines = f.readlines()

# split into a list - goal is to produce a list of areas w/ shelt_rent_30plus_rate > 50
chsa_30plus_list = []
for line in lines[1:]:
    line = line.split(",")
    shelt_rent_30plus_rate = line[5]
    print(shelt_rent_30plus_rate)

