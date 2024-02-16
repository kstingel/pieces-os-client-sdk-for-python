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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.model import Model
from typing import Optional, Set
from typing_extensions import Self

class FlattenedOCRAnalysis(BaseModel):
    """
    [DAG Safe] Ocr Analysis that will reference FlattenedFormats.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr
    raw: ReferencedFormat
    hocr: ReferencedFormat
    model: Model
    image: StrictStr = Field(description="this is a refernece to the image analysis.")
    __properties: ClassVar[List[str]] = ["schema", "id", "raw", "hocr", "model", "image"]

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
        """Create an instance of FlattenedOCRAnalysis from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of raw
        if self.raw:
            _dict['raw'] = self.raw.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hocr
        if self.hocr:
            _dict['hocr'] = self.hocr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlattenedOCRAnalysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "raw": ReferencedFormat.from_dict(obj["raw"]) if obj.get("raw") is not None else None,
            "hocr": ReferencedFormat.from_dict(obj["hocr"]) if obj.get("hocr") is not None else None,
            "model": Model.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "image": obj.get("image")
        })
        return _obj

from pieces_os_client.models.referenced_format import ReferencedFormat
# TODO: Rewrite to not use raise_errors
FlattenedOCRAnalysis.model_rebuild(raise_errors=False)

