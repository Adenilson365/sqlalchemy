from conf.db_ssession import create_ssession
import asyncio 

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

async def insert_aditivo_nutritivo(nome: str, formula_quimica: str) -> AditivoNutritivo:

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    async with create_ssession() as session:
        session.add(an)
        await session.commit()
    
    return an




async def insert_sabor(nome: str) -> Sabor:

    sa: Sabor = Sabor(nome = nome) 
    
    async with create_ssession() as session:
        session.add(sa)
        await session.commit()

    return sa
    #print(f'Sabor id: {sa.id} - Data: {sa.data_criacao}')



async def insert_tipo_embalagem(nome: str) -> TipoEmbalagem:
    tpe: TipoEmbalagem = TipoEmbalagem(nome = nome)
    
    async with create_ssession() as session:
        session.add(tpe)
        await session.commit()

    #print(f'Tipo Embalagem id: {tpe.id} - Data: {tpe.data_criacao}')
    return tpe


async def insert_tipo_picole(nome:str) -> TipoPicole:
    tpp: TipoPicole = TipoPicole(nome = nome)

    async with create_ssession() as session:
        session.add(tpp)
        await session.commit()

    #print(f'Tipo Picole id: {tpp.id} - Data: {tpp.data_criacao}')
    return tpp

async def insert_ingrediente(nome: str) -> Ingrediente:
    ing: Ingrediente = Ingrediente(nome = nome)

    async with create_ssession() as session:
        session.add(ing)
        await session.commit()
    
    return ing


async def insert_conservantes(nome: str, desc: str) -> Conservante:
    cons: Conservante = Conservante(nome=nome, descricao=desc)

    async with create_ssession() as session:
        session.add(cons)
        await session.commit()
    
    return cons



async def insert_revendedor(cnpj: str, razao_social: str, contato: str) -> Revendedor:
    rev: Revendedor = Revendedor(cnpj = cnpj, razao_social = razao_social, contato = contato)

    async with create_ssession() as session:
        session.add(rev)
        await session.commit()

    return rev


async def insert_lote(id_tipo_picole: int, quantidade: int) -> Lote:
    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    async with create_ssession() as session:
        session.add(lote)
        await session.commit()

    return lote

async def insert_notas_fiscais(valor: float, numero_serie: str, descricao: str, id_revendedor: int) -> NotaFiscal:
    nf: NotaFiscal = NotaFiscal(valor = valor, numero_serie=numero_serie, descricao = descricao, id_revendedor=id_revendedor)

    lote1 = await insert_lote(1, 250)
    lote2 = await insert_lote(1,300)

    nf.lotes.append(lote1)
    nf.lotes.append(lote2)

    async with create_ssession() as session:
        session.add(nf)
        await session.commit()


    return nf

# nota = insert_notas_fiscais(300.25, '1245', 'Nota de entrada', 1)

# print(nota.revendedor.razao_social) # Apartir da nota fiscal consigo acessar os dados da sua entidade estrangeira


async def insert_picole(preco: float, id_sabor: int, id_tipo_embalagem: int, id_tipo_picole: int) -> Picole:
    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)

    picole.ingredientes.append(await insert_ingrediente("Xarope de Maca"))
    picole.aditivos_nutritivos.append(await insert_aditivo_nutritivo("VitaminaC", "VTMC"))
    picole.conservantes.append(await insert_conservantes("Acido Citrico", "Um tipo de conservante"))

    async with create_ssession() as session:
        session.add(picole)
        await session.commit()

    return picole



if __name__ == '__main__':
    async def main():
        await insert_aditivo_nutritivo("Vitamina Aac", "VTMAcd")
        await insert_sabor("Limaonada")
        await insert_tipo_embalagem("Plastica")
        await insert_tipo_picole("Casquinha")
        await insert_ingrediente("Xarope")
        await insert_conservantes("Formoldeido", "Um Tipo de conservante quimico")
        await insert_revendedor("99.999.999/0009-00", "Fulano de Tal LTDA", "(99) 99999 - 9999")
        await insert_lote(1,100)
        await insert_notas_fiscais(valor=15250.74, numero_serie='15014', descricao='Nota de entrada', id_revendedor=1)
        await insert_picole(preco=10.85, id_sabor=1, id_tipo_embalagem=1, id_tipo_picole=1)

    asyncio.run(main())