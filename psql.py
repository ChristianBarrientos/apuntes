import psycopg2
"""
UPDATE  observatorio_ubicacion set estado = 'HAB' where id_nacional = '10035'

class foo:
    def __init__(self, **kwargs):
        vars(self).update(kwargs)
        """
class Conexion_BD():
    
    def __init__(self, **kwargs):
        vars(self).update(kwargs)

    #user,password,host,port,database
    def conectar_bd(self):
        try:
            self.connection = psycopg2.connect(user=self.user,password=self.password,host=self.host,port=self.port,database=self.database)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("Error en Conexion")
            print(e)
            return False
        return True

    def cerrar_conexion(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
        return True


    def update_estado_ubicaciones(self,id_nacionles):
        try:
            for id_nacional in id_nacionles:
                postgres_insert_query = """ UPDATE  observatorio_ubicacion set estado = %s where id_nacional = %s """
                record_to_insert = ('HAB',id_nacional)
                #record_to_insert = (5, 'One Plus 6', 950)
                #cursor.execute(postgres_insert_query, record_to_insert)
                self.cursor.execute(postgres_insert_query, record_to_insert)
                self.connection.commit()
                count = self.cursor.rowcount
            
        except (Exception, psycopg2.Error) as error :
            if(self.connection):
                print("Error al EJecutar Funcion", error)
                return False 
        return True



bd_psql = Conexion_BD(user='postgres',password='postgres',host='localhost',port=5432,database='observatorio_clima')

if bd_psql.conectar_bd():
    print("COnecto CORRECTAMENTE")
    bd_psql.update_estado_ubicaciones(['10077'])
else:
    print("Error al conecta con la BD")