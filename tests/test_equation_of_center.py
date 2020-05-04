from unittest import TestCase
from solarcalc import equation_of_center


class EquationOfCenterTest(TestCase):

    # key: input, value: expected output
    testData = dict([
        (-0.99, -0.05237156942233544),
        (0.00, -0.08430148943719645),
        (1.00, -0.11637321218668388)
    ])

    def test_equation_of_center(self):
        self.verificationErrors = []
        for key, value in self.testData.items():
            self._performTest(key, value)
        self.assertEqual([], self.verificationErrors)

    def _performTest(self, input: float, expected_output: float) -> None:
        try:
            self.assertEqual(expected_output, equation_of_center(input))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_equation_of_center_badTimeLower(self):
        self._checkBadTime(-0.991)

    def test_equation_of_center_badTimeUpper(self):
        self._checkBadTime(1.001)

    def _checkBadTime(self, time: float):
        expectedMsg = "t must be beteween -0.99 and 1.00: " + str(time)
        with self.assertRaises(ValueError) as context:
            equation_of_center(time)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
