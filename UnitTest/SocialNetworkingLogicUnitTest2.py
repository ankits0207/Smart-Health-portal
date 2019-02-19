import unittest2
from BusinessLogic import SocialNetworkingLogic


class SocialNetworkingLogicUnitTest2(unittest2.TestCase):

    # Test for sending friend request
    def test_send_request(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().send_request('anksharm', 'arehani')
        SocialNetworkingLogic.SocialNetworkingLogic().send_request('anksharm', 'yuvi')
        self.assertTrue(response)

    # Negative test for invalid requester
    def test_send_request_negative_requester_not_present(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().send_request('invalid_requester', 'arehani')
        self.assertFalse(response)

    # Negative test for invalid requested user
    def test_send_request_negative_requested_user_not_present(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().send_request('anksharm', 'invalid_requested_user')
        self.assertFalse(response)

    # Test for accepting friend request
    def test_accept_request(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().accept_request('anksharm', 'arehani')
        self.assertTrue(response)

    # If the friend request does not exist
    def test_accept_request_negative(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().accept_request('arehani', 'yuvi')
        self.assertFalse(response)

    # Test for returning all friend requests for a particular user
    def test_return_friend_requests(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().return_my_friend_requests('yuvi')
        self.assertEqual('anksharm', response[0].requester_username)

    # Test for returning no data if any request is not present
    def test_return_friend_requests_no_data(self):
        response = SocialNetworkingLogic.SocialNetworkingLogic().return_my_friend_requests('loner')
        self.assertEqual(0, len(response))
if __name__ == '__main__':
    unittest2.main()
