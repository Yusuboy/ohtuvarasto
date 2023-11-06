import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)


    def test_oikea_merkkijono(self):
        self.varasto.lisaa_varastoon(5.0)

        mjono = "saldo = 5.0, vielä tilaa 5.0"


        self.assertEqual(str(self.varasto), mjono)

    def neg_varasto(self):
        varasto = Varasto(0.0)
        neg_varasto = Varasto(-1.0)

        self.assertAlmostEqual(varasto.tilavuus, 0.0)
        self.assertAlmostEqual(neg_varasto.tilavuus, 0.0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)


    def test_neg_muuttuu_nolla(self):
        varasto = Varasto(0.0, 0.0)
        neg_varasto = Varasto(-1.0, -1.0)

        self.assertAlmostEqual(varasto.saldo, 0.0)
        self.assertAlmostEqual(neg_varasto.saldo, 0.0)


    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)


    def test_neg_ei_muuta(self):
        self.varasto.lisaa_varastoon(-1.0)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    

    def test_täyteen_lisäys(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisätään_enemmän_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)


    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)


    def test_ei_voida_ottaa_negatiivinen_summa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(saatu_maara, 0)


    def test_jos_otetaan_enemmän_kuin_on_niin_tyhjentää(self):
        self.varasto.lisaa_varastoon(7)

        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 7)


    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def tyhjä_varasto(self):
      
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)
        self.assertAlmostEqual(varasto.saldo, 0.0)


    def neg_tilavuus_ja_summa(self):
        varasto = Varasto(-5, -10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)
        self.assertAlmostEqual(varasto.saldo, 0.0)


    def test_ottaminen_nolla_maara(self):

        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_initial_balance_less_than_or_equal_to_volume(self):
        varasto = Varasto(10, 8)
        self.assertAlmostEqual(varasto.tilavuus, 10)
        self.assertAlmostEqual(varasto.saldo, 8)

    def test_initial_balance_exceeds_volume(self):
        varasto = Varasto(10, 12)
        self.assertAlmostEqual(varasto.tilavuus, 10)
        self.assertAlmostEqual(varasto.saldo, 10)
