
-- Create Database countries_db
CREATE DATABASE IF NOT EXISTS countries_db;
USE countries_db;

--Create a table called countries
CREATE TABLE countries (
    ID INT AUTO_INCREMENT,
    country VARCHAR(50) NOT NULL,
    capital VARCHAR(50) NOT NULL,
    continent VARCHAR(50) NOT NULL,
    currency VARCHAR(25) NOT NULL,
    PRIMARY KEY (ID)
);

-- Create initial table contents
INSERT INTO countries (country, capital, continent, currency) VALUES
    ('Spain', 'Madrid', 'Europe', 'Euro'),
    ('Italy', 'Rome', 'Europe', 'Euro'),
    ('United Kingdom', 'London', 'Europe', 'Pound'),
    ('United States', 'Washington D.C.', 'North America', 'Dollar'),
    ('Argentina', 'Buenos Aires', 'South America', 'Argentine Peso'),
    ('Nigeria', 'Abuja', 'Africa', 'Naira');
