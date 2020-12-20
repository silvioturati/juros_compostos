def juros_compostos(principal, taxa, periodo):
    """
    Função para calcular juros compostos = P(1 + R / 100)^T
    Onde:
    P é o valor do principal
    R é a taxa
    T é o tempo
    :param principal: float
    :param taxa: inteiro/float
    :param periodo: inteiro
    :return: float(resultado)
    """
    calculo_juros = principal * (pow((1 + taxa / 100), periodo))
    return calculo_juros
