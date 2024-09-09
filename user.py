

class User:
    def __init__(self, name, cpf, data_nascimento):
        self.__name = name
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    def getName(self):
        return self.__name

    def getCpf(self):
        return self.__cpf
    
    def getDataNascimento(self):
        return self.__data_nascimento
    
    


    