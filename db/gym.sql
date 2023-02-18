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
title VARCHAR(255),
class_description VARCHAR(255),
instructor VARCHAR(255),
class_date VARCHAR(255)
);

CREATE TABLE visits (
id SERIAL PRIMARY KEY,
member_id INT REFERENCES members(id) ON DELETE CASCADE
gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);
