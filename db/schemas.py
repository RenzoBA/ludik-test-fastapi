from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(max_digits=6, decimal_places=2)
    stock_quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
   name: Optional[str] = None
   description: Optional[str] = None
   price: Optional[Decimal] = Field(None, max_digits=6, decimal_places=2)
   stock_quantity: Optional[int] = None


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True