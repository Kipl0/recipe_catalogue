
------------------------------------- Tables
-- --------------------------
--          Users
-- --------------------------
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id                     TEXT NOT NULL UNIQUE, 
    user_email                  TEXT NOT NULL UNIQUE,
    user_first_name             TEXT NOT NULL,
    user_last_name              TEXT NOT NULL,
    user_age                    TEXT NOT NULL,
    user_password               TEXT NOT NULL,
    user_created_at             TEXT NOT NULL,
    user_active                 BOOLEAN DEFAULT 0,
    user_profilepic             TEXT,
    user_banner                 TEXT,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;


-- --------------------------
--        Recipes
-- --------------------------
DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes (
    recipe_id                   TEXT NOT NULL UNIQUE,
    recipe_user_fk              TEXT NOT NULL, -- fk
    recipe_name                 TEXT NOT NULL,
    recipe_description          TEXT NOT NULL,
    recipe_category             TEXT NOT NULL,
    recipe_cooking_est          TEXT NOT NULL,
    recipe_difficulty           TEXT NOT NULL,
    recipe_total_likes          INTEGER DEFAULT 0,
    recipe_created_at           TEXT,
    recipe_thumbnail            TEXT,
    PRIMARY KEY(recipe_id)
) WITHOUT ROWID;


-- --------------------------
--        Ingredients
-- --------------------------
DROP TABLE IF EXISTS ingredients;
CREATE TABLE ingredients (
    ingredient_id               TEXT NOT NULL UNIQUE,
    ingredient_recipe_fk        TEXT NOT NULL, -- fk
    ingredient_name             TEXT NOT NULL,
    PRIMARY KEY(ingredient_id)
) WITHOUT ROWID;


-- --------------------------
--       User recipe
-- --------------------------
DROP TABLE IF EXISTS user_recipes;
CREATE TABLE user_recipes (
    user_recipe_user_fk             TEXT NOT NULL, -- fk
    user_recipe_recipe_fk           TEXT NOT NULL UNIQUE, -- fk
    PRIMARY KEY(user_recipe_user_fk, user_recipe_recipe_fk)
) WITHOUT ROWID;


-- --------------------------
--    Recipe ingredients
-- --------------------------
DROP TABLE IF EXISTS recipe_ingredients;
CREATE TABLE recipe_ingredients (
    recipe_ingredient_recipe_fk                 TEXT NOT NULL, -- fk
    recipe_ingredient_ingredient_fk             TEXT NOT NULL, -- fk
    recipe_ingredient_ingredient_amount         TEXT NOT NULL,
    PRIMARY KEY(recipe_ingredient_recipe_fk, recipe_ingredient_ingredient_fk)
) WITHOUT ROWID;


-- --------------------------
--    Recipes_liked_by_users
-- --------------------------
DROP TABLE IF EXISTS Recipes_liked_by_users;
CREATE TABLE Recipes_liked_by_users (
    Recipes_liked_by_users_user_fk              TEXT NOT NULL,
    Recipes_liked_by_users_recipe_fk            TEXT NOT NULL,
    PRIMARY KEY(Recipes_liked_by_users_user_fk, Recipes_liked_by_users_recipe_fk)
) WITHOUT ROWID;



------------------------------------- Inserts
-- Users
INSERT INTO users VALUES("1", "maalmaja@gmail.com", "Maja", "Larsen", "26", "123", "1698156869", "1", "unknown_user.jpg", "");
INSERT INTO users VALUES("2", "voli@hotmail.dk", "Victor", "Larsen", "26", "123", "1698156870", "1", "unknown_user.jpg", "");

-- Recipes
INSERT INTO recipes VALUES("1", "1", "Dahl", "Dhal er en central ret i det indiske køkken. Retten er for det meste tilberedt af bælgfrugter, særligt linser, men til tider også Kikærter, bønner eller ærter.", "Gryderet", "1 time", "Nem", "0", "1698157635", "438921b73d6b454c82b164922947ffed.jpg");
INSERT INTO recipes VALUES("2", "1", "Lasagne", "Lasagne er en pastaret. Den mest kendte version er nok Lasagne Bolognese, der som navnet antyder, stammer fra byen Bologna i Norditalien.", "Pastaret", "2 timer", "Nem", "0", "1698157636", "5cde122617e64defa092321677a4be6a.jpg");
INSERT INTO recipes VALUES("3", "2", "Grønkålssalat", "Grønkålssalat er smuk, velsmagende og en af mine dejligste salater at servere i vintermånederne. Grønkål er så lækkert at bruge i køkkenet og jeg er vild den sprøde grønne farve sammen med de rubinrøde granatæble kerner.", "Salat", "30 minutter", "Nem", "0", "1698157638", "9f75b7d1d3054b72a5189d7bc3d9f684.jpg");
