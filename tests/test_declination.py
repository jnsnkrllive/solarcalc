from unittest import TestCase
from solarcalc import declination


class DeclinationTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, -23.099604088288913),
        (0.00, -23.032515938065938),
        (1.00, -22.96387967236548)
    ])

    def test_declination(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, declination(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_declination_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_declination_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            declination(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
