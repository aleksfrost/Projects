from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# tags for menu
@app.post("/menu/", response_model=schemas.Menu)
def create_menu(menu: schemas.Menu, db: Session = Depends(get_db)):
    return crud.add_menu(db=db, menu=menu)


@app.get("/menu/", response_model=List[schemas.Menu])
def get_menu(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    menus = crud.get_menus(db, skip=skip, limit=limit)
    if not menus:
        raise HTTPException(status_code=201, detail="OK")
    return menus


@app.get("/menu/{key}", response_model=schemas.Menu)
def get_menu_by_key(key: int, db: Session = Depends(get_db)):
    db_menu = crud.get_menu_by_key(db, key=key)
    if db_menu is None:
        return {'detail': "Not found"}
    return db_menu


"""
@app.post("/menu/{key}/submenus/", response_model=None)
def create_submenu_for_menu(
    key: str, submenu: schemas.Submenu, db: Session = Depends(get_db)
):
    return crud.create_menu_submenu(db=db, submenu=submenu, key=key)

"""


@app.get("/submenus/", response_model=List[schemas.Submenu])
def read_subs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    submenus = crud.get_submenus(db, skip=skip, limit=limit)
    return submenus
