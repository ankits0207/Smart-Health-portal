import unittest, BusinessLogic
from BusinessLogic import SocialNetworkingLogic

class SocialNetworkingLogicUnitTest(unittest.TestCase):

    def setUp(self):
        self.business_logic_obj = SocialNetworkingLogic.SocialNetworkingLogic()

    def test_decline_request(self):
        declined = self.business_logic_obj.decline_request('sups','abcd')
        self.assertTrue(declined)

    def test_decline_request_negative(self):
        declined = self.business_logic_obj.decline_request('abcd', 'arehani')
        self.assertFalse(declined)

    def test_unfriend(self):
        unfriend = self.business_logic_obj.unfirend('sups', 'abcd')
        self.assertTrue(unfriend)

    def test_unfriend_negative(self):
        unfirend = self.business_logic_obj.unfirend('abcd', 'arehani')
        self.assertFalse(unfirend)

    def test_unfriend_negative(self):
        my_friends = self.business_logic_obj.return_my_friends('abcd')
        for friend in my_friends:
            username = friend.username
            self.assertEqual('sups', username)
