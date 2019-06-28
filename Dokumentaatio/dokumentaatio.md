Työni aiheena on tehdä sähköinen reseptitietokanta jonne käyttäjä voi kirjautua sisään omilla tunnuksilla, lisätä, muokata ja selata reseptejä, lisätä raaka-aineita ja selata saatavilla olevia raaka-aineita sekä lisätä ja muutta omia henkilötietoja. Käyttäjä näkee etusivulta kunkin käyttäjän reseptien määrän. Sovellus on suunniteltu kaikille käyttäjille jotka haluavat selata ja lukea reseptejä.
Sovellusta voi käyttää vain rekisterötyneet käyttäjät, vierailijat voivat vain nähdä etusivun sekä tiedon kuinka monta reseptiä kullakin käyttäjällä on. Käyttäjätunnusten luominen onnistuu sovelluksen kautta. Sovellusta voi käyttää osoitteessa https://tsoha-keitto-joonas.herokuapp.com.
Lopullinen työ on melko simppeli ulkoasultaan ja käyttö on mahdollisimman yksinkertaista sekä toimintoja on rajoitettu vain reseptien lisäämiseen, muokkaamiseen ja poistamiseen, raaka-aineiden lisäämiseen, niiden katseluun, reseptien selailuun sekä omien tietojen muokkaukseen. Teen ensimmäistä kertaa web-sovellusta joten pidän siksi tavoitteet melko vaatimattomina.

User story:

Käyttäjänä voin:

- lisätä omia reseptejä tietokantaan

      r = Recipe(form.name.data, form.instruction.data)
      r.account.append(current_user)
      for data in form.ingredients.data:
        ingredient = Ingredient.query.filter_by(name=data).first()
        r.ingredient.append(ingredient)
      db.session().add(r)
      db.session().commit())
      
- muokata omia reseptejä tietokantaan

      recipe.name = form.name.data
      recipe.instruction = form.instruction.data
      for data in form.ingredients.data:
        ingredient = Ingredient.query.filter_by(name=data).first()
        recipe.ingredient.append(ingredient)
      db.session().commit()
      
- poistaa omia reseptejä

      UserRecipe.query.filter_by(recipe_id=recipeid).delete()
      RecipeIngredient.query.filter_by(recipe_id=recipeid).delete()
      Recipe.query.filter_by(id=recipeid).delete()
      db.session().commit()

- selata kaikkia reseptejä 
  
         SELECT recipe.id, recipe.name, account.username, account.id
         FROM recipe, user_recipe, account
         WHERE recipe.id = user_recipe.recipe_id
         AND account.id = user_recipe.account_id
         ORDER BY recipe.id

- muokata omia tietojani

        info = Person(form.name.data, form.email.data, form.address.data)
        info.account_id = current_user.id
        db.session().add(info)
        
- luoda omat yhteystiedot

        info = Person(form.name.data, form.email.data, form.address.data)
        info.account_id = current_user.id
        db.session().add(info)
        db.session().commit()

- nähdä kaikkien käyttäjien resepti määrät

        SELECT account.username, COUNT (*) count
        FROM account, recipe, user_recipe
        WHERE account.id = user_recipe.account_id
        AND recipe.id = user_recipe.recipe_id
        GROUP BY account.id
        ORDER BY Count(*) DESC
        
- listä raaka-aineita

        ingredient = Ingredient(form.name.data)
        db.session().add(ingredient)
        db.session().commit()
        
- selata kaikkia raaka-aineita

        SELECT * FROM Ingredient
        
- katsoa reseptin ohjeita

        ohjeet:
        SELECT recipe.name, recipe.instruction
        FROM recipe
        WHERE recipe.id = {}.format(recipeid)
        
        reseptin raaka-aineet:
        SELECT ingredient.name
        FROM ingredient, recipe_ingredient
        WHERE recipe_ingredient.recipe_id = {}
        AND ingredient.id = recipe_ingredient.ingredient_id.format(recipeid)
        

Työn ja sovelluksen rajoitteet, puuttuvat ominaisuudet:

Tällähetkellä sovelluksessa ei ole admin käyttäjälle ominaisuuksia, mutta rooli on valmiina jatkokehitystä varten.
Jatkokehitys ideana voisi olla muiden käyttäjien selaamien ja reseptien tykkääminen, sekä kommentointi.
Sovellus toimii lokaalisti ongelmitta, mutta Herokussa se ei jostain syystä toimi. En löydä tälle syytä mistään.
