from fastapi import FastAPI, Response
from pydantic import BaseModel
from simple_bidder.helper import update_budget_and_spending, load_campaigns
from simple_bidder.models.bid import Bid
from simple_bidder.helper import find_matching_campaigns, select_random_campaign


from simple_bidder.models.campaign import Campaign
from simple_bidder.models.response import CampaignResponse
import orjson

from starlette.responses import RedirectResponse

app = FastAPI()

campaigns = load_campaigns()


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


@app.post("/campaign")  # response_model=CampaignResponse,
def create_campaign(campaign: Campaign):
    campaign_with_id = CampaignResponse(name=campaign.name, keywords=campaign.keywords)
    with open("simple_bidder/campaigns.json", "wb") as f:
        try:
            campaigns.append(campaign_with_id)
            f.write(
                orjson.dumps(
                    [campaign.dict() for campaign in campaigns],
                    option=orjson.OPT_INDENT_2,
                )
            )
        except Exception as e:
            print(f"Oups: {e}")
            return Response(status_code=500)
    return Response(
        headers={"Location": f"campaign/{campaign_with_id.id}"}, status_code=201
    )


@app.post("/bid", response_model=CampaignResponse)
def bid_on_campaign(bid: Bid):
    matching_campaigns = find_matching_campaigns(
        campaigns=campaigns, keywords=bid.keywords
    )
    matching_campaign = select_random_campaign(matching_campaigns)[0]
    return matching_campaign.dict()


# def main():
#     return "hello world!"
