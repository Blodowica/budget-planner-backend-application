from fastapi import APIRouter

router = APIRouter(prefix="/example", tags=["example"])


@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
