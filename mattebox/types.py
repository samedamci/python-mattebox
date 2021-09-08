from __future__ import annotations


class Program:
    name: str
    channel: str
    content_id: str
    description: str
    ts_start: int
    type: str

    @classmethod
    def from_channel_program(cls, data: dict) -> Program:
        obj = cls()
        obj.__dict__ = {
            "name": data["name"],
            "channel": data["channelKey"],
            "content_id": data["epgId"],
            "description": data["shortDescription"],
            "ts_start": data["startTimestamp"],
            "type": "program",
        }
        return obj

    @classmethod
    def from_recording(cls, data: dict) -> Program:
        obj = cls()
        obj.__dict__ = {
            "name": data["title"],
            "channel": data["channelKey"],
            "content_id": data["pvrProgramId"],
            "description": data["longDescription"],
            "ts_start": data["startTime"],
            "type": "recording",
        }
        return obj

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"
