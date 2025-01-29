import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
from models.model_base import ModelBase

class Conservante(ModelBase):
    __tablename__ = 'conservantes'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    nome: Mapped[str]= mapped_column(sa.String(45), unique=True, nullable=False)
    descricao: Mapped[str]= mapped_column(sa.String(100), unique=True, nullable=False)
    
    def __repr__(self) -> str: 
        return f'<Conservante: {self.nome}'