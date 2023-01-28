import uuid


from pydantic import BaseModel


class Menu(BaseModel):
    key: str | None
    value: str | None = ''
    type: str | None = 'default'
    enabled: bool | None = True
#    submenus: int | None = 0
#    dishes: int | None = 0


class Submenu(BaseModel):
    key: str
    value: str | None = ''
    type: str | None = 'default'
    enabled: bool | None = True
#    dishes: int | None = 0


class Dish(BaseModel):
    key: str
    value: str | None = ''
    type: str | None = 'default'
    enabled: bool | None = True
    price: float | None = 0.00
