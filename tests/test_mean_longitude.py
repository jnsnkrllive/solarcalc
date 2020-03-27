from unittest import TestCase
from solarcalc import mean_longitude


class MeanLongitudeTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, 279.70462546632916),
        (0.00, 280.46646),
        (1.00, 281.23659320000297)
    ])

    def test_mean_longitude(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, mean_longitude(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_mean_longitude_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_mean_longitude_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            mean_longitude(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
