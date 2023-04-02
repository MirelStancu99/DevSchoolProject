CREATE TABLE foods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    denumire text NOT NULL,
    calorii INTEGER,
    proteine INTEGER,
    gramaj INTEGER
);

INSERT INTO foods (denumire, calorii, proteine, gramaj)
VALUES
    ('Pui cu legume', 400, 25, 100),
    ('Somon la gratar', 300, 30, 100),
    ('Salata Caesar', 250, 10, 100),
    ('Omleta cu sunca si branza', 350, 20, 100),
    ('Chiftelute cu cartofi piure', 450, 15, 100),
    ('Pizza Margherita', 600, 20, 100),
    ('Tocana de legume cu pui', 350, 18, 100),
    ('Supa de rosii', 150, 5, 100),
    ('Burger cu cartofi prajiti', 800, 25, 100),
    ('Paine prajita cu avocado si oua', 300, 12, 100),
    ('Paine neprajita cu avocado si oua', 400, 12, 100);