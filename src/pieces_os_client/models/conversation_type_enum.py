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
import json
from enum import Enum
from typing_extensions import Self


class ConversationTypeEnum(str, Enum):
    """
    This is a type of conversation, for now just COPILOT.
    """

    """
    allowed enum values
    """
    COPILOT = 'COPILOT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConversationTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


