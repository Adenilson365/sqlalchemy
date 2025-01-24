import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker #cria a sessão com o banco de dados
from pathlib import Path #usado no sqlite
from typing import Optional

from sqlalchemy.orm import Session 
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    """
    Função para configurar a conexão com o banco de dados
    """
    global __engine 

    if __engine:
        return
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent 
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread":False})
    else:
        conn_str = f'postgresql://admin:admin@localhost:5432/picoles'
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_ssession() -> Session:
    """
    Função para criar a sessão de conexão com o bando de dados
    Essa sessão é criada usando a engine
    """
    global __engine

    if not __engine:
        create_engine() # para usar sqlite  -> create_engine(sqlite=True)
    
    __session = sessionmaker(__engine, xpire_on_commit=False, class_=Session)

    session: Session = __session()

    return session
    


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models
    ModelBase.metadata.drop_all(__engine)  #Vai apagar as tabelas que já existir
    ModelBase.metadata.create_all(__engine) #Vai criar novas tableas