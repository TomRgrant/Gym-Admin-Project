DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;


CREATE TABLE members (
id SERIAL PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
membership VARCHAR(255)
);

CREATE TABLE gym_classes (
id SERIAL PRIMARY KEY,
class_description VARCHAR(255),
instructor VARCHAR(255),
date_time VARCHAR(255)
);

CREATE TABLE visits (
id SERIAL PRIMARY KEY,
meber_id INT REFERENCES members(id) ON DELETE CASCADE
gym_classes INT REFERENCES gym_classes(id) ON DELETE CASCADE
);
