"""
This file shows how you can create an alea unitest
"""
# The following imports are required
from obc_test_internals import obc_test, timeout

import numpy as np

"""
You want to inherit the Setup and Teardown of OBCTest so add it as the Parent Class.
Should you want to change the default SetUp or tearDown you can implement it here.
"""
class PingTest(obc_test.OBCTest):

    @timeout.timeout(5)
    def test_ping(self):
        resp = self.obc.ping()
        self.assertTrue(resp.is_success)

    @timeout.timeout(5)
    def test_hello(self):
        name = "Nicholas"
        message = "Hello Nicholas"
        """
        Name of command first and then arguments after
        """
        resp = self.obc.send_cmd("HELLO", name)
        
        self.assertTrue(resp.is_success)
        self.assertEqual(message, resp.data["message"])

"""
This section is required if you want to run these tests independently.
"""
if __name__ == '__main__':
    obc_test.main(PingTest)
