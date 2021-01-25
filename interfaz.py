import tkinter as tk
from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import bd
import time

class Interfaz:
    def __init__(self):
        self.venta1=bd.Ventas()
        self.ventana = Tk()
        self.ventana.title("SEGURIDAD")
        self.ventana.geometry("350x150+500+250")
        self.ventana.configure(background='navy')
        self.ventana.resizable(0, 0)
        self.login()
        self.ventana.mainloop()

    def login(self):
        self.Label1=tk.Label(self.ventana, text="Usuario:",bg='navy',fg='white').place(x=10,y=20)
        #self.caja1 = Entry(self.ventana)
        #self.caja1.place(x=100,y=20)
        self.combo1= ttk.Combobox(self.ventana,state="readonly")
        self.combo1['value'] = self.venta1.bdusuario()
        self.combo1.current(0)
        self.combo1.place(x=100,y=20)
        self.Label2=tk.Label(self.ventana, text="Contraseña:",bg='navy',fg='white').place(x=10,y=80)
        self.caja2 = Entry(self.ventana, show="*")
        self.caja2.place(x=100,y=80)
        self.Button1=tk.Button(text="Entrar",command=lambda:self.entrar())
        self.Button1.pack(side=tk.BOTTOM)

    def entrar(self):

        self.datos=(self.combo1.get(), self.caja2.get())
        if self.venta1.verificar(self.datos):
            #ms.showinfo(title="Login correcto", message="Usuario y contraseña correctos")
            self.ventana.destroy()
            time.sleep(2)
            self.menuprincipal(self.datos)
        else:
            ms.showerror(title="Login incorrecto", message="Contraseña incorrecta")
            self.caja2.delete("0","end")


    def menuprincipal(self,data):
        self.venta1=bd.Ventas()
        self.ventana = Tk()
        self.ventana.title("ventas")
        self.ventana.geometry("500x300+350+200")
        self.ventana.configure(background='navy')
        self.ventana.resizable(0, 0)
        self.ventana2(data)
        self.ventana.mainloop()

    def ventana2(self,data):
        nombre=self.venta1.nombreusuario(data)
        self.Label3 = tk.Label(text="Bienvenido "+nombre[0][0]).pack(side=tk.TOP,fill=X)
        #self.nombreusuario= tk.Label(text="xdxd ").pack(side=tk.TOP,fill=X)
        self.cuaderno=ttk.Notebook(self.ventana)
        self.visualizar = Frame(self.cuaderno)
        self.cuaderno.add(self.visualizar, text="Visualizar", padding=10)
        self.cuaderno.pack(fill="both", expand="yes")
        self.Button2 = tk.Button(self.visualizar,text="Ver clientes",command=lambda:self.ver_clientes())
        self.Button2.place(x=20,y=40)
        self.Button3 = tk.Button(self.visualizar, text="Ver pedidos",command=lambda:self.ver_pedido())
        self.Button3.place(x=20, y=80)
        self.opciones=Frame(self.cuaderno)
        self.cuaderno.add(self.opciones, text="Opciones", padding=10)
        self.Button4 = tk.Button(self.opciones, text="Cambiar contraseña",command=lambda:self.cambiarpassgui())
        self.Button4.place(x=20,y=20)

    def ver_clientes(self):
        self.log = tk.Toplevel(self.ventana)
        self.log.transient(self.ventana)
        self.log.title('Clientes')
        columns = ('NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'CIUDAD', 'CATEGORIA')
        self.tree = ttk.Treeview(self.log, height=20, columns=columns, show='headings')
        self.tree.grid(row=0, column=0, sticky='news')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=160, anchor=tk.CENTER)
        for rec in self.venta1.verusuario():
            self.tree.insert('', 'end', value=rec)
        self.sb = tk.Scrollbar(self.log, orient=tk.VERTICAL, command=self.tree.yview)
        self.sb.grid(row=0, column=1, sticky='ns')
        self.tree.config(yscrollcommand=self.sb.set)

    def ver_pedido(self):
        self.log2 = tk.Toplevel(self.ventana)
        self.log2.transient(self.ventana)
        self.log2.title('Pedidos')
        columns = ('CLIENTE', 'COMERCIAL', 'FECHA', 'TOTAL')
        self.tree2 = ttk.Treeview(self.log2, height=20, columns=columns, show='headings')
        self.tree2.grid(row=0, column=0, sticky='news')
        for col in columns:
            self.tree2.heading(col, text=col)
            self.tree2.column(col, width=160, anchor=tk.CENTER)
        for rec in self.venta1.verpedido():
            self.tree2.insert('', 'end', value=rec)
        self.sb2 = tk.Scrollbar(self.log2, orient=tk.VERTICAL, command=self.tree2.yview)
        self.sb2.grid(row=0, column=1, sticky='ns')
        self.tree2.config(yscrollcommand=self.sb2.set)

    def cambiarpassgui(self):
        self.tlevel=tk.Toplevel()
        self.tlevel.title("Cambiar contraseña")
        self.tlevel.geometry("280x400+600+200")
        self.tlevel.resizable(0,0)
        self.tlevel.transient(self.ventana)
        self.Label4=tk.Label(self.tlevel,text="Ingrese contraseña actual").place(x=70,y=40)
        self.caja3= tk.Entry(self.tlevel,show="*")
        self.caja3.place(x=75,y=70)
        self.Label5 = tk.Label(self.tlevel, text="Ingrese nueva contraseña").place(x=70, y=120)
        self.caja4= tk.Entry(self.tlevel,show="*")
        self.caja4.place(x=75, y=150)
        self.Label6 = tk.Label(self.tlevel, text="Repita la nueva contraseña").place(x=70, y=200)
        self.caja5 = tk.Entry(self.tlevel,show="*")
        self.caja5.place(x=75, y=230)
        self.Button5 =tk.Button(self.tlevel, text="Guardar",command=lambda:self.cambiarpass()).place(x=100,y=300)

    def cambiarpass(self):
        passwords=[self.caja3.get(),self.caja4.get(),self.caja5.get()]
        if(len(passwords[0])==0 or len(passwords[1])==0 or len(passwords[2])==0):
            ms.showerror(title="Error", message="Llene los campos")
        else:
            if passwords[0] != self.datos[1]:
                ms.showerror(title="Error", message="Contraseña incorrecta")
                self.caja3.delete("0", "end")
            else:
                if passwords[1]!= passwords[2]:
                    ms.showerror(title="Error", message="Las contraseñas no coinciden")
                    self.caja5.delete("0", "end")
                else:
                    ms.showinfo(title="Éxito", message="Contraseña actualizada")
                    actualizar=[passwords[1],self.datos[0]]
                    self.venta1.bdcambiarpass(actualizar)
                    self.caja3.delete("0", "end")
                    self.caja4.delete("0", "end")
                    self.caja5.delete("0", "end")
                    self.tlevel.destroy()







interfaz=Interfaz()