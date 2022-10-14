
ingredientes = {"massa": {}, "molho": {}, "queijo": {}, "cobertura": {}}
#ingredientes = {"massa":{"tradicional": 10.50, "recheada": 11.50}, "molho":{}, "queijo": {}, "cobertura": {}}


def cadastrar_ingrediente(ingredientes: dict[str, dict[str, float]],
                          tipo_ingrediente: str, novo_ingrediente: str, novo_preco: float):
    """Cadastra novo ingrediente e o imprime no terminal

    :param ingredientes: dicionário com os ingredientes ja inseridos
    :type ingredientes: dict[str,dict[str,float]
    :param tipo_ingrediente: tipo do novo ingrediente ["massa", "molho", "queijo", "cobertura"]
    :type tipo_ingrediente: str
    :param novo_ingrediente: nome do novo ingrediente
    :type novo_ingrediente: str
    :param novo_preco: preco do novo ingrediente (0.00)
    :type novo_preco: float
    :return: dicionario atualizado
    :rtype: dict[str,dict[str,float]]
    >>> cadastrar_ingrediente(ingredientes, "massa", "tradicional", 5.50)
    {'massa': {'tradicional': 5.5}, 'molho': {}, 'queijo': {}, 'cobertura': {}}
    {'massa': {'tradicional': 5.5}, 'molho': {}, 'queijo': {}, 'cobertura': {}}
    >>> cadastrar_ingrediente(ingredientes, "molho", "tomate", 7.50)
    {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 7.5}, 'queijo': {}, 'cobertura': {}}
    {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 7.5}, 'queijo': {}, 'cobertura': {}}
    >>> cadastrar_ingrediente(ingredientes, "molho", "tomate", 8.50)
    {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    """
    ingredientes[tipo_ingrediente][novo_ingrediente] = novo_preco
    print(ingredientes)
    return ingredientes


def remover_ingrediente(ingredientes: dict[str, dict[str, float]],
                        tipo_ingrediente: str, nome_ingrediente: str):
    """Remove ingrediente e o imprime no terminal

    :param ingredientes: dicionário com os ingredientes ja inseridos
    :type ingredientes: dict[str,dict[str,float]
    :param tipo_ingrediente: tipo do ingrediente ["massa", "molho", "queijo", "cobertura"]
    :type tipo_ingrediente: str
    :param nome_ingrediente: nome do ingrediente
    :type nome_ingrediente: str
    :return: dicionario atualizado
    :rtype: dict[str,dict[str,float]]
    >>> ingredientes = {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    >>> remover_ingrediente(ingredientes, "massa", "tradicional")
    {'massa': {}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    {'massa': {}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    >>> ingredientes = {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    >>> remover_ingrediente(ingredientes, "massa", "grossa")
    {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    """
    try:
        del ingredientes[tipo_ingrediente][nome_ingrediente]
        print(ingredientes)
    except:
        pass
    return ingredientes


def listar_ingredientes(ingredientes: dict[str, dict[str, float]], tipos_ingrediente: list[str]):
    """Lista os ingredientes dos tipos especificos e os imprime no terminal

    :param ingredientes: dicionário com os ingredientes ja inseridos
    :type ingredientes: dict[str,dict[str,float]
    :param tipos_ingrediente: tipo do ingrediente ["massa", "molho", "queijo", "cobertura"]
    :type tipos_ingrediente: list[str]
    :return: dicionario filtrado
    :rtype: dict[str,dict[str,float]]
    >>> ingredientes = {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {}, 'cobertura': {}}
    >>> listar_ingredientes(ingredientes, ["massa"])
    massa
    ...
    {'massa': {'tradicional': 5.5}}
    """
    dicionario_filtrado = {}
    for tipo in tipos_ingrediente:
        print(tipo)
        print(ingredientes[tipo], "\n")
        dicionario_filtrado[tipo] = ingredientes[tipo]
    return dicionario_filtrado


"""
cadastrar_ingrediente(ingredientes, "massa", "tradicional", 5.50)
cadastrar_ingrediente(ingredientes, "queijo", "tradicional", 6.50)
cadastrar_ingrediente(ingredientes, "cobertura", "tradicional", 7.50)
print(listar_ingredientes(ingredientes, ["massa", "queijo"]))
"""


def montar_pizza(ingredientes: dict[str, dict[str, float]], ingredientes_pizza: dict[str, dict[str, float]]):
    """Filtra o dicionario pelos ingredientes escolhidos e calcula o preco e imprime no terminal

    :param ingredientes: dicionário com os ingredientes ja inseridos
    :type ingredientes: dict[str,dict[str,float]
    :param ingredientes_pizza: dicionario filtrado com os ingredientes escolhidos. So pode ser escolhido uma massa
    :type ingredientes_pizza: dict[str,dict[str,float]]
    :return: Mensagem que lista os ingredientes escolhidos e o preco
    :rtype: str
    >>> ingredientes = {'massa': {'tradicional': 5.5, 'grossa': 7.5}, 'molho': {'tomate': 8.5}, 'queijo': {'mussarela': 7.0}, 'cobertura': {'calabresa': 8.5}}
    >>> ingredientes_pizza = {'massa': {'tradicional': 5.5}, 'molho': {'tomate': 8.5}, 'queijo': {'mussarela': 7.0}, 'cobertura': {'calabresa': 8.5}}
    >>> montar_pizza(ingredientes, ingredientes_pizza)
    'A pizza tem contem os ingredientes:\nmassa tradicional\nmolho tomate\nqueijo mussarela\ncobertura calabresa\n\n Seu preco e: \n29.5'
    """
    preco_total = float()
    lista_ingredientes = str()
    for tipo in ingredientes_pizza:
        for ingrediente in ingredientes_pizza[tipo]:
            if ingrediente in ingredientes[tipo]:
                lista_ingredientes += tipo + " "
                lista_ingredientes += ingrediente + "\n"
                preco_total += ingredientes_pizza[tipo][ingrediente]
            else:
                print(f"O ingrediente {ingrediente} nao foi encontrado")
    preco_total = str(preco_total)
    mensagem = "A pizza tem contem os ingredientes:\n" + \
        lista_ingredientes + "\n Seu preco e: \n" + preco_total
    return mensagem


"""
cadastrar_ingrediente(ingredientes, "massa", "tradicional", 5.50)
cadastrar_ingrediente(ingredientes, "queijo", "tradicional", 6.50)
cadastrar_ingrediente(ingredientes, "cobertura", "tradicional", 7.50)

mensagem = montar_pizza(
    ingredientes, {"massa": {"tradicional": 5.50}, "queijo": {"tradicional": 6.50}})
print(mensagem)
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
