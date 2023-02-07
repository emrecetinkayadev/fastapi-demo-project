import typing as t


def max_id(entities) -> t.Optional[int]:
    return max(entities, key=lambda entity: entity["id"]).get("id")
