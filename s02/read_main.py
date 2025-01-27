from typing import List
from sqlalchemy import func #Importa funções de agregação

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

def select_todos_aditivos() -> None:
    with create_ssession() as session:
        #Forma 1
        #aditivos: List[AditivoNutritivo] = session.query(AditivoNutritivo) #Traz um objeto do tipo Any
        #Forma 2
        aditivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all() # Já traz a lista pronta

        for an in aditivos:
            print(f'ID: {an.id}  -  Data: {formata_data(an.data_criacao)}')


def select_filtro_sabor(id_sabor: int) -> None:
    with create_ssession() as session:
        #Forma 1 -> Retorna None caso não encontre
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()

        #Forma 2 -> Retorna None caso não encontre, mesmo que first(), mas nomeado de forma mais explicita
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        #Forma 3 -> Retorna exec.NoResultFound caso não encontro, pode ser usado quando tem certeza que o item existe, ou vc quer obrigar exceção
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        #Forma 4 -> Usando where no lugar de filter
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one()

        print(f'ID: {sabor.id}, Data: {formata_data(sabor.data_criacao)}')


#Select mais complexo

def select_picole() -> None:
    with create_ssession() as session:
        picoles: List[Picole] = session.query(Picole).all()

        for picole in picoles:
            print(f'ID: {picole.id}, Data: {formata_data(picole.data_criacao)}, Sabor: {picole.sabor.nome}')

if __name__ == '__main__':
    #select_todos_aditivos()
    #select_filtro_sabor(1)
    select_picole()