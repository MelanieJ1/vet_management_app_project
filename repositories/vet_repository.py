
from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, patient_list) VALUES (%s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.patient_list]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['patient_list'], row['id'])
        vets.append(vet)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    
    if results:
        result = results[0]
        vet = Vet(result['first_name'], result['last_name'], result['patient_list'], result['id'] )
    return vet


# def delete_all():
#     sql = "DELETE  FROM vets"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM vets WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(vet):
#     sql = "UPDATE vets SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [vet.first_name, vet.last_name, vet.patient_list, vet.id]
#     run_sql(sql, values)

