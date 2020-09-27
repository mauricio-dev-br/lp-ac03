# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: cliente.py
# Prof. Rafael Maximo
#
# Email Impacta: mauricio.santos@aluno.faculdadeimpacta.com.br

# Adicione aqui a importação dos módulos que julgar necesários, ex:
# import modulo_exemplo


class Cliente:
    """
    Classe que modela os clientes do banco.

    possui os atributos públicos:
    + nome
    + telefone
    + email

    e não possui nenhum método (público ou privado).

    O nome deve ser recebido na inicialização do objeto e ser guardado em
    um atributo privado, não podendo ser alterado posteriormente, após o cliente
    ter sido criado. O valor do atributo deve ser acessado pelo identificador
    público `nome` (use uma @property para isso).

    Tanto o email quando o telefone também precisam ser obrgatoriamente
    recebidos na inicialização e guardados em atributos privados.
    O acesso externo deve ser feito pelos atributos públicos
    `telefone` e `email`, usando a property e o setter.

    Considerações ao atribuir o valor do telefone e do email, válidas
    tanto para a incialização do objeto quanto para uma eventual
    alteração posterior feita através do atributo público:
    * caso o email não seja uma string, levanta um TypeError;
    * caso o email não seja válido (verificar se contém o @) levanta um ValueError;
    * caso o telefone não seja um número inteiro levanta um TypeError.
    """

    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if type(novo_telefone) == int:
            self.__telefone = novo_telefone
        else:
            raise TypeError()
            """
            Setter do telefone do cliente, caso não receba um número,
            levanta um TypeError
            """
            pass

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if type(novo_email) != str:
            raise TypeError()
        elif novo_email.find("@") == -1:
            raise ValueError()
        else:
            self.__email = novo_email
        """
        Setter do email do cliente, lançamento de exceções:
        levanta um TypeError caso não receba uma string; e
        levanta um ValueError caso não receba um email válido (contendo o @)
        """  