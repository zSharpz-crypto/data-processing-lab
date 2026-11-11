import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

for city in cities[:5]:
    print(city)

print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

for city in cities:
    if city['country'] == 'Germany':
        print(city)

for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        print(city)


countries = set()
for city in cities:
    countries.add(city['country'])
print(len(countries))

german_temps = [float(city['temperature']) for city in cities if city['country'] == 'Germany']
print(sum(german_temps)/len(german_temps))

italy_temps = [float(city['temperature']) for city in cities if city['country'] == 'Italy']
print(max(italy_temps))
