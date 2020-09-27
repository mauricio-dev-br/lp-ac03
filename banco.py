# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: banco.py
# Prof. Rafael Maximo
#
# Email Impacta: mauricio.santos@aluno.faculdadeimpacta.com.br

# Adicione aqui a importação dos módulos que julgar necesários, ex:
# import modulo_exemplo

from conta import Conta
class Banco:
    """
    Classe que modela o banco

    possui os atributos públicos:
    + nome
    + contas

    possui o método público:
    + abre_conta()

    O nome deve ser recebido na inicialização do objeto e ser guardado em um
    atributo privado, acessível apenas para leitura através de uma property.

    Crie um atributo privado que irá armazenar as contas criadas no banco
    e utilze esse atributo para gerar automaticamente o número das novas
    contas do banco. A lista de contas deverá ser acessível apenas para leitura
    através de uma property `contas`.

    O método abre_conta deverá abrir uma nova conta, sendo responsável por
    atribuir o numero da conta em ordem crescente, a partir de 1 para a
    primeira conta aberta.

    ----------------------------------------------------------------------------

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, como método especial __init__
        deve receber na inicialização os atributos:
            nome
    * Property do nome do banco.
    * Property da lista de contas do banco.
    * Método abrir_conta da classe Banco:
        recebe a lista de clientes e o saldo inicial da conta,
        caso o saldo inicial seja negativo levanta um ValueError (a conta não é aberta).
        DICA: O parâmetro clientes será uma lista com instâncias do tipo Cliente.
    """


    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []       

    @property
    def nome(self):
        return self.__nome

    @property
    def contas(self):
        return self.__contas

    def abre_conta(self, clientes, saldo):
        if(saldo < 0):
            raise ValueError()
        else:
            self.__contas.append(Conta(clientes, (len(self.__contas)+1), saldo))