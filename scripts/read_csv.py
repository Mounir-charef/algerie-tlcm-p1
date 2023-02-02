import csv
from user.models import Dot, Cmp


def run(file):
    with open(f'static/{file}') as file:
        reader = csv.reader(file)

        Dot.objects.all().delete()
        Cmp.objects.all().delete()

        for row in list(reader):
            dot, *cmps = row
            print(dot, cmps)
            temp = Dot.objects.create(name=dot.upper())
            for cmp in cmps:
                Cmp.objects.create(dot=temp, name=cmp.upper())

