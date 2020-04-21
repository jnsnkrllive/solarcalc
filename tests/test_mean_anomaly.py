from unittest import TestCase
from solarcalc import mean_anomaly


class MeanAnomalyTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, -35281.530827741364),
        (0.00, 357.52911),
        (1.00, 36356.5792463)
    ])

    def test_mean_anomaly(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, mean_anomaly(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_mean_anomaly_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_mean_anomaly_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            mean_anomaly(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
