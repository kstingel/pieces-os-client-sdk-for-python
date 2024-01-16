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
from pydantic import BaseModel, Field, StrictInt
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema
from openapi_client.models.seeded_connector_creation import SeededConnectorCreation

class SuggestionTarget(BaseModel):
    """
    This is the target that was sent to pieces. This will return the string that represents this coppied || pasted asset. This will also send along the SeededConnectorCreation and will send along the vector that we created based on the seed.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    seed: SeededConnectorCreation = Field(...)
    vector: StrictInt = Field(..., description="This is the vector representation of this target that we generated.")
    __properties = ["schema", "seed", "vector"]

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
    def from_json(cls, json_str: str) -> SuggestionTarget:
        """Create an instance of SuggestionTarget from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of seed
        if self.seed:
            _dict['seed'] = self.seed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SuggestionTarget:
        """Create an instance of SuggestionTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SuggestionTarget.parse_obj(obj)

        _obj = SuggestionTarget.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "seed": SeededConnectorCreation.from_dict(obj.get("seed")) if obj.get("seed") is not None else None,
            "vector": obj.get("vector")
        })
        return _obj


