class Pessoa:
    def cumprimentar(self):
        return f'ola {id(self)}'


if __name__ == "__main__":
    Pessoa = Pessoa()
    print(Pessoa)
    print(id(Pessoa))
    print(Pessoa.cumprimentar())

