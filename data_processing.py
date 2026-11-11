import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_items(condition, dict_list):
    result = []
    for item in dict_list:
        if condition(item):
            result.append(item)
    return result


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = []
    for item in dict_list:
        values.append(item[aggregation_key])
    return aggregation_function(values)


for city in cities[:5]:
    print(city)

print("The average temperature of all the cities:")
print(aggregate('temperature',
                lambda t: sum(float(x) for x in t) / len(t),
                cities))
print()

for city in filter_items(lambda c: c['country'] == 'Germany', cities):
    print(city)

for city in filter_items(
        lambda c: c['country'] == 'Spain' and float(c['temperature']) > 12,
        cities):
    print(city)

print(aggregate('country', lambda c: len(set(c)), cities))

german_cities = filter_items(lambda c: c['country'] == 'Germany', cities)
print(aggregate('temperature',
                lambda t: sum(float(x) for x in t) / len(t),
                german_cities))

italian_cities = filter_items(lambda c: c['country'] == 'Italy', cities)
print(aggregate('temperature', lambda t: max(float(x) for x in t),
                italian_cities))
