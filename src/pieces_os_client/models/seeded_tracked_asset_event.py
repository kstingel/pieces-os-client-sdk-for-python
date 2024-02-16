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
from pieces_os_client.models.tracked_asset_event_identifier_description_pairs import TrackedAssetEventIdentifierDescriptionPairs
from typing import Optional, Set
from typing_extensions import Self

class SeededTrackedAssetEvent(BaseModel):
    """
    This seeded tracked asset event will be recieved by a context on the OS Server side, which will then be able to look up the asset id and structure the asset for shipment to Segment aka a fully built TrackedAssetEvent
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    asset: ReferencedAsset
    identifier_description_pair: TrackedAssetEventIdentifierDescriptionPairs
    metadata: Optional[TrackedAssetEventMetadata] = None
    __properties: ClassVar[List[str]] = ["schema", "asset", "identifier_description_pair", "metadata"]

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
        """Create an instance of SeededTrackedAssetEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identifier_description_pair
        if self.identifier_description_pair:
            _dict['identifier_description_pair'] = self.identifier_description_pair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededTrackedAssetEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "asset": ReferencedAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "identifier_description_pair": TrackedAssetEventIdentifierDescriptionPairs.from_dict(obj["identifier_description_pair"]) if obj.get("identifier_description_pair") is not None else None,
            "metadata": TrackedAssetEventMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None
        })
        return _obj

from pieces_os_client.models.referenced_asset import ReferencedAsset
from pieces_os_client.models.tracked_asset_event_metadata import TrackedAssetEventMetadata
# TODO: Rewrite to not use raise_errors
SeededTrackedAssetEvent.model_rebuild(raise_errors=False)

