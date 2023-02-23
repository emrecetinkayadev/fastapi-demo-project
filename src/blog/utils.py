import typing as t
import hashlib



def max_id(entities) -> t.Optional[int]:
    if entities == []:
        return 0
    return max(entities, key=lambda entity: entity["id"]).get("id")

