from typing import List
from sqlalchemy import func #Importa funções de agregação
from sqlalchemy.future import select
import asyncio

from conf.helpers import formata_data
from conf.db_ssession import create_ssession

from models.__all_models import ( 
                                 Sabor,
                                 Picole
                                 )


async def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    async with create_ssession() as session:
        #Passo1
        query = select(Sabor).filter(Sabor.id == id_sabor)
        sabor: Sabor = (await session.execute(query)).scalars().one_or_none()
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            #Passo 2
            sabor.nome = novo_nome
            #Passo 3
            await session.commit()
        else:
            print(f"Sabor id: {id_sabor} Não Encontrado!")



"""
Para atualizar:
1 - Buscamos o dado
2 - Alteramos o dado
3 - Salvamos o novo dado
"""

if __name__ == "__main__":
    from read_main import select_filtro_sabor
    #select_filtro_sabor(2)
    asyncio.run(atualizar_sabor(4, "teste2"))
    #select_filtro_sabor(2)
