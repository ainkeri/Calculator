# Testausdokumentti

Ohjelman testaus testaa vain sovelluslogiikkaa, eikä käyttöliittymää. Syynä on, että en osannut testata käyttöliittymää. Eli testaus on suppea.

## Sovelluslogiikka

`Calculator`-luokkaa, joka vastaa laskimen sovelluslogiikasta, testataan [TestCalculator](https://github.com/ainkeri/Calculator/blob/9764731b796d57addeb4df23f99f9f1f46d76f92/calculator/src/tests/calculator_test.py)-testiluokan avulla. `TestCalculator` alustaa testauksessaan calculatorin, ja testaa eri funktioiden avulla toimiiko `Calculator`. Näitä ovat esimerkiksi eri laskutoimitukset, nollalla jakaminen, laskukentän tyhjentäminen ja vastauksen saaminen.

## Testikattavuus

Testikattavuus on vain 27%, koska käyttöliittymän testaus on 0%.
![image](https://github.com/ainkeri/Calculator/assets/114941561/f6882b61-96fd-4e9e-bcba-97c3367e4ffb)
