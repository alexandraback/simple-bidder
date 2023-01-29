from pydantic import BaseModel, validator
import ulid

from simple_bidder.models.bid import Bid


class Campaign(BaseModel):
    name: str
    keywords: list[str]
    budget: int = 100
    # _id: str = None

    # class Config:
    #     underscore_attrs_are_private = True

    def is_matching(self, bid_keywords: list[str]) -> bool:
        for keyword in bid_keywords:
            if keyword in self.keywords:
                return True
        return False
