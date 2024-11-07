import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Product:
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True, init=False
    )
    name: Mapped[str] = mapped_column(sa.String(30), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(250))
    qtd: Mapped[int] = mapped_column(sa.Integer)
    price: Mapped[float] = mapped_column(sa.Float)
    has_discount: Mapped[bool] = mapped_column(sa.Boolean)
    discount: Mapped[float] = mapped_column(sa.Float)
    image_url: Mapped[str] = mapped_column(sa.String)
