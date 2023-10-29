
------------------------------------- Tables
-- --------------------------
--          Users
-- --------------------------
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id                     TEXT NOT NULL UNIQUE, 
    user_email                  TEXT NOT NULL UNIQUE,
    user_username               TEXT NOT NULL UNIQUE,
    user_first_name             TEXT NOT NULL,
    user_last_name              TEXT NOT NULL,
    user_birthday               TEXT NOT NULL,
    user_password               TEXT NOT NULL,
    user_created_at             TEXT NOT NULL,
    user_active                 BOOLEAN DEFAULT 0,
    user_profilepic             TEXT,
    user_banner                 TEXT,
    user_total_followers        TEXT DEFAULT 0,
    user_total_following        TEXT DEFAULT 0,
    user_total_recipes          TEXT DEFAULT 0,
    user_total_collections      TEXT DEFAULT 0,
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
--    Recipe collections
-- --------------------------
DROP TABLE IF EXISTS collections;
CREATE TABLE collections (
    collection_id               TEXT NOT NULL UNIQUE,
    collection_user_fk          TEXT NOT NULL,
    collection_name             TEXT NOT NULL,
    collection_created_at       TEXT NOT NULL,
    collection_thumbnail        TEXT,
    PRIMARY KEY(collection_id)
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
--        Ingredients
-- --------------------------
DROP TABLE IF EXISTS ingredients;
CREATE TABLE ingredients (
    ingredient_id               TEXT NOT NULL UNIQUE,
    ingredient_recipe_fk        TEXT NOT NULL, -- fk
    ingredient_order            INTEGER NOT NULL, 
    ingredient_name             TEXT NOT NULL,
    PRIMARY KEY(ingredient_id)
) WITHOUT ROWID;


-- --------------------------
--    Recipe ingredients
-- --------------------------
DROP TABLE IF EXISTS steps;
CREATE TABLE steps (
    step_id                     TEXT NOT NULL UNIQUE,
    step_recipe_fk              TEXT NOT NULL, -- fk
    step_order                  INTEGER NOT NULL, 
    step_description            TEXT NOT NULL,
    PRIMARY KEY(step_id)
) WITHOUT ROWID;


-- --------------------------
--    Recipes in collections
-- --------------------------
DROP TABLE IF EXISTS recipes_in_collections;
CREATE TABLE recipes_in_collections (
    recipes_in_collections_recipe_fk            TEXT NOT NULL, -- fk
    recipes_in_collections_collection_fk        TEXT NOT NULL, -- fk
    recipes_in_collections_added_at             TEXT NOT NULL,
    PRIMARY KEY(recipes_in_collections_recipe_fk, recipes_in_collections_collection_fk)
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
INSERT INTO users VALUES("1", "maalmaja@gmail.com", "Kip", "Maja", "Larsen", "29-09-97", "123", "1698156869", "1", "user1.jpg", "banner1.jpg", 14, 18, 3, 3);
INSERT INTO users VALUES("2", "voli@hotmail.dk", "Vic", "Victor", "Larsen", "13-07-97", "123", "1698156870", "1", "unknown_user.jpg", "banner2.png", 11, 21, 3, 3);

-- Recipes
INSERT INTO recipes VALUES("1", "1", "Indisk dahl med nahn brød", "Dhal er en central ret i det indiske køkken. Retten er for det meste tilberedt af bælgfrugter, særligt linser, men til tider også Kikærter, bønner eller ærter.", "Gryderet", "1 time", "Nem", "0", "1698157635", "438921b73d6b454c82b164922947ffed.jpg");
INSERT INTO recipes VALUES("2", "1", "Klassisk lasagne", "Lasagne er en pastaret. Den mest kendte version er nok Lasagne Bolognese, der som navnet antyder, stammer fra byen Bologna i Norditalien.", "Pastaret", "2 timer", "Nem", "0", "1698157636", "5cde122617e64defa092321677a4be6a.jpg");
INSERT INTO recipes VALUES("3", "2", "Grønkålssalat med avocado", "Grønkålssalat er smuk, velsmagende og en af mine dejligste salater at servere i vintermånederne. Grønkål er så lækkert at bruge i køkkenet og jeg er vild den sprøde grønne farve sammen med de rubinrøde granatæble kerner.", "Salat", "30 minutter", "Nem", "0", "1698157638", "9f75b7d1d3054b72a5189d7bc3d9f684.jpg");
INSERT INTO recipes VALUES("4", "2", "Hjemmelavet Brød", "Dette hjemmelavede brød er luftigt og lækkert med en sprød skorpe. Perfekt til morgenmad eller som tilbehør til dine yndlingsretter.", "Brød", "2 timer", "Middel", "0", "1698157639", "pexels-kader-d-kahraman-15564188.jpg");
INSERT INTO recipes VALUES("5", "1", "Hjemmelavede Pandekager", "Disse pandekager er lette, fluffy og helt uimodståelige. Server dem med ahornsirup eller dit foretrukne fyld for en lækker morgenmad.", "Pandekager", "30 minutter", "Nem", "0", "1698157640", "pexels-nishant-aneja-2955819.jpg");
INSERT INTO recipes VALUES("6", "1", "Kyllingewraps med Tortillabrød", "Disse kyllingewraps er fyldt med saftig kylling, friske grøntsager og lækre tortillabrød. Perfekte til en hurtig og velsmagende frokost eller aftensmad.", "Wraps", "45 minutter", "Nem", "0", "1698157641", "pexels-wendy-wei-1656680.jpg");


-- Collections
INSERT INTO collections VALUES("1", "1", "Gryderetter", "1698157635", "438921b73d6b454c82b164922947ffed.jpg");
INSERT INTO collections VALUES("2", "1", "Ovnretter", "1698157636", "5cde122617e64defa092321677a4be6a.jpg");
INSERT INTO collections VALUES("3", "2", "Salater", "1698157638", "9f75b7d1d3054b72a5189d7bc3d9f684.jpg");


----------------------------------
-- Ingredienser
----------------------------------
-- Dahl
INSERT INTO ingredients VALUES("1", "1", 1, "1 kop røde linser");
INSERT INTO ingredients VALUES("2", "1", 2, "2 kopper vand");
INSERT INTO ingredients VALUES("3", "1", 3, "1 hakket løg");
INSERT INTO ingredients VALUES("4", "1", 4, "2 presset hvidløg");
INSERT INTO ingredients VALUES("5", "1", 5, "1 revet frisk ingefær");
INSERT INTO ingredients VALUES("6", "1", 6, "1 tsk spidskommen");
INSERT INTO ingredients VALUES("7", "1", 7, "1 tsk gurkemeje");
INSERT INTO ingredients VALUES("8", "1", 8, "1 tsk koriander");
INSERT INTO ingredients VALUES("9", "1", 9, "1/2 tsk kanel");
INSERT INTO ingredients VALUES("10", "1", 10, "1/2 tsk cayennepeber");
INSERT INTO ingredients VALUES("11", "1", 11, "2 hakket tomater");
INSERT INTO ingredients VALUES("12", "1", 12, "1 kokosmælk");
INSERT INTO ingredients VALUES("13", "1", 13, "Salt og peber efter smag");
INSERT INTO ingredients VALUES("15", "1", 14, "Frisk koriander efter smag");

-- Lasagne
INSERT INTO ingredients VALUES("16", "2", 1, "6 lasagneplader");
INSERT INTO ingredients VALUES("17", "2", 2, "500 g hakket oksekød");
INSERT INTO ingredients VALUES("18", "2", 3, "1 løg, hakket");
INSERT INTO ingredients VALUES("19", "2", 4, "2 fed hvidløg, presset eller hakket");
INSERT INTO ingredients VALUES("20", "2", 5, "2 fed hvidløg, presset eller hakket");
INSERT INTO ingredients VALUES("21", "2", 6, "200 gram revet mozzarella ost");
INSERT INTO ingredients VALUES("22", "2", 7, "Salt og peber efter smag");
INSERT INTO ingredients VALUES("23", "2", 8, "Olivenolie til stegning");
INSERT INTO ingredients VALUES("24", "2", 9, "Frisk basilikum eller persille til pynt");


-- Grønkålssalat
INSERT INTO ingredients VALUES ("25", "3", 1, "250 gram Grønkål");
INSERT INTO ingredients VALUES ("26", "3", 2, "2 stk Avocado");
INSERT INTO ingredients VALUES ("27", "3", 3, "1/4 kop Ekstra jomfru olivenolie");
INSERT INTO ingredients VALUES ("28", "3", 4, "Saft fra 1 citron Citronsaft");
INSERT INTO ingredients VALUES ("29", "3", 5, "Efter smag Salt og peber");

-- Brød
INSERT INTO ingredients VALUES("30", "4", 1, "Hvedemel (500 gram)");
INSERT INTO ingredients VALUES("31", "4", 2, "Vand (300 ml)");
INSERT INTO ingredients VALUES("32", "4", 3, "Salt (10 gram)");
INSERT INTO ingredients VALUES("33", "4", 4, "Gær (10 gram)");


-- Pandekager
INSERT INTO ingredients VALUES("34", "5", 1, "Hvedemel (200 gram)");
INSERT INTO ingredients VALUES("35", "5", 2, "Mælk (500 ml)");
INSERT INTO ingredients VALUES("36", "5", 3, "Æg (2 stk)");
INSERT INTO ingredients VALUES("37", "5", 4, "Sukker (2 spiseskeer)");
INSERT INTO ingredients VALUES("38", "5", 5, "Smør (2 spiseskeer)");


-- wraps
INSERT INTO ingredients VALUES("39", "6", 1, "Tortillapandekager (4 stk)");
INSERT INTO ingredients VALUES("40", "6", 2, "Kyllingebryst (2 stk)");
INSERT INTO ingredients VALUES("41", "6", 3, "Salatblade");
INSERT INTO ingredients VALUES("42", "6", 4, "Tomater (2 stk)");
INSERT INTO ingredients VALUES("43", "6", 5, "Agurk (1 stk)");



----------------------------------
-- Fremgangsmåde - steps
----------------------------------
INSERT INTO steps VALUES("1", "1", 1, "Skyl de røde linser grundigt og dræn dem.");
INSERT INTO steps VALUES("2", "1", 2, "I en stor gryde skal du opvarme lidt olie og sautere hakket løg indtil de bliver bløde og klare.");
INSERT INTO steps VALUES("3", "1", 3, "Tilsæt presset hvidløg og revet ingefær. Steg i et minut eller indtil det begynder at dufte.");
INSERT INTO steps VALUES("4", "1", 4, "Tilsæt spidskommen, gurkemeje, koriander, kanel og cayennepeber. Rør godt og steg krydderierne i et minut for at frigive deres aromaer.");
INSERT INTO steps VALUES("5", "1", 5, "Tilsæt de hakkede tomater og kog dem indtil de bliver bløde og saucy.");
INSERT INTO steps VALUES("6", "1", 6, "Tilsæt de skyllede røde linser og vand. Bring det hele i kog.");
INSERT INTO steps VALUES("7", "1", 7, "Reducer varmen, dæk gryden og lad det simre i ca. 20-25 minutter, eller indtil linserne er møre og konsistensen er tyk.");
INSERT INTO steps VALUES("8", "1", 8, "Tilsæt kokosmælk og rør godt. Varm det igennem.");
INSERT INTO steps VALUES("9", "1", 9, "Smag til med salt og peber, og juster krydderierne efter behov.");
INSERT INTO steps VALUES("10", "1", 10, "Server dahl'en varm, drysset med frisk koriander som pynt.");

----------------- Fremgangsmåde - steps
INSERT INTO steps VALUES("11", "2", 1, "Forvarm din ovn til 180°C (varmluft).");
INSERT INTO steps VALUES("12", "2", 2, "I en stor pande, opvarm en smule olivenolie over medium varme. Tilsæt hakket løg og hvidløg og steg dem indtil de er bløde og gennemsigtige.");
INSERT INTO steps VALUES("13", "2", 3, "Tilføj det hakkede oksekød til panden og steg det indtil det er brunet og gennemstegt. Sørg for at bryde kødet op i mindre stykker mens det steger.");
INSERT INTO steps VALUES("14", "2", 4, "Tilsæt de hakkede tomater, og lad det simre i 10-15 minutter, indtil saucen er tyknet. Smag til med salt og peber.");
INSERT INTO steps VALUES("15", "2", 5, "I et smurt 9x13 tommer oplagtage, læg et lag lasagneplader i bunden. Derefter tilføj et lag kødsauce og et lag mozzarella ost. Gentag processen, indtil ingredienserne er brugt op, og afslut med et lag mozzarella ost på toppen.");
INSERT INTO steps VALUES("16", "2", 6, "Dæk lasagnen med aluminiumsfolie og bag den i den forvarmede ovn i ca. 30 minutter.");
INSERT INTO steps VALUES("17", "2", 7, "Fjern folien og bag yderligere 10-15 minutter, indtil osten er gyldenbrun og boblende.");
INSERT INTO steps VALUES("18", "2", 8, "Lad lasagnen hvile i et par minutter før du skærer den i portioner. Pynt med frisk basilikum eller persille, og server den varm.");


-- Vask og skær grønkålen
INSERT INTO steps VALUES ("19", "3", 1, "Vask og skær grønkålen i tynde strimler.");
INSERT INTO steps VALUES ("20", "3", 2, "Skær avocadoerne i tern.");
INSERT INTO steps VALUES ("21", "3", 3, "I en stor skål, kombiner grønkål og avocado.");
INSERT INTO steps VALUES ("22", "3", 4, "Bland ekstra jomfru olivenolie og citronsaft i en skål og hæld det over salaten.");
INSERT INTO steps VALUES ("23", "3", 5, "Krydr med salt og peber efter smag.");
INSERT INTO steps VALUES ("24", "3", 6, "Bland godt, så dressing og ingredienser fordeler sig jævnt. Server salaten som en frisk og sund sideskål.");

-- brød
INSERT INTO steps VALUES("25", "4", 1, "Bland hvedemel og salt i en skål.");
INSERT INTO steps VALUES("26", "4", 2, "Opløs gær i vand og tilsæt blandingen til mel.");
INSERT INTO steps VALUES("27", "4", 3, "Ælt dejen indtil den er smidig.");
INSERT INTO steps VALUES("28", "4", 4, "Dæk dejen til og lad den hæve i 1 time.");
INSERT INTO steps VALUES("29", "4", 5, "Bag brødet i en forvarmet ovn ved 200°C i 30-40 minutter.");

-- pandekager
INSERT INTO steps VALUES("30", "5", 1, "Bland hvedemel og sukker i en skål.");
INSERT INTO steps VALUES("31", "5", 2, "Tilsæt mælk og æg og rør godt sammen.");
INSERT INTO steps VALUES("32", "5", 3, "Smelt smør og tilsæt det til dejen.");
INSERT INTO steps VALUES("33", "5", 4, "Opvarm en pande og steg pandekagerne indtil de er gyldenbrune på begge sider.");

-- wraps
INSERT INTO steps VALUES("34", "6", 1, "Steg kyllingebrystene indtil de er gennemstegte.");
INSERT INTO steps VALUES("35", "6", 2, "Skær kyllingebrystene i strimler.");
INSERT INTO steps VALUES("36", "6", 3, "Varm tortillapandekagerne i en tør pande.");
INSERT INTO steps VALUES("37", "6", 4, "Fordel salatblade, tomater, agurk og kylling på pandekagerne.");
INSERT INTO steps VALUES("38", "6", 5, "Rul pandekagerne sammen og server dem som wraps.");
