# coding: utf-8

"""
    Agent Communication Protocol

    Specification of the API protocol for communication with an agent.  # noqa: E501

    The version of the OpenAPI document: v0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401

from pydantic import BaseModel, Field, StrictStr, conlist

from agbenchmark.agent_protocol_client.models.artifact import Artifact


class TaskAllOf(BaseModel):
    """
    Definition of an agent task.
    """

    task_id: StrictStr = Field(..., description="The ID of the task.")
    artifacts: conlist(Artifact) = Field(
        ..., description="A list of artifacts that the task has produced."
    )
    __properties = ["task_id", "artifacts"]

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
    def from_json(cls, json_str: str) -> TaskAllOf:
        """Create an instance of TaskAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in artifacts (list)
        _items = []
        if self.artifacts:
            _items.extend(_item.to_dict() for _item in self.artifacts if _item)
            _dict["artifacts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskAllOf:
        """Create an instance of TaskAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskAllOf.parse_obj(obj)

        return TaskAllOf.parse_obj(
            {
                "task_id": obj.get("task_id"),
                "artifacts": [
                    Artifact.from_dict(_item) for _item in obj.get("artifacts")
                ]
                if obj.get("artifacts") is not None
                else None,
            }
        )
