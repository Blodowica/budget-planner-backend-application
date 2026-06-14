from fastapi import APIRouter, Depends

from app.auth import get_current_user

router = APIRouter(prefix="/example", tags=["example"])


@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/add")
def add(a: int, b: int):
    return {"result": a + b}


@router.get("/protected")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": f"Hello {user.get('preferred_username', 'unknown')}"}
