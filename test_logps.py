#!/usr/bin/env python

import unittest
import logps


class LogPsTestCase(unittest.TestCase):

    def test_command_ps(self):
        result = logps.process_list().read()
        assert "ps -ax" in result

    def test_find_pid(self):
        result = logps.find_pid("  123 ttys000    0:00.00 ps -ax")
        self.assertEquals(123, result)


if __name__ == "__main__":
    unittest.main()
