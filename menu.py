from listaAgentes import ListaAgentes
class Menu:
    __opcion:int
    def __init__(self) -> None:
        self.__opcion=int
    def opciones(self,lista,jsonF):
        while self.__opcion!=0:
            print('\n1 - Insertar agente\n2 - Agregar Agente\n3 - Mostrar Agente\n4 - Generar Listado ordenado\n5 - Contar cantidad de agentes\n6 - Generar listado\n7 - Listar una categoria de investigacion\n8 - Almacenar en archivo JSON\n0 - Salir')
            self.__opcion=int(input('Ingrese opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nOPCION 1')
                lista.insertarAgente()
            elif self.__opcion==2:
                print('\nOPCION 2')
                lista.agregarAgenteFinal()
            elif self.__opcion==3:
                print('\nOPCION 3')
                lista.mostrarAgente()
            elif self.__opcion==4:
                print('\nOPCION 4')
                lista.generarListadoOrdenado()
            elif self.__opcion==5:
                print('\nOPCION 5')
                lista.contarAgentes()
            elif self.__opcion==6:
                print('\nOPCION 6')
                lista.generarColeccionOrdenada()
            elif self.__opcion==7:
                print('\nOPCION 7')
                lista.mostrarTotal()
            elif self.__opcion==8:
                print('\nOPCION 8')
                lista.guardarAgentes(jsonF)
        else:
            print('\nHA SALIDO DEL SISTEMA')
            lista.mostrarLista()