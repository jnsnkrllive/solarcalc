from unittest import TestCase
from solarcalc import apparent_longitude


class ApparentLongitudeTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, 279.6506965833835),
        (0.00, 280.3725548788095),
        (1.00, 281.1152856538691)
    ])

    def test_apparent_longitude(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, apparent_longitude(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_apparent_longitude_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_apparent_longitude_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            apparent_longitude(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
