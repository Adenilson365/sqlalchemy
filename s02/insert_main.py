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

def insert_aditivo_nutritivo(nome: str, formula_quimica: str) -> AditivoNutritivo:

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_ssession() as session:
        session.add(an)
        session.commit()
    
    return an




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


def insert_ingrediente(nome: str) -> Ingrediente:
    ing: Ingrediente = Ingrediente(nome = nome)

    with create_ssession() as session:
        session.add(ing)
        session.commit()
    
    return ing


def insert_conservantes(nome: str, desc: str) -> Conservante:
    cons: Conservante = Conservante(nome=nome, descricao=desc)

    with create_ssession() as session:
        session.add(cons)
        session.commit()
    
    return cons



def insert_revendedor(cnpj: str, razao_social: str, contato: str) -> Revendedor:
    rev: Revendedor = Revendedor(cnpj = cnpj, razao_social = razao_social, contato = contato)

    with create_ssession() as session:
        session.add(rev)
        session.commit()

    return rev


def insert_lote(id_tipo_picole: int, quantidade: int) -> Lote:
    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_ssession() as session:
        session.add(lote)
        session.commit()

    return lote

def insert_notas_fiscais(valor: float, numero_serie: str, descricao: str, id_revendedor: int) -> NotaFiscal:
    nf: NotaFiscal = NotaFiscal(valor = valor, numero_serie=numero_serie, descricao = descricao, id_revendedor=id_revendedor)

    lote1 = insert_lote(1, 250)
    lote2 = insert_lote(1,300)

    nf.lotes.append(lote1)
    nf.lotes.append(lote2)

    with create_ssession() as session:
        session.add(nf)
        session.commit()

    return nf

# nota = insert_notas_fiscais(300.25, '1245', 'Nota de entrada', 1)

# print(nota.revendedor.razao_social) # Apartir da nota fiscal consigo acessar os dados da sua entidade estrangeira


def insert_picole(preco: float, id_sabor: int, id_tipo_embalagem: int, id_tipo_picole: int) -> Picole:
    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)

    picole.ingredientes.append(insert_ingrediente("Xarope de Maca"))
    picole.aditivos_nutritivos.append(insert_aditivo_nutritivo("VitaminaC", "VTMC"))
    picole.conservantes.append(insert_conservantes("Acido Citrico", "Um tipo de conservante"))

    with create_ssession() as session:
        session.add(picole)
        session.commit()

    return picole



if __name__ == '__main__':
    insert_aditivo_nutritivo("Vitamina A", "VTMA")
    insert_sabor("Limao")
    insert_tipo_embalagem("Plastica")
    insert_tipo_picole("Casquinha")
    insert_ingrediente("Xarope")
    insert_conservantes("Formoldeido", "Um Tipo de conservante quimico")
    insert_revendedor("99.999.999/0009-00", "Fulano de Tal LTDA", "(99) 99999 - 9999")
    insert_lote(1,100)
    insert_notas_fiscais(valor=15250.74, numero_serie='15014', descricao='Nota de entrada', id_revendedor=1)
    insert_picole(preco=10.85, id_sabor=1, id_tipo_embalagem=1, id_tipo_picole=1)