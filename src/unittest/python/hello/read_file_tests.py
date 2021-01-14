from unittest import TestCase
from hello.regex_assignment import pluralize


class Test(TestCase):

    def test_pluralize(self):
        assert pluralize('anomaly') == 'anomalies'
        assert pluralize('test') == 'tests'
