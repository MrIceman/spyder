import unittest

from lib.config import Config
from lib.parser.kotlin.kotlin import KotlinParser
from model.component import Component


class KotlinParserTest(unittest.TestCase):

    def test_should_recognize_abstraction(self):
        parser = KotlinParser(Config(
            ".kt",
            [],
            [],
            []
        ))
        with open('./fixtures/ReportDataSource.kt', 'r') as file:
            code = file.read()
            result = parser.is_abstraction(code)

            self.assertTrue(result)
