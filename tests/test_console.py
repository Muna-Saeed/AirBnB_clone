#!/usr/bin/env python3
""" test console """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import uuid


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        """ test quit """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("quit")
            output = mock_stdout.getvalue().strip()
            print(output)
            self.assertEqual(output, "")

    def test_show(self):
        """ test show """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            id = "2be367c9-69dd-4a68-abb3-ca9df61ba2b6"
            self.cmd.onecmd(f"User.show({id})")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(len(output), 239)

    def test_create(self):
        """ test create """
        expected = str(uuid.uuid4())
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create User")
            output = mock_stdout.getvalue().strip()
            uuid_obj = uuid.UUID(output)

    def test_help(self):
        """ test help """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, output)


if __name__ == "__main__":
    unittest.main()
