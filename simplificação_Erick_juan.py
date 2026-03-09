

preco_frutas ={
    'maçã':2.5,
    'banana':1.8,
    'laranja':3.0

}


    # Definimos qual queremos procurar
frutas_desejadas = 'maçã'

    # Fazemos a busca direta usando método .get()
    # O .get() tenta encontar uma fruta; se não achar,mostra'fruta não encontrada'
resultado = preco_frutas.pegar(frutas_desejadas,'fruta não')

    #Exibimos o resultado
print('f"o preço da{frutas_desejada}é r${resultado}"')