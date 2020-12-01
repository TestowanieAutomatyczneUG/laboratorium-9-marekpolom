import unittest
from unittest.mock import *

import sample.car as car


class TestCar(unittest.TestCase):

    def test_fule(self):
        #mock
        test_object = car.Car()
        test_object.needsFule = Mock(name = 'needsFule')
        test_object.needsFule.return_value = False

        #test
        self.assertFalse(test_object.needsFule())

    def test_getEngineTemperature(self):
        #mock
        test_object = car.Car()
        test_object.getEngineTemperature = Mock(name = 'getEngineTemperature')
        test_object.getEngineTemperature.return_value = 80

        #test
        self.assertEqual(test_object.getEngineTemperature(), 80)

    def test_driveTo(self):
        dest = 'Miasto'

        #mock
        test_object = car.Car()
        test_object.driveTo = Mock(name = 'driveTo')
        test_object.driveTo.return_value = dest

        #test
        self.assertEqual(test_object.driveTo(dest), dest)


if __name__ == '__main__':
    unittest.main()
