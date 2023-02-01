import csv
from user.models import Dot


def run():
    with open('static/DOTS.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Dot.objects.all().delete()

        for dot, cmps in reader:
            print(dot, cmps)
            Dot.objects.create(name=dot)


if __name__ == '__main__':
    run()
