
# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: conta.py
# Prof. Rafael Maximo
#
# Email Impacta: mauricio.santos@aluno.faculdadeimpacta.com.br

# Adicione aqui a importação dos módulos que julgar necesários, ex:
# import modulo_exemplo


class Conta:
    """
    A classe Conta deverá possuir os atributos públicos:
    + clientes
    + numero
    + saldo

    E os métodos públicos:
    + sacar()
    + depositar()
    + tirar_extrato()

    A lista de clientes, o número da conta e o saldo inicial devem obrigatoriamente
    serem recebidos na inicialização do objeto e devem ser guardados em atributos privados
    acessíveis apenas para leitura através dos atributos públicos mencionados acima,
    usando a property para isso.

    O saldo só poderá ser alterado pelos métodos sacar e depositar,
    não podendo ser alterado diretamente.

    O extrato da conta deverá ser uma lista e todas as operações feitas na conta
    (abertura da conta, saque e deposito) devem aparecer no extrato como tuplas
    da seguinte forma:
    -------------------------------------------------
          operação       |    entrada no extrato
    ---------------------|---------------------------
    * abertura da conta  | ('saldo inicial', 1000)
    * saque              | ('saque', 100)
    * depósito           | ('deposito', 250)
    -------------------------------------------------
    As operações devem aparecer da ordem em que foram feitas, ou seja,
    o primeiro item da lista deverá sempre ser o de abertura da conta.

    DICA: Crie um atributo privado para guardar as operações feitas na conta

    ------------------------------------------------------------------------

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, como método especial __init__
        deve receber na inicialização os atributos:
            clientes,
            numero_conta,
            saldo_inicial
    * Property da lista de clientes
    * Property do saldo da conta
    * Property do numero da conta
    * Método sacar da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
    * Método depositar da classe Conta, operação deve aparecer no extrato
    * Método tirar_extrato da classe Conta
        retorna uma lista com as operações (Tuplas) executadas na Conta
    """
    pass