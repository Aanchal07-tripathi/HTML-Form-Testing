
from html.parser import HTMLParser
import unittest


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.inputs = {}
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form" and attrs.get("id") == "registrationForm":
            self.form_found = True

        if tag == "input":
            field_id = attrs.get("id")
            if field_id:
                self.inputs[field_id] = attrs

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = FormParser()
        with open("index.html", encoding="utf-8") as file:
            parser.feed(file.read())
        cls.parser = parser

    def test_form_exists(self):
        self.assertTrue(self.parser.form_found)

    def test_name_field(self):
        self.assertIn("name", self.parser.inputs)
        self.assertEqual(self.parser.inputs["name"].get("type"), "text")
        self.assertIn("required", self.parser.inputs["name"])

    def test_email_field(self):
        self.assertIn("email", self.parser.inputs)
        self.assertEqual(self.parser.inputs["email"].get("type"), "email")
        self.assertIn("required", self.parser.inputs["email"])

    def test_contact_field(self):
        self.assertIn("contact", self.parser.inputs)
        self.assertEqual(self.parser.inputs["contact"].get("type"), "tel")
        self.assertIn("required", self.parser.inputs["contact"])

    def test_submit_button(self):
        self.assertTrue(self.parser.submit_found)


if __name__ == "__main__":
    unittest.main(verbosity=2)
