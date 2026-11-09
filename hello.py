def greet(name: str) -> str:
    """Возвращает приветствие для пользователя."""
    if not name:
        raise ValueError("Имя не может быть пустым")
    return f"Привет, {name}!"

if __name__ == "__main__":
    print(greet("Мир"))