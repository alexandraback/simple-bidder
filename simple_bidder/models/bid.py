from pydantic import BaseModel, validator
import ulid


class Bid(BaseModel):
    bid_id: str = None
    keywords: list[str]

    @validator("bid_id", always=True)
    def create_bid_id(v: str | None):
        if v is None:
            return ulid.new().str
        return v
