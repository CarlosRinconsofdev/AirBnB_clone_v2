import unittest
import pep8
from console import HBNBCommand
from unittest.mock import patch
import io


class ConsoleTests(unittest.TestCase):
    """Unittests"""

    def test_pep8(self):
        """Test that we conforms to PEP8"""
        p8style = pep8.StyleGuide()
        result = p8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_create(self):
        """Test for feature"""
        stdout = None
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="Antioquia"')
            stdout = f.getvalue()
            self.assertEqual(type(stdout), str)

if __name__ == "__main__":
    unittest.main()
