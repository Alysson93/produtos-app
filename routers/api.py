from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from DTOs import ProductRequest, ProductResponse
from models import Product

router = APIRouter(prefix='/api/products', tags=['products'])


@router.get('/', response_model=list[ProductResponse])
def get_products(session: Session = Depends(get_session)):
    products = session.scalars(select(Product)).all()
    return products


@router.get('/{id:int}', response_model=ProductResponse)
def get_product_by_id(id: int, session: Session = Depends(get_session)):
    product = session.scalars(select(Product).where(Product.id == id)).first()
    if product is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Product not found'
        )
    return product


@router.post('/', status_code=HTTPStatus.OK)
def create_product(
    product: ProductRequest, session: Session = Depends(get_session)
):
    p = Product(
        name=product.name,
        description=product.description,
        qtd=product.qtd,
        price=product.price,
        has_discount=product.has_discount,
        discount=product.discount,
        image_url=product.image_url,
    )
    session.add(p)
    session.commit()
    session.refresh(p)
    return p.id


@router.put('/{id:int}', status_code=HTTPStatus.NO_CONTENT)
def get_product_by_id(
    id: int, data: ProductRequest, session: Session = Depends(get_session)
):
    product = session.scalars(select(Product).where(Product.id == id)).first()
    if product is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Product not found'
        )
    product.name = data.name
    product.description = data.description
    product.qtd = data.qtd
    product.discount = data.discount
    product.has_discount = data.has_discount
    product.price = data.price
    product.image_url = data.image_url
    session.commit()
    session.refresh(product)


@router.get('/delete/{id:int}', status_code=HTTPStatus.NO_CONTENT)
def delete_product(id: int, session: Session = Depends(get_session)):
    product = session.scalars(select(Product).where(Product.id == id)).first()
    if product is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Product not found'
        )
    session.delete(product)
    session.commit()
