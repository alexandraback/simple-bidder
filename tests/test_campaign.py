from simple_bidder.models.campaign import Campaign
from simple_bidder.helper import select_random_campaign


def test_bid_keyword_is_matching():
    campaign = Campaign(name="Alex Campaign", keywords=["goat", "programmer"])
    assert (campaign.is_matching(["ping", "programmer"])) == True


def test_bid_keyword_is_not_matching():
    campaign = Campaign(name="Alex Campaign", keywords=["goat", "programmer"])
    assert (campaign.is_matching(["ping", "data scientist"])) == False


def test_random():
    campaign = Campaign(name="Alex Campaign", keywords=["goat", "programmer"])
    campaign1 = Campaign(name="Alex Campaign2", keywords=["goat2", "programmer2"])
    campaign2 = Campaign(name="Alex Campaign3", keywords=["goat3", "programmer2"])
    l = [campaign, campaign1, campaign2]

    print(select_random_campaign(l))
    print(select_random_campaign(l))
    print(select_random_campaign(l))
