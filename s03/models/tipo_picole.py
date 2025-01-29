import sqlalchemy as sa
from sqlalchemy.orm import  Mapped, mapped_column
from datetime import datetime
from models.model_base import ModelBase

class TipoPicole(ModelBase):
    __tablename__ = 'tipos_picole'
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(sa.String(45), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(
        sa.DateTime, default=datetime.now, index=True, nullable=False
    )
    
    def __repr__(self) -> str: 
        return f'<TipoPicole: {self.nome}'