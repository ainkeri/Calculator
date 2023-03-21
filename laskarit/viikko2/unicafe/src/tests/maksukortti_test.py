import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_maksukortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_maksukortti_ei_mene_miinukselle(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

