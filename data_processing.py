import csv, os


class DataLoader:
    def __init__(self, base_path=None):
        self.base_path = base_path or os.path.dirname(os.path.abspath(__file__))

    def load_csv(self, filename):
        with open(os.path.join(self.base_path, filename)) as f:
            rows = [dict(r) for r in csv.DictReader(f)]
        return Table(filename, rows)


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        return iter(self.table)

    def __getitem__(self, index):
        return self.table[index]

    def __str__(self):
        return f"Table({self.table_name}, {len(self.table)} rows)"

    def filter(self, condition):
        result = []
        for item in self.table:
            if condition(item):
                result.append(item)
        return Table(self.table_name, result)

    def aggregate(self, aggregation_key, aggregation_function):
        values = []
        for item in self.table:
            values.append(item[aggregation_key])
        return aggregation_function(values)

    def to_list(self):
        return list(self.table)


def mean(values):
    nums = [float(v) for v in values]
    return sum(nums) / len(nums)


def maximum(values):
    return max(float(v) for v in values)


loader = DataLoader()
cities = loader.load_csv('Cities.csv')

for city in cities[:5]:
    print(city)

print("The average temperature of all the cities:")
print(cities.aggregate('temperature', mean))
print()

for city in cities.filter(lambda c: c['country'] == 'Germany'):
    print(city)

for city in cities.filter(
        lambda c: c['country'] == 'Spain' and float(c['temperature']) > 12):
    print(city)

print(cities.aggregate('country', lambda c: len(set(c))))

german_cities = cities.filter(lambda c: c['country'] == 'Germany')
print(german_cities.aggregate('temperature', mean))

italian_cities = cities.filter(lambda c: c['country'] == 'Italy')
print(italian_cities.aggregate('temperature', maximum))
