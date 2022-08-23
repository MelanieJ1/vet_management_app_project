
from db.run_sql import run_sql


from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository


def save(animal):
    sql = "INSERT INTO animals (name, date_of_birth, animal_type, client_name, client_email, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [animal.name, animal.date_of_birth, animal.type, animal.client_name, animal.client_email, animal.treatment_notes, animal.vet.id]
    results = run_sql(sql, values)[0]
    animal.id = results[0]
    return animal


def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        # vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['date_of_birth'], row['type'], row['client_name'], row['client_email'], row['treatment_notes'], row['id'] )
        animals.append(animal)
    return animals



def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

   
    if results:
        result = results[0]
        vet = vet_repository.select(result['vet.id'])
        animals = Animal(result['name'], result['date_of_birth'], result['type'], result['client_name'], result['client_email'], result['treatment_notes'], vet, result['id'] )
    return animal


def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, type, client_name, client_email, treatment_notes, author_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.type, animal. client_name, animal.client_email, animal.treatment_notes, animal.vet.id, animal.id]
    print(values)
    run_sql(sql, values)
