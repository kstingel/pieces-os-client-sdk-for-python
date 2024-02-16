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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.application import Application
from pieces_os_client.models.conversation_type_enum import ConversationTypeEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.qgpt_prompt_pipeline import QGPTPromptPipeline
from pieces_os_client.models.referenced_model import ReferencedModel
from pieces_os_client.models.seeded_anchor import SeededAnchor
from pieces_os_client.models.seeded_annotation import SeededAnnotation
from pieces_os_client.models.seeded_conversation_message import SeededConversationMessage
from typing import Optional, Set
from typing_extensions import Self

class SeededConversation(BaseModel):
    """
    This is a pre-Conversation object.  This will hold together a conversation. Ie allthe message within a conversation.  All the additional properties on here used on here like(anchors/assets) are used for context that will seed the conversation.  model is a calculated property, and will be the model of the last message sent if applicable.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    name: Optional[StrictStr] = Field(default=None, description="This is a name that is customized.")
    favorited: Optional[StrictBool] = None
    application: Optional[Application] = None
    annotations: Optional[List[SeededAnnotation]] = None
    messages: Optional[List[SeededConversationMessage]] = None
    model: Optional[ReferencedModel] = None
    assets: Optional[FlattenedAssets] = None
    websites: Optional[FlattenedWebsites] = None
    anchors: Optional[List[SeededAnchor]] = None
    type: ConversationTypeEnum
    pipeline: Optional[QGPTPromptPipeline] = None
    demo: Optional[StrictBool] = Field(default=None, description="This will let us know if this conversation was generated as a 'demo' conversation")
    __properties: ClassVar[List[str]] = ["schema", "name", "favorited", "application", "annotations", "messages", "model", "assets", "websites", "anchors", "type", "pipeline", "demo"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SeededConversation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in anchors (list)
        _items = []
        if self.anchors:
            for _item in self.anchors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['anchors'] = _items
        # override the default output from pydantic by calling `to_dict()` of pipeline
        if self.pipeline:
            _dict['pipeline'] = self.pipeline.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededConversation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "name": obj.get("name"),
            "favorited": obj.get("favorited"),
            "application": Application.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "annotations": [SeededAnnotation.from_dict(_item) for _item in obj["annotations"]] if obj.get("annotations") is not None else None,
            "messages": [SeededConversationMessage.from_dict(_item) for _item in obj["messages"]] if obj.get("messages") is not None else None,
            "model": ReferencedModel.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "assets": FlattenedAssets.from_dict(obj["assets"]) if obj.get("assets") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj["websites"]) if obj.get("websites") is not None else None,
            "anchors": [SeededAnchor.from_dict(_item) for _item in obj["anchors"]] if obj.get("anchors") is not None else None,
            "type": obj.get("type"),
            "pipeline": QGPTPromptPipeline.from_dict(obj["pipeline"]) if obj.get("pipeline") is not None else None,
            "demo": obj.get("demo")
        })
        return _obj


