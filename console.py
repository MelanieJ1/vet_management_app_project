
import pdb
from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

# animal_repository.delete_all()
# vet_repository.delete_all()

vet1 = Vet("James", "Anderson", "Bella and Mario")
vet_repository.save(vet1)
vet2 = Vet("Sarah", "Miller", "Max and Daisy")
vet_repository.save(vet2)

vet_repository.select_all()



animal_1 = Animal("Bella", "21/1/2021", "Dog", "James Smith", "j.smith@net.com", vet1)
animal_repository.save(animal_1)

animal_2 = Animal("Mario", "5/5/2018", "Cat", "Nicola James", "n.james@net.com", vet1)
animal_repository.save(animal_2)

animal_3 = Animal("Max", "21/6/2019", "Dog", "Stewart Wright", "s.wright@net.com", vet2)
animal_repository.save(animal_3)

animal_4 = Animal("Daisy", "9/9/2020", "Rabbit", "John Williams", "j.williams@net.com", vet2)
animal_repository.save(animal_2)

pdb.set_trace()




