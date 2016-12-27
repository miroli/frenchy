import unittest
import frenchy


class CommunePropsTestCase(unittest.TestCase):
    def setUp(self):
        self.machy = frenchy.get('10212', year=2012)

    def test_commune_has_correct_region(self):
        self.assertEqual(self.machy.region, 'CHAMPAGNE-ARDENNE')

    def test_commune_has_correct_region_code(self):
        self.assertEqual(self.machy.region_code, 21)

    def test_commune_has_correct_department(self):
        self.assertEqual(self.machy.department, 'AUBE')

    def test_commune_has_correct_department_code(self):
        self.assertEqual(self.machy.department_code, '10')


class ResultsTestCase(unittest.TestCase):
    def setUp(self):
        self.locqueltas = frenchy.get('56120', year=2012)

    def test_joly_votes(self):
        joly = self.locqueltas.results.loc['Mme Eva JOLY'].iloc[0].values[0]
        self.assertEqual(joly, 25)
