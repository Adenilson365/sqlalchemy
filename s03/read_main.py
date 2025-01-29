from typing import List
from sqlalchemy import func #Importa funções de agregação
from sqlalchemy.future import select
import asyncio

from conf.helpers import formata_data
from conf.db_ssession import create_ssession

from models.__all_models import ( AditivoNutritivo,
                                 Sabor,
                                 Picole,
                                 NotaFiscal,
                                 Conservante,
                                 Lote,
                                 Ingrediente,
                                 Revendedor,
                                 TipoEmbalagem,
                                 TipoPicole
                                 )


#select simples - similar a : SELECT * FROM <tabela>;

async def select_todos_aditivos() -> None:

    async with create_ssession() as session:

        # query = select(AditivoNutritivo)
        # aditivos: List[AditivoNutritivo] = await session.execute(query) # Já traz a lista pronta
        # aditivos = aditivos.scalars().all()

        aditivos: List[AditivoNutritivo] = (await session.execute(select(AditivoNutritivo))).scalars().all()
       
        for an in aditivos:
            print(f'ID: {an.id}  -  Data: {formata_data(an.data_criacao)}')


async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_ssession() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        #pode ser filter ou where

        sabor: Sabor = await session.execute(query)

        #Forma 1 - retorna none caso não encontre
        resultado = await session.execute(query)
        sabor: Sabor = resultado.scalars().first()

        #Forma 2 - retorne none caso não encontre
        #sabor: Sabor = resultado.scalars().one_or_none()

        #Forma 3 retorna exceção caso não exista
        #sabor: Sabor = resultado.scalars().one()

        print(f'ID: {sabor.nome}, Data: {formata_data(sabor.data_criacao)}')


#Select mais complexo

async def select_picole() -> None:
    async with create_ssession() as session:
        picoles: List[Picole] = (await session.execute(select(Picole))).scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}, Data: {formata_data(picole.data_criacao)}, Sabor: {picole.sabor.nome}')


async def select_gorup_by_picole() -> None:
    async with create_ssession() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)

        picoles: List[Picole] = (await session.execute(query)).scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}, tipo: {picole.tipo_picole.id}')


async def select_limit() -> None:
    async with create_ssession() as session:
        query = select(Sabor).limit(25)
        sabores: List[Sabor] = (await session.execute(query)).scalars().all()

        for sabor in sabores:
            print(f'Sabor: {sabor.nome}')


async def select_count() -> None:
    async with create_ssession() as session:
        query = select(func.count(Sabor.id))
        qtd: int = (await session.execute(query)).scalar()
        print(f'Quantidade: {qtd}')


# Funções de agregação

async def select_agregagacao() -> None:
    async with create_ssession() as session:

        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('minimo'),
            func.max(Picole.preco).label('maximo')
        )

        resultado = (await session.execute(query)).all() 

        print(f'resultado: {resultado}')
        print(f'soma {resultado[0][0]}')
        print(f'média {resultado[0][1]}')
        print(f'mínimo {resultado[0][2]}')
        print(f'máximo {resultado[0][3]}')
if __name__ == '__main__':
    #asyncio.run(select_todos_aditivos())
    #asyncio.run(select_filtro_sabor(1))
    #select_picole()
    #asyncio.run(select_gorup_by_picole())
    #asyncio.run(select_limit())
    #asyncio.run(select_count())
    asyncio.run(select_agregagacao())