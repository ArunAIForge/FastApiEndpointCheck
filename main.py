from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI app!"}


@app.get("/greet/{name}")
def greet(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/goodbye/{name}")
def say_goodbye(name: str) -> dict[str, str]:
    return {"message": f"Goodbye, {name}!"}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int | str]:
    return {"item_id": item_id, "name": f"Item {item_id}"}
