from typing import List, Optional
from sqlalchemy import func #Importa funções de agregação
from sqlalchemy.future import select
import asyncio

from conf.db_ssession import create_ssession

from models.__all_models import ( 
                                 Revendedor,
                                 Picole
                                 )


async def deletar_picole(id: int) -> None:
    async with create_ssession() as session:
        query = select(Picole).filter(Picole.id == id)
        picole: Optional[Picole] = (await session.execute(query)).scalars().unique().one_or_none()
        #picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id).one_or_none()

        if picole:
            await session.delete(picole)
            await session.commit()
        else:
            print(f'Picole com id: {id}, Não encontrado!')


if __name__ == '__main__':
    asyncio.run(deletar_picole(2))