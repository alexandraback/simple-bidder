import orjson
from simple_bidder.models.response import CampaignResponse
import random


def load_campaigns():
    with open("simple_bidder/campaigns.json") as f:
        campaigns = orjson.loads(f.read())
        return [CampaignResponse.parse_obj(campaign) for campaign in campaigns]


def find_matching_campaigns(campaigns: list[CampaignResponse], keywords: list[str]):
    matches = []
    for campaign in campaigns:
        if campaign.is_matching(keywords):
            matches.append(campaign)
    return matches


def select_random_campaign(campaigns: list[CampaignResponse]):
    return random.choices(population=campaigns)


def update_budget_and_spending(campaign: CampaignResponse):
    campaign.budget -= 1
    campaign.spending += 1
