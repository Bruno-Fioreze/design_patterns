class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    #def __init__(self):
    #se possuir atribuição a propriedades dentro do init, corre o risco dela ser sobrescrita.

if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()

    print(as1 == as2)
    print(id(as1) == id(as2))

