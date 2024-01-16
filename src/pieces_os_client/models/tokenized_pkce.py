# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema

class TokenizedPKCE(BaseModel):
    """
    This is the flow that mobile apps use to access an API. Use this endpoint to exchange an Authorization Code for a Token.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    grant_type: StrictStr = Field(..., description="Denotes the flow you are using. For Authorization Code, use authorization_code or refresh_token.")
    client_id: StrictStr = Field(..., description="Your application's Client ID.")
    code: StrictStr = Field(..., description="The Authorization Code received from the initial /authorize call.")
    redirect_uri: StrictStr = Field(..., description="This is required only if it was set at the GET /authorize endpoint. The values must match.")
    code_verifier: StrictStr = Field(..., description="Cryptographically random key that was used to generate the code_challenge passed to /authorize.")
    audience: Optional[StrictStr] = Field(None, description="The audience domain: i.e. https://pieces.us.auth0.com")
    __properties = ["schema", "grant_type", "client_id", "code", "redirect_uri", "code_verifier", "audience"]

    @validator('grant_type')
    def grant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('refresh_token', 'authorization_code'):
            raise ValueError("must be one of enum values ('refresh_token', 'authorization_code')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TokenizedPKCE:
        """Create an instance of TokenizedPKCE from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TokenizedPKCE:
        """Create an instance of TokenizedPKCE from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TokenizedPKCE.parse_obj(obj)

        _obj = TokenizedPKCE.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "grant_type": obj.get("grant_type"),
            "client_id": obj.get("client_id"),
            "code": obj.get("code"),
            "redirect_uri": obj.get("redirect_uri"),
            "code_verifier": obj.get("code_verifier"),
            "audience": obj.get("audience")
        })
        return _obj


