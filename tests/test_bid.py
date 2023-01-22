from simple_bidder.models.bid import Bid


def test_bid_with_id():
    check_expected = {"bid_id": "1234", "keywords": ["goat programmer"]}
    assert check_expected == Bid.parse_obj(check_expected).dict()
