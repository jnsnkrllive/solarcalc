from unittest import TestCase
from solarcalc import obliquity_of_ecliptic


class ObliquityOfEclipticTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, 23.45087819366623),
        (0.00, 23.437821291789415),
        (1.00, 23.42881509177207)
    ])

    def test_obliquity_of_ecliptic(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, obliquity_of_ecliptic(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_obliquity_of_ecliptic_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_obliquity_of_ecliptic_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            obliquity_of_ecliptic(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
