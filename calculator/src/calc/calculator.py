class Calculator:
    """
    Luokka, joka pystyy suorittamaan yksinkertaisia laskutoimituksia.
    Attributes:
        number: nykyinen numero laskimessa
        calculation: laskutoimitus, jota suoritetaan
        result: laskutoimituksen vastaus
    """

    def __init__(self):
        """
        Luokan konstruktori, joka luo numeron, laskutoimituksen ja vastauksen.

        Args:
            number: nykyinen numero laskimessa
            calculation: laskutoimitus, jota suoritetaan
            result: laskutoimituksen vastaus
        """

        self.number = 0
        self.calculation = ""
        self.result = 0

    def add(self, num):
        """
        Lisää halutun numeron nykyiseen numeroon laskimessa.

        Args:
            num: nykyiseen numeroon lisättävä numero
        """

        self.result = self.number + num

    def substract(self, num):
        """
        Vähentää halutun numeron nykyisestä numerosta laskimessa.

        Args:
            num: nykyisestä numertosta vähennettävä numero
        """

        self.result = self.number - num

    def multiply(self, num):
        """
        Kertoo halutulla numerolla nykyisen numeron laskimessa.

        Args:
            num: numero, jolla kerrotaan nykyinen numero.
        """

        self.result = self.number * num

    def divide(self, num):
        """
        Jakaa nykyisen numeron halutulla numerolla. Jos numero on 0, jako ei onnistu ja tulee virheviesti.

        Args:
            num: numero, jolla jaetaan nykyinen numero.
        """

        if num != 0:
            self.result = self.number / num
        else:
            self.result = None
            print("Error: Cannot divide by zero")

    def clear(self):
        """
        Nollaa laskimen arvot.

        """

        self.number = 0
        self.calculation = ""
        self.result = 0

    def get_result(self):
        """
        Palauttaa laskimessa lasketun laskutoimituksen.

        Returns:
            self.result, joka kertoo laskimessa lasketun vastauksen.
        """

        return self.result
