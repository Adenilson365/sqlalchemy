import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__ = 'lotes'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True, nullable=False)

    id_tipo_picole: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: Mapped['TipoPicole'] = orm.relationship('TipoPicole', lazy='joined')

    quantidade: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    
    def __repr__(self) -> int: 
        return f'<Lote: {self.id}'