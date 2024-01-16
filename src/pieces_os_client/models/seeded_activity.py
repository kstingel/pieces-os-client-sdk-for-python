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
from pydantic import BaseModel, Field
from openapi_client.models.application import Application
from openapi_client.models.mechanism_enum import MechanismEnum
from openapi_client.models.referenced_asset import ReferencedAsset
from openapi_client.models.referenced_conversation import ReferencedConversation
from openapi_client.models.referenced_format import ReferencedFormat
from openapi_client.models.referenced_user import ReferencedUser
from openapi_client.models.seeded_connector_tracking import SeededConnectorTracking

class SeededActivity(BaseModel):
    """
    This is the preseed to a full blown Activity.  This is the minimum information needed to create an Activity, used within our [POST] /activities/create  if mechenism is not passed in we will default to AUTOMATIC  NOT required to pass in an asset/user/format.  # noqa: E501
    """
    event: SeededConnectorTracking = Field(...)
    application: Application = Field(...)
    asset: Optional[ReferencedAsset] = None
    user: Optional[ReferencedUser] = None
    format: Optional[ReferencedFormat] = None
    mechanism: Optional[MechanismEnum] = None
    conversation: Optional[ReferencedConversation] = None
    __properties = ["event", "application", "asset", "user", "format", "mechanism", "conversation"]

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
    def from_json(cls, json_str: str) -> SeededActivity:
        """Create an instance of SeededActivity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededActivity:
        """Create an instance of SeededActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededActivity.parse_obj(obj)

        _obj = SeededActivity.parse_obj({
            "event": SeededConnectorTracking.from_dict(obj.get("event")) if obj.get("event") is not None else None,
            "application": Application.from_dict(obj.get("application")) if obj.get("application") is not None else None,
            "asset": ReferencedAsset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "user": ReferencedUser.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "format": ReferencedFormat.from_dict(obj.get("format")) if obj.get("format") is not None else None,
            "mechanism": obj.get("mechanism"),
            "conversation": ReferencedConversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None
        })
        return _obj


