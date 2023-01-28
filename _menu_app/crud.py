import uuid

from sqlalchemy.orm import Session

import models
import schemas


def get_menu_by_key(db: Session, key: int):
    return db.query(models.Menu).filter(models.Menu.key == key).first()


def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Menu).offset(skip).limit(limit).all()


def add_menu(db: Session, menu: schemas.Menu):
    db_menu = models.Menu(key=menu.key)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def get_submenus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Submenu).offset(skip).limit(limit).all()


def create_menu_submenu(db: Session, submenu: schemas.Submenu):
    db_submenu = models.Submenu(**submenu.dict())
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


