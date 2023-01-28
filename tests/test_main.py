from simple_bidder.models.campaign import CampaignResponse


def test_campaign_with_id():
    check_expect = {
        "name": "Alex Campaign",
        "keywords": ["awesome programmer", "goat programmer"],
        "id": "1234",
        "budget": 100,
        "spending": 0,
    }
    check = CampaignResponse.parse_obj(check_expect)
    assert check == check_expect


def test_campaign_no_id():
    campaign = CampaignResponse(
        name="Alex Campaign",
        keywords=["awesome programmer", "goat programmer"],
    )
    assert campaign.id is not None and len(campaign.id) == 26
