import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
from models.model_base import ModelBase

class Revendedor(ModelBase):
    __tablename__ = 'revendedores'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    razao_social:Mapped[str]= mapped_column(sa.String(100), unique=True, nullable=False)
    cnpj: Mapped[str]= mapped_column(sa.String(45), unique=True, nullable=False)
    contato: Mapped[str]= mapped_column(sa.String(100), unique=True, nullable=False)

    
    def __repr__(self) -> str: 
        return f'<Revendedor: {self.razao_social}'