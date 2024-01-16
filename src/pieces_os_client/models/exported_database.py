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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema
from openapi_client.models.exported_database_formats import ExportedDatabaseFormats

class ExportedDatabase(BaseModel):
    """
    ExportedDatabase
    """
    analyses: conlist(StrictInt) = Field(...)
    applications: conlist(StrictInt) = Field(...)
    assets: conlist(StrictInt) = Field(...)
    code_analyses: conlist(StrictInt) = Field(..., alias="codeAnalyses")
    files: conlist(StrictInt) = Field(...)
    format_metrics: conlist(StrictInt) = Field(..., alias="formatMetrics")
    formats: conlist(StrictInt) = Field(...)
    fragments: conlist(StrictInt) = Field(...)
    image_analyses: conlist(StrictInt) = Field(..., alias="imageAnalyses")
    models: conlist(StrictInt) = Field(...)
    ocr_analyses: conlist(StrictInt) = Field(..., alias="ocrAnalyses")
    persons: conlist(StrictInt) = Field(...)
    sensitives: conlist(StrictInt) = Field(...)
    tags: conlist(StrictInt) = Field(...)
    websites: conlist(StrictInt) = Field(...)
    values: ExportedDatabaseFormats = Field(...)
    version: StrictStr = Field(..., description="This is the version of your os_server or cloud_server that we we exporting from.")
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    relationships: Optional[conlist(StrictInt)] = None
    activities: Optional[conlist(StrictInt)] = None
    annotations: Optional[conlist(StrictInt)] = None
    hints: Optional[conlist(StrictInt)] = None
    anchors: Optional[conlist(StrictInt)] = None
    anchor_points: Optional[conlist(StrictInt)] = Field(None, alias="anchorPoints")
    conversations: Optional[conlist(StrictInt)] = None
    conversation_messages: Optional[conlist(StrictInt)] = Field(None, alias="conversationMessages")
    message_values: Optional[ExportedDatabaseFormats] = Field(None, alias="messageValues")
    __properties = ["analyses", "applications", "assets", "codeAnalyses", "files", "formatMetrics", "formats", "fragments", "imageAnalyses", "models", "ocrAnalyses", "persons", "sensitives", "tags", "websites", "values", "version", "schema", "relationships", "activities", "annotations", "hints", "anchors", "anchorPoints", "conversations", "conversationMessages", "messageValues"]

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
    def from_json(cls, json_str: str) -> ExportedDatabase:
        """Create an instance of ExportedDatabase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of values
        if self.values:
            _dict['values'] = self.values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message_values
        if self.message_values:
            _dict['messageValues'] = self.message_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportedDatabase:
        """Create an instance of ExportedDatabase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportedDatabase.parse_obj(obj)

        _obj = ExportedDatabase.parse_obj({
            "analyses": obj.get("analyses"),
            "applications": obj.get("applications"),
            "assets": obj.get("assets"),
            "code_analyses": obj.get("codeAnalyses"),
            "files": obj.get("files"),
            "format_metrics": obj.get("formatMetrics"),
            "formats": obj.get("formats"),
            "fragments": obj.get("fragments"),
            "image_analyses": obj.get("imageAnalyses"),
            "models": obj.get("models"),
            "ocr_analyses": obj.get("ocrAnalyses"),
            "persons": obj.get("persons"),
            "sensitives": obj.get("sensitives"),
            "tags": obj.get("tags"),
            "websites": obj.get("websites"),
            "values": ExportedDatabaseFormats.from_dict(obj.get("values")) if obj.get("values") is not None else None,
            "version": obj.get("version"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "relationships": obj.get("relationships"),
            "activities": obj.get("activities"),
            "annotations": obj.get("annotations"),
            "hints": obj.get("hints"),
            "anchors": obj.get("anchors"),
            "anchor_points": obj.get("anchorPoints"),
            "conversations": obj.get("conversations"),
            "conversation_messages": obj.get("conversationMessages"),
            "message_values": ExportedDatabaseFormats.from_dict(obj.get("messageValues")) if obj.get("messageValues") is not None else None
        })
        return _obj


