import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0
print(sites[0])
print(sites_new[0])

# A dictionary-k value-jaihoz az alábbi módon lehet hozzáférni pl:

# sites[0]['size']

# for index in range(0, len(sites)):
#     print(sites[index]['size'], sites_new[index]['size'])

# 1.Feladat
print("---1. Feladat---")

for index in range(0, len(sites_new)):
    sum += sites_new[index]['size']

allWebSiteSize = round(sum / 1024, 2)
avgWebSiteSize = round(allWebSiteSize / len(sites_new), 2)
print("total size is: " + str(allWebSiteSize) + " Gb")
print("avg site size is: " + str(avgWebSiteSize) + " Gb")

# 2.Feladat
print("---2. Feladat---")
elojel = ""
for i in range(0, len(sites)):
    if (sites[i]['size'] != sites_new[i]['size']):
        kolonbseg = sites_new[i]['size'] - sites[i]['size']
        valtozas_arany = kolonbseg / (sites_new[i]['size'] / 100)
        if (valtozas_arany >= 0):
            elojel = "+"
        else:
            elojel = ""
        print(sites[i]['domain'] + " changed by: " + elojel +
              str(round(valtozas_arany, 2)) + " %")

# 3.Feladat
print("---3. Feladat---")
emptySitesCounter = 0
for indexTmp in range(0, len(sites_new)):
    if (sites_new[indexTmp]['size'] == 0):
        emptySitesCounter += 1
print("there are " + str(emptySitesCounter) + " empty sites")

# 4.Feladat
print("---4. Feladat---")
for iTmp in range(0, len(sites_new)):
    if (sites_new[iTmp]['size'] > 0):
        if (sites_new[iTmp]['size'] > 1024):
            print(sites_new[iTmp]['domain'] + " is: " +
                  str(round(sites_new[iTmp]['size'] / 1024, 2)) + " Gb")
        if (sites_new[iTmp]['size'] <= 1024):
            print(sites_new[iTmp]['domain'] + " is: " +
                  str(round(sites_new[iTmp]['size'], 2)) + " Mb")
