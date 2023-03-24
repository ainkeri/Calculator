import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_alustus(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_lounaat_kateinen(self):
        edullinen = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(edullinen, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

        edullinen_epanega = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(edullinen_epanega, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_maukkaat_lounaat_kateinen(self):
        maukas = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(maukas, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        maukas_epanega = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(maukas_epanega, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_edulliset_lounaat_kortti(self):
        maksukortti = Maksukortti(300)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
        self.assertEqual(maksukortti.saldo, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_maukkaat_lounaat_kortti(self):
        maksukortti = Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_kortin_saldo_lataus(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 50)
        self.assertEqual(maksukortti.saldo, 150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100050)

        self.kassapaate.lataa_rahaa_kortille(maksukortti, -50)
        self.assertEqual(maksukortti.saldo, 150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100050)



