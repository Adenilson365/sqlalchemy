import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
from models.model_base import ModelBase

class Ingrediente(ModelBase):
    __tablename__ = 'ingredientes'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    nome: Mapped[str]= mapped_column(sa.String(45), unique=True, nullable=False)
    
    def __repr__(self) -> str: 
        return f'<Ingrediente: {self.nome}'