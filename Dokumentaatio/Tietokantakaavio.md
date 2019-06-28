Henkilö((pk) id:Integer, nimi:String, sähköposti:String)
Käyttäjätunnus((pk) id:Integer, (fk) henkilö_id -> Henkilö, nimi:String)
Resepti((pk) id:Integer, nimi:String, ohje:String)
Kategoria((pk) id:Integer, nimi:String)
Raaka-aine((pk) id:Integer, nimi:String)
KäyttäjäResepti((fk) käyttäjätunnus_id - > Käyttäjätunnus, (fk) resepti_id -> Resepti)
ReseptiKategoria((fk) resepti_id - > Resepti, (fk) kategoria_id -> Kategoria)
ReseptiRaaka-aine((fk) resepti_id - > Resepti, (fk) raaka-aine_id -> Raaka-aine)

![](/Kuvat/Tietokantakaavio.png)


CREATE TABLE account (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        username VARCHAR(30) NOT NULL,
        password VARCHAR(30) NOT NULL,
        PRIMARY KEY (id)
        
)


CREATE TABLE role (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
        
)


CREATE TABLE recipe (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(99) NOT NULL,
        instruction VARCHAR(200) NOT NULL,
        PRIMARY KEY (id)
        
)


CREATE TABLE ingredient (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(99) NOT NULL,
        PRIMARY KEY (id)
        
)


CREATE TABLE user_recipe (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        account_id INTEGER,
        recipe_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(recipe_id) REFERENCES recipe (id)
        
)


CREATE TABLE account_role (

        account_id INTEGER NOT NULL,
        role_id INTEGER NOT NULL,
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(role_id) REFERENCES role (id)
        
)


CREATE TABLE recipe_ingredient (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        recipe_id INTEGER,
        ingredient_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(recipe_id) REFERENCES recipe (id),
        FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
        
)


CREATE TABLE person (

        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(99) NOT NULL,
        email VARCHAR(99) NOT NULL,
        address VARCHAR(99) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
        
)
