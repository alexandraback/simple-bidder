from pydantic import BaseModel, validator
import ulid


class Campaign(BaseModel):
    name: str
    keywords: list[str]
    budget: int = 100
    # _id: str = None

    # class Config:
    #     underscore_attrs_are_private = True


class CampaignResponse(Campaign):
    id: str = None
    spending: int = 0

    @validator("id", always=True)
    def create_id(v: str | None):
        if v is not None:
            return v
        return ulid.new().str
