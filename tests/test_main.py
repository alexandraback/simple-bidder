import ulid
from simple_bidder.main import main
from simple_bidder.models.campaign import Campaign


# def test_main():
#     print(main())


def test_campaign_with_id():
    check_expect = {
        "name": "Alex Campaign",
        "keywords": ["awesome programmer", "goat programmer"],
        "id": "1234",
    }
    check = Campaign.parse_obj(check_expect)
    assert check == check_expect


def test_campaign_no_id():
    campaign = Campaign(
        name="Alex Campaign", keywords=["awesome programmer", "goat programmer"]
    )
    assert campaign.id is not None and len(campaign.id) == 26
