from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field


# Define schema for creating a website tools
class CreateWebsiteSchema(BaseModel):
    """Required Fields for Create a website over Liferay"""

    membershipType: str = Field(..., description="Membership type of the website It should be(open or private)")
    name: str = Field(..., description="Name of the website, (It should be string only")


class CreateUserSchemas(BaseModel):
    """ Required Fields for Create a user over Liferay"""

    alternateName: str = Field(..., description="Name of the user")
    emailAddress: str = Field(..., description="Email address of the user")
    familyName: str = Field(..., description="Family Name of the user")
    givenName: str = Field(..., description="Given Name of the user")


class GetUserListSchema(BaseModel):
    """
    Optional Fields for Get a user list over Liferay
    """
    page: int = 1  # Default value is 1
    pageSize: int = 20  # Default value is 10
    filter: Optional[str] = None
    search: Optional[str] = None
    sort: Optional[str] = None
