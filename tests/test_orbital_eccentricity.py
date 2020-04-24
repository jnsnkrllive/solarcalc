from unittest import TestCase
from solarcalc import orbital_eccentricity


class OrbitalEccentricityTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, 0.01675012645133),
        (0.00, 0.016708634),
        (1.00, 0.0166664703)
    ])

    def test_mean_anomaly(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, orbital_eccentricity(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_mean_anomaly_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_mean_anomaly_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            orbital_eccentricity(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
