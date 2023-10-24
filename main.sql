
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id TEXT,
    name TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;

INSERT INTO users VALUES("1","Maja Ibs Larsen");