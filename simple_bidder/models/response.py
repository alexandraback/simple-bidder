from pydantic import validator
import ulid
from simple_bidder.models.campaign import Campaign


class CampaignResponse(Campaign):
    id: str = None
    spending: int = 0

    @validator("id", always=True)
    def create_id(v: str | None):
        if v is not None:
            return v
        return ulid.new().str
