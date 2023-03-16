from agency import *
from Accommodation import *
from cars import *

'''Criação  dos  diversos  objetos  referidos  acima
   Simulação de algumas  operações  de  reserva  e  entrega 
   Impressão, no final, da informação atual sobre a agência '''
def main():

    # criar uma agência
    agencia = AgenciaDeViagens("MyTravel","Aveiro")

    # adcionar alguns apartamentos   
    apartamentos = [Apartamento ("T4","Aveiro",1500,4), Apartamento ("T3","Albufeira",900,3), Apartamento ("T3","Lisboa",1000,3) ]
    apartamentos[0].checkin()
    for ap in apartamentos:
        agencia.adicionar_alojamento(ap) 
        

    # adicionar alguns quartos de hotel
    quartos  = [QuartoDeHotel ("Quarto 23","Hotel Américas (Aveiro)",200,"Duplo"), QuartoDeHotel ("Quarto 2","Hotel Imperial (Aveiro)",100,"Simples")]
    quartos[1].checkin()
    for quarto in quartos:
        agencia.adicionar_alojamento(quarto) 
    
    # adicionar algumas viaturas
    viaturas = [CarroEletrico("Tesla", "X","OF-04-90",200), CarroGasoleo("VW", "Golf", "AA-11-AA", 100), CarroGasolina("VW", "Golf", "AA-12-AA", 120)] 
    for viatura in viaturas:
        agencia.adicionar_viatura(viatura)

    # processamento ao nível da agência do aluguer de viaturas
    agencia.alugar_viatura("Tesla","X","OF-04-90")
    agencia.alugar_viatura("Tesla","Y","FF-14-09")
    
    
    # processamento ao nível da agência do aluguer de alojamentos
    agencia.alugar_alojamento("T4","Aveiro")
    agencia.alugar_alojamento("Quarto 23","Hotel Américas (Aveiro)")
    agencia.alugar_alojamento("Quarto 24","Hotel Américas (Aveiro)")
     
    # processamento ao nível da agência do ckeckout de um alojamento
    agencia.checkout_alojamento("T4","Aveiro")
    
    # processamento ao nível da agência da devolução de um carro que se encontrava alugado
    agencia.devolucao_viatura("Tesla", "X","OF-04-90")
    
    # mostrar informação sobre todos alojamentos e viaturas da agência
    print("\n----------------------")
    print(agencia)

 

if __name__ == "__main__":
    main()
