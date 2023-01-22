from simple_bidder.models.campaign import CampaignResponse


def find_matching_campaigns(campains: list[CampaignResponse], keywords: list[str]):
    ...


def update_budget_and_spending(campaign: CampaignResponse):
    campaign.budget -= 1
    campaign.spending += 1
