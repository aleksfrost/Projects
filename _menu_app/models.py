import uuid
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship

from database import Base


class Menu(Base):
    __tablename__ = 'menus'

    key = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String, index=True)
    type = Column(String, default='default')
    enabled = Column(Boolean, default=True)
#    submenus = Column(Integer, default=0)
#    dishes = Column(Integer, default=0)

#    items = relationship("Submenu", back_populates="owner")


class Submenu(Base):
    __tablename__ = 'submenus'

    key = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String, index=True)
    type = Column(String, default='default')
    enabled = Column(Boolean, default=True)
#    dishes = Column(Integer, default=0)
#    owner_key = Column(Integer, ForeignKey("menus.key"))

#    owner = relationship("Menu", back_populates="items")
#    items = relationship("Dish", back_populates="owner")


class Dish(Base):
    __tablename__: str = 'dishes'

    key = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String, index=True)
    type = Column(String, default='default')
    enabled = Column(Boolean, default=True)
    price = Column(Float, default=0.00)
#    owner_key = Column(Integer, ForeignKey("submenus.key"))

#    owner = relationship("Submenu", back_populates="items")
