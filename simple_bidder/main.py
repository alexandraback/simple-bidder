from fastapi import FastAPI
from pydantic import BaseModel
from simple_bidder.helper import update_budget_and_spending

from simple_bidder.models.campaign import Campaign, CampaignResponse


app = FastAPI()

campaigns = []


@app.get("/campaigns")
def read_root():
    return campaigns


@app.post("/campaign", response_model=CampaignResponse)
def create_campaign(campaign: Campaign):
    campaign_with_id = CampaignResponse(name=campaign.name, keywords=campaign.keywords)
    campaigns.append(campaign_with_id)
    return campaign_with_id.dict()


@app.get("/bid", response_model=list[CampaignResponse])
def bid_on_campaign():
    campaign = campaigns[0]
    update_budget_and_spending(campaign=campaign)
    return campaigns


# def main():
#     return "hello world!"
