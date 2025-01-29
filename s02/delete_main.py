from typing import List, Optional
from sqlalchemy import func #Importa funções de agregação

from conf.helpers import formata_data
from conf.db_ssession import create_ssession

from models.__all_models import ( 
                                 Revendedor,
                                 Picole
                                 )


def deletar_picole(id: int) -> None:
    with create_ssession() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Picole com id: {id}, Não encontrado!')


if __name__ == '__main__':
    deletar_picole(2)