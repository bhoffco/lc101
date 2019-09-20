CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(120),
    year INTEGER,
    director VARCHAR(120)
);

CREATE TABLE directors (
    director_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first VARCHAR(120),
    last VARCHAR(120),
    country VARCHAR(120)
);

DROP TABLE movies;

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(120),
    year INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

SELECT title FROM movies;

SELECT title FROM movies ORDER BY year DESC; 

INSERT INTO directors (first, last, country)
VALUES ('Jean-Pierre', 'Jeunet', 'France');

SELECT director_id
FROM directors 
WHERE first = 'Jean-Pierre' and last = 'Jeunet'

INSERT INTO movies (title, year, director_id)
VALUES ('Amelie', 2001, 2)

SELECT * FROM directors ORDER BY country

SELECT country FROM directors d
JOIN movies m on d.director_id = m.director_id
WHERE title = 'amelia'

SELECT m.title, d.last, d.first FROM movies m
join directors d on m.director_id = d.director_id
order by last