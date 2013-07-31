import sys

from models import *

if __name__ == "__main__":
    if len(School.objects) == 0:
        print "Nao existe nenhuma escola cadastrada. Importe os dados do ENEM primeiro."
    else:
        with open("./docs/escolas_cidade_sao_paulo.csv", "r") as file:
            for line in file:
                city_id, city_name, school_id, school_name = line.split(",")

                school = School.objects(code = school_id).first()

                if not school:
                    continue

                school.name = school_name
                school.save()
