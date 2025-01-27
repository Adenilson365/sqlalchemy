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

def insert_aditivo_nutritivo() -> None:
    print("Cadastrando aditivo nutritivo")

    nome: str = input("Informe o Nome do Aditivo: ")
    formula_quimica: str = input("Informa a fórmula quimica: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_ssession() as session:
        session.add(an)
        session.commit()
    
    print('Aditivo cadastrado com sucesso')
    print(f'ID: {an.id} - data: {an.data_criacao}')



def insert_sabor(nome: str) -> None:

    sa: Sabor = Sabor(nome = nome) 
    
    with create_ssession() as session:
        session.add(sa)
        session.commit()

    print(f'Sabor id: {sa.id} - Data: {sa.data_criacao}')



def insert_tipo_embalagem(nome: str) -> None:
    tpe: TipoEmbalagem = TipoEmbalagem(nome = nome)
    
    with create_ssession() as session:
        session.add(tpe)
        session.commit()

    print(f'Tipo Embalagem id: {tpe.id} - Data: {tpe.data_criacao}')


def insert_tipo_picole(nome:str) -> None:
    tpp: TipoPicole = TipoPicole(nome = nome)

    with create_ssession() as session:
        session.add(tpp)
        session.commit()

    print(f'Tipo Picole id: {tpp.id} - Data: {tpp.data_criacao}')


def inser_ingrediente(nome: str) -> None:
    ing: Ingrediente = Ingrediente(nome = nome)

    with create_ssession() as session:
        session.add(ing)
        session.commit()
    
    print(f'Ingrediente id: {ing.id} - Data: {ing.data_criacao}')


def insert_conservantes(nome: str, desc: str) -> None:
    cons: Conservante = Conservante(nome=nome, descricao=desc)

    with create_ssession() as session:
        session.add(cons)
        session.commit()

    print(f'Conservante id: {cons.id} - Data: {cons.data_criacao}')

def insert_revendedor(cnpj: str, razao_social: str, contato: str) -> Revendedor:
    rev: Revendedor = Revendedor(cnpj = cnpj, razao_social = razao_social, contato = contato)

    with create_ssession() as session:
        session.add(rev)
        session.commit()

    #print(f'Revendedor ID: {rev.id} - CNPJ: {rev.cnpj}')
    return rev

#print(insert_revendedor("99.999.999/0009-07", "Fulano de Tal SA", "(99) 99999 - 9997"))

#rev = insert_revendedor("99.999.999/0009-08", "Sorveteria SorvBom", "(99) 99999 - 9998")

#print(rev.__repr__)
if __name__ == '__main__':
    insert_aditivo_nutritivo()
    insert_sabor("Limao")
    insert_tipo_embalagem("Plastica")
    insert_tipo_picole("Casquinha")
    inser_ingrediente("Xarope")
    insert_conservantes("Formoldeido", "Um Tipo de conservante quimico")
    insert_revendedor("99.999.999/0009-00", "Fulano de Tal LTDA", "(99) 99999 - 9999")
