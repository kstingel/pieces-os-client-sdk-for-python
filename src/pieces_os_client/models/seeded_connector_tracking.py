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
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.seeded_tracked_adoption_event import SeededTrackedAdoptionEvent
from pieces_os_client.models.seeded_tracked_interaction_event import SeededTrackedInteractionEvent
from pieces_os_client.models.seeded_tracked_keyboard_event import SeededTrackedKeyboardEvent
from pieces_os_client.models.seeded_tracked_machine_learning_event import SeededTrackedMachineLearningEvent
from pieces_os_client.models.seeded_tracked_session_event import SeededTrackedSessionEvent

class SeededConnectorTracking(BaseModel):
    """
    This model is designed to be light weight and low friction while most of the heavy lifting will be happening inside of the context servers.  This Model is important because this has references to our materials, instead of fully referenced materials.(very similar to our SeededTrackedEvent, consider consolidating and converting these to Referenced models instead of ID's)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    format: Optional[SeededTrackedFormatEvent] = None
    asset: Optional[SeededTrackedAssetEvent] = None
    interaction: Optional[SeededTrackedInteractionEvent] = None
    keyboard: Optional[SeededTrackedKeyboardEvent] = None
    session: Optional[SeededTrackedSessionEvent] = None
    assets: Optional[SeededTrackedAssetsEvent] = None
    ml: Optional[SeededTrackedMachineLearningEvent] = None
    adoption: Optional[SeededTrackedAdoptionEvent] = None
    conversation: Optional[SeededTrackedConversationEvent] = None
    __properties = ["schema", "format", "asset", "interaction", "keyboard", "session", "assets", "ml", "adoption", "conversation"]

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
    def from_json(cls, json_str: str) -> SeededConnectorTracking:
        """Create an instance of SeededConnectorTracking from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interaction
        if self.interaction:
            _dict['interaction'] = self.interaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyboard
        if self.keyboard:
            _dict['keyboard'] = self.keyboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ml
        if self.ml:
            _dict['ml'] = self.ml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of adoption
        if self.adoption:
            _dict['adoption'] = self.adoption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededConnectorTracking:
        """Create an instance of SeededConnectorTracking from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededConnectorTracking.parse_obj(obj)

        _obj = SeededConnectorTracking.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "format": SeededTrackedFormatEvent.from_dict(obj.get("format")) if obj.get("format") is not None else None,
            "asset": SeededTrackedAssetEvent.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "interaction": SeededTrackedInteractionEvent.from_dict(obj.get("interaction")) if obj.get("interaction") is not None else None,
            "keyboard": SeededTrackedKeyboardEvent.from_dict(obj.get("keyboard")) if obj.get("keyboard") is not None else None,
            "session": SeededTrackedSessionEvent.from_dict(obj.get("session")) if obj.get("session") is not None else None,
            "assets": SeededTrackedAssetsEvent.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "ml": SeededTrackedMachineLearningEvent.from_dict(obj.get("ml")) if obj.get("ml") is not None else None,
            "adoption": SeededTrackedAdoptionEvent.from_dict(obj.get("adoption")) if obj.get("adoption") is not None else None,
            "conversation": SeededTrackedConversationEvent.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None
        })
        return _obj

from pieces_os_client.models.seeded_tracked_asset_event import SeededTrackedAssetEvent
from pieces_os_client.models.seeded_tracked_assets_event import SeededTrackedAssetsEvent
from pieces_os_client.models.seeded_tracked_conversation_event import SeededTrackedConversationEvent
from pieces_os_client.models.seeded_tracked_format_event import SeededTrackedFormatEvent
SeededConnectorTracking.update_forward_refs()
