def greet(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip() or "friend"
    return f"Hello, {name}! ??"

if __name__ == "__main__":
    print(greet("Cursor"))
