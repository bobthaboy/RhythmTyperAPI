from datetime import datetime, timezone


def parse_timestamp(ts) -> datetime | None:
    if isinstance(ts, str):
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    elif isinstance(ts, dict):
        return datetime.fromtimestamp(ts.get("_seconds", 0), tz=timezone.utc)
    else:
        return None


def find_new_data(data, indent=0):
    def type_name(value):
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "str"
        if value is None:
            return "None"
        if isinstance(value, dict):
            return "dict"
        if isinstance(value, list):
            return "list"
        return type(value).__name__

    def merge_types(values):
        types = {type_name(v) for v in values if v is not None}

        # int + float → float | int
        if "int" in types and "float" in types:
            types.discard("int")
            types.add("float | int")

        return " | ".join(sorted(types)) or "None"

    def walk(value, level):
        prefix = " " * level

        if isinstance(value, dict):
            for key, val in value.items():
                if isinstance(val, list):
                    if not val:
                        print(f"{prefix}{key}: list")
                    elif all(isinstance(x, dict) for x in val):
                        print(f"{prefix}{key}: list[dict]")
                        walk_list_dicts(val, level + 4)
                    else:
                        print(f"{prefix}{key}: list[{merge_types(val)}]")

                elif isinstance(val, dict):
                    print(f"{prefix}{key}: dict")
                    walk(val, level + 4)

                else:
                    print(f"{prefix}{key}: {type_name(val)}")

    def walk_list_dicts(items, level):
        # Collect all keys from every dict in the list
        keys = {}
        for item in items:
            for key, value in item.items():
                keys.setdefault(key, []).append(value)

        prefix = " " * level

        for key, values in keys.items():
            first = next((v for v in values if v is not None), None)

            if isinstance(first, dict):
                print(f"{prefix}{key}: dict")
                walk(first, level + 4)

            elif isinstance(first, list):
                if first and all(isinstance(x, dict) for x in first):
                    print(f"{prefix}{key}: list[dict]")
                    walk_list_dicts(
                        [x for v in values if isinstance(v, list) for x in v],
                        level + 4
                    )
                else:
                    print(f"{prefix}{key}: list[{merge_types(
                        [x for v in values if isinstance(v, list) for x in v]
                    )}]")

            else:
                print(f"{prefix}{key}: {merge_types(values)}")

    if isinstance(data, list):
        if not data:
            print("list")
        elif all(isinstance(x, dict) for x in data):
            print("list[dict]")
            walk_list_dicts(data, indent + 4)
        else:
            print(f"list[{merge_types(data)}]")
    else:
        walk(data, indent)

    raise RuntimeError("API testing: inspect response above.")
