import csv


def run():
    with open('static/DOTS.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for dot, cmps in reader:
            print(dot, cmps)


if __name__ == '__main__':
    run()
