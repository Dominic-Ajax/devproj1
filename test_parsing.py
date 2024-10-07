import unittest
from parse_data import parse_json, parse_xml, parse_yaml

class TestParsingFunctions(unittest.TestCase):

    def test_parse_json(self):
        json_data = '{"name": "John", "age": 30}'
        self.assertEqual(parse_json(json_data), {"name": "John", "age": 30})

    def test_parse_xml(self):
        xml_data = '<person><name>John</name><age>30</age></person>'
        self.assertEqual(parse_xml(xml_data), {'person': {'name': 'John', 'age': '30'}})

    def test_parse_yaml(self):
        yaml_data = "name: John\nage: 30"
        self.assertEqual(parse_yaml(yaml_data), {"name": "John", "age": 30})

if __name__ == '__main__':
    unittest.main()
