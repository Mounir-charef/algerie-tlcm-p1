import csv
from user.models import Cmp, Information
import datetime


def run(file_name):
    with open(f'static/{file_name}') as file:
        reader = csv.reader(file)
        # date = file_name.split('_')[1]
        date = datetime.date(2023, 6, 15)
        for row in list(reader):
            cmp_name, total, auto, binome, dhdb, ftth, la_ls, sans, total, qos, norme, objecif = row
            cmp = Cmp.objects.get(name=cmp_name.upper())
            if not Information.objects.filter(cmp=cmp, date=date):
                Information.objects.create(
                    cmp=cmp,
                    date=date,
                    total_raccordement_client=int(total),
                    auto=int(auto),
                    binome=int(binome),
                    dhdb=int(dhdb),
                    ftth=int(ftth),
                    la_ls=int(la_ls),
                    sans_specialite=int(sans),
                    total=int(total),
                    q_o_s=float(qos),
                    norme=float(norme),
                    objectif=float(objecif)
                )
