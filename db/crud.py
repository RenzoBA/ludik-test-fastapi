from sqlalchemy.orm import Session

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_name(db:Session, product_name:str):
    return db.query(models.Product).filter(models.Product.name == product_name).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name,description=product.description,price=product.price,stock_quantity=product.stock_quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db:Session, product_id: int, product: schemas.Product):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.stock_quantity = product.stock_quantity
    db.commit()
    return db_product


def update_partial_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.stock_quantity is not None:
        db_product.stock_quantity = product.stock_quantity
    
    db.commit()
    return db_product


def delete_product(db: Session, product: schemas.Product):
     db.delete(product)
     db.commit()
     return {"message":"Product deleted successfully"}