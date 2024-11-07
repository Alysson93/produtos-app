from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from httpx import AsyncClient

API_URL = 'http://localhost:8000/api/products/'
templates = Jinja2Templates(directory='templates')

router = APIRouter(tags=['webapp'])


@router.get('/', response_class=HTMLResponse)
async def root(request: Request):
    async with AsyncClient() as client:
        response = await client.get(API_URL)
        products = response.json()
    return templates.TemplateResponse(
        request=request, name='home.html', context={'products': products}
    )


@router.get('/item/{id:int}', response_class=HTMLResponse)
async def item(request: Request, id: int):
    async with AsyncClient() as client:
        response = await client.get(f'{API_URL}{id}')
        product = response.json()
    return templates.TemplateResponse(
        request=request, name='item.html', context={'product': product}
    )


@router.get('/add', response_class=HTMLResponse)
def add_page(request: Request):
    return templates.TemplateResponse(request=request, name='novo-item.html')


@router.post('/add')
async def add(
    name: str = Form(...),
    description: Optional[str] = Form('No description'),
    qtd: int = Form(0),
    price: float = Form(0.0),
    has_discount: bool = Form(False),
    discount: Optional[float] = Form(0.0),
    image_url: Optional[str] = Form(None),
):
    async with AsyncClient() as client:
        await client.post(
            API_URL,
            json={
                'name': name,
                'description': description,
                'qtd': int(qtd),
                'price': float(price),
                'has_discount': bool(has_discount),
                'discount': float(discount),
                'image_url': image_url,
            },
        )
    return RedirectResponse(url='/', status_code=HTTPStatus.SEE_OTHER)


@router.get('/edit/{id:int}', response_class=HTMLResponse)
async def edit_page(request: Request, id: int):
    async with AsyncClient() as client:
        response = await client.get(f'{API_URL}{id}')
        product = response.json()
    return templates.TemplateResponse(request=request, name='editar-item.html', context={'product': product})


@router.post('/edit/{id:int}')
async def add(
    id: int,
    name: str = Form(...),
    description: Optional[str] = Form('No description'),
    qtd: int = Form(0),
    price: float = Form(0.0),
    has_discount: bool = Form(False),
    discount: Optional[float] = Form(0.0),
    image_url: Optional[str] = Form(None),
):
    async with AsyncClient() as client:
        await client.put(
            f'{API_URL}{id}',
            json={
                'name': name,
                'description': description,
                'qtd': int(qtd),
                'price': float(price),
                'has_discount': bool(has_discount),
                'discount': float(discount),
                'image_url': image_url,
            },
        )
    return RedirectResponse(url='/', status_code=HTTPStatus.SEE_OTHER)



@router.get('/del/{id:int}', response_class=HTMLResponse)
async def delete_item(request: Request, id: int):
    async with AsyncClient() as client:
        await client.get(f'{API_URL}delete/{id}')
    return RedirectResponse(url='/', status_code=HTTPStatus.SEE_OTHER)
