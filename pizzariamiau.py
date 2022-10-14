
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
    """
    pass


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
    """
    pass


def listar_ingredientes(ingredientes: dict[str, dict[str, float]], tipos_ingrediente: list[str]):
    """Lista os ingredientes dos tipos especificos e os imprime no terminal

    :param ingredientes: dicionário com os ingredientes ja inseridos
    :type ingredientes: dict[str,dict[str,float]
    :param tipos_ingrediente: tipo do ingrediente ["massa", "molho", "queijo", "cobertura"]
    :type tipos_ingrediente: list[str]
    :return: dicionario filtrado
    :rtype: dict[str,dict[str,float]]
    """
    pass


def montar_pizza(ingredientes: dict[str, dict[str, float]], ingredientes_pizza: dict[str, dict[str, float]]):
    """Filtra o dicionario pelos ingredientes escolhidos e calcula o preco e imprime no terminal

    :param ingredientes: dicionário com os ingredientes ja inseridos
    :type ingredientes: dict[str,dict[str,float]
    :param ingredientes_pizza: dicionario filtrado com os ingredeintes escolhidos
    :type ingredientes_pizza: dict[str,dict[str,float]]
    :return: Mensagem que lista os ingredientes escolhidos e o preco
    :rtype: str
    """
    pass
