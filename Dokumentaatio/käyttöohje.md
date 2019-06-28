Sovellusta pääset käyttämään osoitteessa: https://tsoha-keitto-joonas.herokuapp.com (Kaikki osat ei toimi enkä tiedä miksi)

Ohjeet:
0) etusivulla näet kaikkien käyttäjien respetien määrän laskevassa järjestyksessä
1) mikäli sinulla ei ole käyttäjätunnuksia. Tee sellaiset painamalla oikeassa yläkulmassa olevaa nappia "register". Täytä vaaditut kentät.
1.1) jos sinulla on tunnukset klikkaa "login" painiketta
2) kirjaudut sovellukseen sisään
3) Sovelluksen yläpalkissa on erinäisä painikkeita jotak päästävät käyttäjän sovelluksen eri ominaisuuksiin
4) Home välilehti on sovelluksen etu-sivu
  - Add recepistä voit lisätä uuden reseptin mikäli olet kirjautunut sisään
  - List recepistä näet kaikki sovellukseen lisäty reseptit ja niiden tekijät
    - klikkaamalla reseptin nimeä pääset reseptin ohjeisiin
  - Add ingredientstä voit lisätä uuden raaka-aineen sovelluksen tietokantaan
  - List ingredientistä näet kaikki sovelluksessa olevat raaka-aineet
  - my informationsta pääset muokkaamaan omia yhteystietoja (tämä on näkyvissä vain jos on kirjautunut sisään)
  - jos olet kirautunut sisään ja haluat kirjautua ulos niin näin voi tehdä painamalla sovelluksen oikealta yläkulmasta linkkiä "LOGOUT"
  
  
Sovelluksen lataaminen omalle koneelle:

- Sinulla tulee olla ladattuna Python ja Pip
- Kloonaa respositori gitistä. Mene sovelluksen juuri hakemistoon ja aja komento : git clone https://github.com/JaykobJ/TsohaKeittoJoonas.git
- Lataa vaatimukset pip install -r /path/to/requirements.txt
- Luo ja aktivoi virtuaali ympäristö: venv/bin/activate
- Aja sovellus: python3 run.py
- Mene selaimellasi komentorivin ohjeistamaan localhost:5000
