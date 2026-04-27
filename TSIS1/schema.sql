CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(20)
);
