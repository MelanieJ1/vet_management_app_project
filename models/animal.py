
class Animal:

    def __init__(self, name, date_of_birth, type, client_name, client_email, treatment_notes, vet, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type = type
        self.client_name = client_name
        self.client_email = client_email
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.id = id
