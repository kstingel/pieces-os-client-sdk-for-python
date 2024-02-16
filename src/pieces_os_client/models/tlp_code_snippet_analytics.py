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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.tlp_code_fragment_classification import TLPCodeFragmentClassification
from pieces_os_client.models.tlp_code_fragment_description import TLPCodeFragmentDescription
from pieces_os_client.models.tlp_code_fragment_reclassification import TLPCodeFragmentReclassification
from pieces_os_client.models.tlp_code_fragment_statistics import TLPCodeFragmentStatistics
from pieces_os_client.models.tlp_code_fragment_tagify import TLPCodeFragmentTagify
from pieces_os_client.models.tlp_code_snippet_suggested_interactions import TLPCodeSnippetSuggestedInteractions
from typing import Optional, Set
from typing_extensions import Self

class TLPCodeSnippetAnalytics(BaseModel):
    """
    TLPCodeSnippetAnalytics
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    statistics: Optional[TLPCodeFragmentStatistics] = None
    classification: Optional[TLPCodeFragmentClassification] = None
    reclassification: Optional[TLPCodeFragmentReclassification] = None
    suggested: Optional[TLPCodeSnippetSuggestedInteractions] = None
    tagify: Optional[TLPCodeFragmentTagify] = None
    description: Optional[TLPCodeFragmentDescription] = None
    __properties: ClassVar[List[str]] = ["schema", "statistics", "classification", "reclassification", "suggested", "tagify", "description"]

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
        """Create an instance of TLPCodeSnippetAnalytics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reclassification
        if self.reclassification:
            _dict['reclassification'] = self.reclassification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of suggested
        if self.suggested:
            _dict['suggested'] = self.suggested.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tagify
        if self.tagify:
            _dict['tagify'] = self.tagify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TLPCodeSnippetAnalytics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "statistics": TLPCodeFragmentStatistics.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "classification": TLPCodeFragmentClassification.from_dict(obj["classification"]) if obj.get("classification") is not None else None,
            "reclassification": TLPCodeFragmentReclassification.from_dict(obj["reclassification"]) if obj.get("reclassification") is not None else None,
            "suggested": TLPCodeSnippetSuggestedInteractions.from_dict(obj["suggested"]) if obj.get("suggested") is not None else None,
            "tagify": TLPCodeFragmentTagify.from_dict(obj["tagify"]) if obj.get("tagify") is not None else None,
            "description": TLPCodeFragmentDescription.from_dict(obj["description"]) if obj.get("description") is not None else None
        })
        return _obj


