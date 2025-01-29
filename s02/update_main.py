from typing import List
from sqlalchemy import func #Importa funções de agregação

from conf.helpers import formata_data
from conf.db_ssession import create_ssession

from models.__all_models import ( 
                                 Sabor,
                                 Picole
                                 )


def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_ssession() as session:
        #Passo1
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            #Passo 2
            sabor.nome = novo_nome
            #Passo 3
            session.commit()
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
    select_filtro_sabor(2)
    atualizar_sabor(2, "asdsad")
    select_filtro_sabor(2)
