class BilleteraV:
    __titular: str
    __numero_celular: str
    __alias: str
    __saldo: float

    def __init__(self,titular,numero_celular,alias,saldo):
        self.__titular = titular
        self.__numero_celular = numero_celular
        self.__alias = alias
        self.__saldo = saldo

    def __str__(self):
        return ("Titular:{},Numero de Celular{},Alias{},Saldo{}".format(self.__titular,self.__numero_celular,self.__alias,self.__saldo))    

    def get_Titular(self):
        return self.__titular
    def get_NumeroC(self):
        return self.__numero_celular
    def get_Alias(self):
        return self.__alias
    def get_Saldo(self):
        return self.__saldo
    
    def IngresarDinero(self, importe):
        if importe > 0:
            self.__saldo += importe
        return self.__saldo
    
    def PagarCompra(self,importe):
        if importe <= self.__saldo:
            #puedo comprar
            self.__saldo -= importe
            return self.__saldo    
        else: 
            return -1
            
    def transferir(self):
        return