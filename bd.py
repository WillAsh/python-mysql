import pymysql
class Ventas:
    def conectar(self):
        db = pymysql.connect(host='sql10.freemysqlhosting.net',
                             user='sql10390533',
                             password='LtVePTPIPy',
                             database='sql10390533',
                             port= 3306)
        return db
    def verificar(self,datos):
        c=self.conectar()
        cursor=c.cursor()
        sql = 'SELECT * FROM seguridad WHERE usuario = %s AND aes_decrypt(contrasena, "asd") = %s'
        cursor.execute(sql,datos)
        c.close()
        return cursor.fetchall()

    def bdusuario(self):
        c = self.conectar()
        cursor = c.cursor()
        sql = 'SELECT usuario FROM seguridad '
        cursor.execute(sql)
        c.close()
        return cursor.fetchall()

    def verusuario(self):
        c = self.conectar()
        cursor = c.cursor()
        sql = 'SELECT nombre, apellido1, apellido2, ciudad, categoría from cliente '
        cursor.execute(sql)
        return cursor

    def verpedido(self):
        c = self.conectar()
        cursor = c.cursor()
        sql = 'select * from verpedido '
        cursor.execute(sql)
        return cursor

    def nombreusuario(self,datos):
        c = self.conectar()
        cursor = c.cursor()
        asd=datos[0]
        sql = ("select nombres from seguridad where usuario = '%s'")%asd
        cursor.execute(sql)
        return cursor.fetchall()

    def bdcambiarpass(self,datos):
        c = self.conectar()
        cursor = c.cursor()
        sql = ("update seguridad set contrasena = aes_encrypt('%s','asd') where usuario = '%s'")%(datos[0],datos[1])
        cursor.execute(sql)
        c.commit()

