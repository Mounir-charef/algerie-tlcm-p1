import csv
from user.models import Dot, Cmp


def run(file):
    with open(f'static/{file}') as file:
        reader = csv.reader(file)

        for row in list(reader):
            dot, *cmps = row
            dot, created = Dot.objects.get_or_create(
                defaults={
                    "name": dot.upper()
                },
                name=dot.upper()
            )
            for cmp in cmps:
                name = cmp.upper()
                if Cmp.objects.filter(name=name, dot=dot).exists():
                    continue

                Cmp.objects.create(name=name, dot=dot)
