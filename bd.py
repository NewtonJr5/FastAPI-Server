
class Bd:
    def __init__(self):
        self.users = []
    
    def addUser(self, user):
        self.users.append(user)

    def getUsers(self):
        return self.users
    
    def showUsers(self):
        for user in self.users:
            print("User: " + user.getName())
            print("CPF: " + str(user.getCpf()))
            print("Data de Nascimento: " + user.getDataNascimento())
            print("")
    
    def getUser(self, cpf):
        for user in self.users:
            if user.getCpf() == cpf:
                return user
        return None