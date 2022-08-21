
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  patient_list VARCHAR(255)
);

CREATE TABLE animals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  date_of_birth VARCHAR(255),
  animal_type VARCHAR(255),
  client_name VARCHAR(255),
  client_email VARCHAR(255),
  treatment_notes VARCHAR(255),
  vet_id INT NOT NULL REFERENCES vets(id)
);

