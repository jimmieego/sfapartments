from craigslist import CraigslistHousing
import csv


def getLat(loc):
    str = ","
    if loc == "None":
        return("")
    else:
        try:
            pos = loc.index(str)
        except ValueError:
            return("")
        return(loc[1: pos])


def getLong(loc):
    str1 = ","
    str2 = ")"
    if loc == "None":
        return("")
    else:
        try:
            pos1 = loc.index(str1)
            pos2 = loc.index(str2)
        except ValueError:
            return("")
        return(loc[pos1 + 2: pos2])


cl_h = CraigslistHousing(site='sfbay', area='sby', category='apa', filters={
                         'max_price': 3000, 'has_image': True, 'posted_today': True})


# for result in cl_h.get_results(sort_by='newest', geotagged=True):
#     print(type(result))

rowCount = 1
with open('sfapartments.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'url', 'datetime', 'price', 'where', 'has_image', 'has_map', 'geotag',
                  'lat', 'long', 'price_number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        loc = result['geotag']
        price = result['price']
        if loc is None:
            continue
        else:
            writer.writerow({'id': result['id'], 'name': result['name'],
                             'url': result['url'], 'datetime': result['datetime'], 'price': result['price'],
                             'where': result['where'], 'has_image': result['has_image'],
                             'has_map': result['has_map'], 'geotag': result['geotag'],
                             'lat': loc[0], 'long': loc[1], 'price_number': int(price[1:])})
            rowCount = rowCount + 1
            print(rowCount)
