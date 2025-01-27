import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
from typing import List

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

#Nota fiscal pode ter vários lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'), primary_key=True)
)

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id: Mapped[int] =mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] =mapped_column(sa.DateTime, default=datetime.now, index=True)

    valor: Mapped[float] =mapped_column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: Mapped[str] =mapped_column(sa.String(45), unique=True, nullable=False)
    descricao: Mapped[str] =mapped_column(sa.String(200), nullable=False)

    id_revendedor: Mapped[int] =mapped_column(sa.Integer, sa.ForeignKey('revendedores.id'))
    revendedor: Mapped[Revendedor] = orm.relationship('Revendedor', lazy='joined')

    #Uma nota fiscal pode ter vários lotes, e um lote está ligado a uma nota fiscal
    lotes: Mapped[List[Lote]] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')

    def __repr__(self) -> int: 
        return f'<Nota Fiscal: {self.numero_serie}'