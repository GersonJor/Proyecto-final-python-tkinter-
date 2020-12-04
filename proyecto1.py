
from tkinter import Button, Entry, Frame, Label, Tk, Toplevel, ttk, messagebox, Scrollbar
from tkinter.font import Font
from tkinter import *
from tkinter.ttk import Combobox

import sqlite3#importando la base de datos "SQLite"
# from IPython.terminal.pt_inputhooks import tk

class Miventana(Frame):#creamos una clase"Mi ventana" y luego heredamos la clase "Frame"

    db_name='database.db'#nombramos a una variable la base de datos creado desde el SQLite

    def __init__(self,master=None):#creamos el constructor de la clase POO y nombramos a master con un valor nulo
        super().__init__(master,width=500,height=350,bg="#BCBEB4")#heredamos de la clase Frame con super() y luego nombramos el ancho, la altura, y el color de la ventana Frame
        
        self.master=master
        self.pack(expand=True,fill='both')
        self.crear_widgets()
    
    def Productos(self,event):#creamos una funcion "Productos" que reciba un parametro "event" para luego con un command lo ejecutemos
        
        if (self.txt6_Cod1.get()) == '0':#con el 1er combobox del frame si el valor seleccionado es igual a 0
             self.etiqueta_prod1["text"]="0"
             self.etiqueta_Unid1["text"]="0"
             self.a1=0
             self.etiqueta_precio1["text"]="S/",self.a1 
        elif (self.txt6_Cod1.get()) == '1':#si el valor seleccionado es igual a 1
            self.etiqueta_prod1["text"]="Linterna de baterías"#con esa etiqueta_prod1 imprimimos el valor digitado en la ventana frame
            self.etiqueta_Unid1["text"]="S/8.00"
            
        elif self.txt6_Cod1.get() == '2':#si el valor seleccionado es igual a 2
            self.etiqueta_prod1["text"]="Taladro"
            self.etiqueta_Unid1["text"]="S/40.00"
        elif self.txt6_Cod1.get() == '3':#si el valor seleccionado es igual a 3
            self.etiqueta_prod1["text"]="Escalera"
            self.etiqueta_Unid1["text"]="S/80.00"
        elif self.txt6_Cod1.get() == '4':
            self.etiqueta_prod1["text"]="Alicate"
            self.etiqueta_Unid1["text"]="S/12.00"
        elif self.txt6_Cod1.get() == '5':
            self.etiqueta_prod1["text"]="Martillo"
            self.etiqueta_Unid1["text"]="S/15.00"
        elif self.txt6_Cod1.get() == '6':
            self.etiqueta_prod1["text"]="Cinta métrica"
            self.etiqueta_Unid1["text"]="S/5.00"
        
        
        if(self.txt7_Cod2.get())=='0':#con el 2do combobox del frame si el valor seleccionado es igual a 0
            self.etiqueta_prod2["text"]="0"
            self.etiqueta_Unid2["text"]="0"
            self.a2=0
            self.etiqueta_precio2["text"]="S/",self.a2 
        elif(self.txt7_Cod2.get())=='1':
            self.etiqueta_prod2["text"]="Linterna de baterías"
            self.etiqueta_Unid2["text"]="S/8.00"
        elif self.txt7_Cod2.get() == '2':
            self.etiqueta_prod2["text"]="Taladro"
            self.etiqueta_Unid2["text"]="S/40.00"
        elif self.txt7_Cod2.get() == '3':
            self.etiqueta_prod2["text"]="Escalera"
            self.etiqueta_Unid2["text"]="S/80.00"
        elif self.txt7_Cod2.get() == '4':
            self.etiqueta_prod2["text"]="Alicate"
            self.etiqueta_Unid2["text"]="S/12.00"
        elif self.txt7_Cod2.get() == '5':
            self.etiqueta_prod2["text"]="Martillo"
            self.etiqueta_Unid2["text"]="S/15.00"
        elif self.txt7_Cod2.get() == '6':
            self.etiqueta_prod2["text"]="Cinta métrica"
            self.etiqueta_Unid2["text"]="S/5.00"

        if(self.txt8_Cod3.get())=='0':#con el 3ro combobox del frame si el valor seleccionado es igual a 0
            self.etiqueta_prod3["text"]="0"
            self.etiqueta_Unid3["text"]="0"
            self.a3=0
            self.etiqueta_precio3["text"]="S/",self.a3
        if(self.txt8_Cod3.get())=='1':
            self.etiqueta_prod3["text"]="Linterna de baterías"
            self.etiqueta_Unid3["text"]="S/8.00"
        elif self.txt8_Cod3.get() == '2':
            self.etiqueta_prod3["text"]="Taladro"
            self.etiqueta_Unid3["text"]="S/40.00"
        elif self.txt8_Cod3.get() == '3':
            self.etiqueta_prod3["text"]="Escalera"
            self.etiqueta_Unid3["text"]="S/80.00"
        elif self.txt8_Cod3.get() == '4':
            self.etiqueta_prod3["text"]="Alicate"
            self.etiqueta_Unid3["text"]="S/12.00"
        elif self.txt8_Cod3.get() == '5':
            self.etiqueta_prod3["text"]="Martillo"
            self.etiqueta_Unid3["text"]="S/15.00"
        elif self.txt8_Cod3.get() == '6':
            self.etiqueta_prod3["text"]="Cinta métrica"
            self.etiqueta_Unid3["text"]="S/5.00"

        self.etiquetas_productos["text"]=self.etiqueta_prod1["text"]+';'+ self.etiqueta_prod2["text"]+";"+self.etiqueta_prod3["text"]


    def fprecios(self,evento):#funcion que sirve para hallar el precio de la cantidad seleccionada del primer combobox del Frame, dependiendo del producto
        cont=0
        a=int(self.txt9_Cant1.get())
        for i in range (1,a+1):
            cont+=1
        if self.txt6_Cod1.get()=='0':
            self.a1=cont*0   
            self.etiqueta_precio1["text"]="S/",self.a1 
        elif self.txt6_Cod1.get()=='1':
            self.a1=cont*8
            self.etiqueta_precio1["text"]="S/",self.a1            
        elif self.txt6_Cod1.get()=='2':
            self.a1=cont*40
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='3':
            self.a1=cont*80
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='4':
            self.a1=cont*12
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='5':
            self.a1=cont*15
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='6':
            self.a1=cont*5
            self.etiqueta_precio1["text"]="S/",self.a1

    def fprecios2(self,evento): #funcion que sirve para hallar el precio de la cantidad seleccionada del segundo combobox del Frame, dependiendo del producto   
        cont1=0
        cont=0
        b=int(self.txt10_Cant2.get())
        for i in range (1,b+1):
            cont1+=1
        # a= int(self.txt7_Cod2.get())
        # for i in range (1,a+1):
        #     cont+=1           
        if self.txt7_Cod2.get()=='0':
            self.a2=cont1*0
            self.etiqueta_precio2["text"]="S/",self.a2 
        elif self.txt7_Cod2.get()=='1':
            self.a2=cont1*8
            self.etiqueta_precio2["text"]="S/",self.a2         
        elif self.txt7_Cod2.get()=='2':
            self.a2=cont1*40
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='3':
            self.a2=cont1*80
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='4':
            self.a2=cont1*12
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='5':
            self.a2=cont1*15
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='6':
            self.a2=cont1*5
            self.etiqueta_precio2["text"]="S/",self.a2
            
    def fprecios3(self,evento): #funcion que sirve para hallar el precio de la cantidad seleccionada del tercer combobox del Frame, dependiendo del producto 
        cont1=0
        b=int(self.txt11_Cant3.get())
        for i in range (1,b+1):
            cont1+=1 
        if self.txt8_Cod3.get()=='0':
            self.a3=cont1*0
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='1':
            self.a3=cont1*8
            self.etiqueta_precio3["text"]="S/",self.a3     
        elif self.txt8_Cod3.get()=='2':
            self.a3=cont1*40
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='3':
            self.a3=cont1*80
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='4':
            self.a3=cont1*12
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='5':
            self.a3=cont1*15
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='6':
            self.a3=cont1*5
            self.etiqueta_precio3["text"]="S/",self.a3 

        # if self.txt9_Cant1.get() == '2':
        #     self.etiqueta_precio1["text"]="S/16.00"
        

    def total(self):#una vez llenado los datos con los combobox hallaremos la suma total de los 3 combobox creados
        
            
        suma=self.a1+self.a2+self.a3
        self.preciototal=self.etiqueta_total["text"]="S/",suma
        
        
    def ver_registros(self):#creamos una funcion para crear una tabla con los datos de la base de datos
        #una vez seleccionado el boton "registrar" creamos una nueva ventana con la funcion (Toplevel)
        self.edit_wind=Toplevel()
        self.frame6=Frame(self.edit_wind,width=850,height=300,bg="#C4E4D5")
        self.frame6.pack(expand=True,fill='both')
        
        self.frame5=Frame(self.frame6,bg="#C4E4D5")
        self.frame5.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.96)

        #creamos la tabla donde colocarremos los datos con la base de datos
        self.tree = ttk.Treeview(self.frame5,height=11, columns=("Id","DNI","Apellidos","Nombres","Dirección","Teléfono","Pedidos","Cantidad","Total"), selectmode = "browse" )
        
        #creamos cada columna de la tabla y le nombramos un nombre y una posicion
        self.tree.heading("#1", text="Id", anchor=CENTER)
        self.tree.heading("#2", text="DNI", anchor=CENTER)
        self.tree.heading("#3", text="Apellidos", anchor=CENTER)
        self.tree.heading("#4", text="Nombres", anchor=CENTER)
        self.tree.heading("#5", text="Dirección", anchor=CENTER)
        self.tree.heading("#6", text="Teléfono", anchor=CENTER)
        self.tree.heading("#7", text="Pedidos", anchor=CENTER)
        self.tree.heading("#8", text="Cantidad", anchor=CENTER)
        self.tree.heading("#9", text="Total", anchor=CENTER)

        
        self.tree.place(relx=0,rely=0.02,width=815,height=257)#la posicion donde la se coloca la tabla
       
        #posiciones de cada columna creada de la tabla       
        self.tree.column("#1",minwidth=25, width = 25, stretch=NO)
        self.tree.column("#2",minwidth=55, width = 55, stretch=NO)
        self.tree.column("#3", minwidth =85, width = 85, stretch=NO)
        self.tree.column("#4", minwidth=85, width = 85, stretch=NO)
        self.tree.column("#5", minwidth=100, width=130, stretch=NO)
        self.tree.column("#6", minwidth=70, width=70, stretch=NO)
        self.tree.column("#7", minwidth=150, width=245, stretch=NO)
        self.tree.column("#8", minwidth=60, width=60, stretch=NO)
        self.tree.column("#9", minwidth=60, width=60, stretch=NO)
        self.tree.column("#0", minwidth=0, width=0, stretch=NO)
        #boton de eliminar fila
        ttk.Button(self.frame5,text='ELIMINAR DATOS',command=self.delete_product).place(relx=0.45,rely=0.91,width=150)

        #llenando las filas de la tabla
        self.get_products()

       

    def run_query(self,query,parameters = ()):#funcion donde conectamos nuestros datos a la base de datos
       with sqlite3.connect(self.db_name) as conn:
         cursor= conn.cursor() 
         result= cursor.execute(query,parameters)
         conn.commit()
       return result     

    def get_products(self):
        #limpiando la tabla
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #consultando los datos
        query='SELECT * FROM product ORDER BY Id ASC'
        db_rows=self.run_query(query)
        index=iid=0
        #rellenando los datos
        for row in db_rows:
           self.tree.insert("",index, iid, values=row)      
           index = iid = index  +1

    def validacion(self):#validar si todos los datos fueron añadidos
        return (len(self.txt1_DNI.get()) !=0 and len(self.txt2_Apellidos.get()) !=0 and len(self.txt3_Nombres.get()) != 0 and len(self.txt4_Direccion.get()) !=0
                and len(self.txt5_Telf.get()) !=0 and len(self.etiqueta_total["text"] ) !=0)
    def add_datos(self):#agregar datos
        if self.validacion():
           query= 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
           self.cantidad_Total["text"]=self.txt9_Cant1.get()+','+self.txt10_Cant2.get()+','+self.txt11_Cant3.get()
           parameters=(self.txt1_DNI.get(),self.txt2_Apellidos.get(),self.txt3_Nombres.get(),self.txt4_Direccion.get()
                    ,self.txt5_Telf.get(),self.etiquetas_productos["text"],self.cantidad_Total["text"],self.etiqueta_total["text"])
           self.run_query(query, parameters)
           messagebox.showinfo(title="Listo!!",message="Datos guardados exitosamente :)")
           #una vez resgistrado los datos y el producto limpiamos todos los datos 
           self.txt1_DNI.delete(0, END)
           self.txt2_Apellidos.delete(0, END)
           self.txt3_Nombres.delete(0, END)
           self.txt4_Direccion.delete(0, END)
           self.txt5_Telf.delete(0, END)
           
           
           self.etiqueta_total["text"]=""


        else:
            messagebox.showinfo(title="Falta datos que llenar",message="ERROR!!\nEs obligatorio llenar todas las casillas verifique")
        self.get_products()

    def delete_product(self):#eliminar fila seleccionada
        
        
        try:
            str(self.tree.item(self.tree.selection())['values'][0])
        except IndexError as e:
            messagebox.showinfo(title="Error",message="ERROR!!\nPor favor seleccione una fila")
            return  
        Nombres=str(self.tree.item(self.tree.selection())['values'][0])
        query='DELETE FROM product WHERE  Id = ?'
        self.run_query(query, (Nombres, ))
        messagebox.showinfo(title=":)",message="Listo!! el usuario con el ID: {} \n Fue eliminado exitosamente".format(Nombres))
        
        self.get_products() 

    def crear_widgets(self):#esta funcion es donde creamos todos los buttons, frames, labels,combobox,le damos color, etc de nuestra ventana principal
        #creando el frame de la parte superior
        frame2=Frame(self,bg="#C4E4D5")
        frame2.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.54)
        #creando el frame de la parte inferior
        frame3=Frame(self,bg="#E6EFB8")
        frame3.place(relx=0.02,rely=0.58,relwidth=0.96,relheight=0.40)

        #dando estilos o tipo de letra a nuestros labels
        my_font=Font(family="Time New Roman",size=14,weight="bold",slant="italic")
        my_font2=Font(family="Time New Roman",size=9,weight="bold",slant="roman")


        #creando cajas de texto a nuestra ventana principal superior
        self.txt1_DNI=Entry(frame2,width=8,borderwidth=3)
        self.txt1_DNI.place(relx=0.18,rely=0.15)
        self.txt2_Apellidos=Entry(frame2,width=14,borderwidth=3)
        self.txt2_Apellidos.place(relx=0.18,rely=0.31)
        self.txt3_Nombres=Entry(frame2,width=14,borderwidth=3)
        self.txt3_Nombres.place(relx=0.65,rely=0.31)
        self.txt4_Direccion=Entry(frame2,width=50,borderwidth=3)
        self.txt4_Direccion.place(relx=0.18,rely=0.48)
        self. txt5_Telf=Entry(frame2,width=50,borderwidth=3)
        self.txt5_Telf.place(relx=0.18,rely=0.65)

        #creando los labels a nuestra ventana principal superior
        Label(frame2,text="Ferretería el Tornillo Feliz",font=my_font,fg="black",bg="#C4E4D5").pack()        
        Label(frame2,text="DNI",font=my_font2,bg="#C4E4D5").place(relx=0.08,rely=0.16)
        Label(frame2,text="Apellidos",font=my_font2, bg="#C4E4D5").place(relx=0.04,rely=0.32)
        Label(frame2,text="Nombres",font=my_font2, bg="#C4E4D5").place(relx=0.5,rely=0.32)
        Label(frame2,text="Dirección",font=my_font2, bg="#C4E4D5").place(relx=0.04,rely=0.49)
        Label(frame2,text="Teléfono",font=my_font2, bg="#C4E4D5").place(relx=0.04,rely=0.66)
    
        #creando los labels a nuestra ventana principal inferior   
        Label(frame3,text="Cod_Prod",font=my_font2, bg="#E6EFB8").place(relx=0)
        Label(frame3,text="Descripción",font=my_font2, bg="#E6EFB8").place(relx=0.21)       
        Label(frame3,text="Unidad",font=my_font2, bg="#E6EFB8").place(relx=0.42)
        Label(frame3,text="Cantidad",font=my_font2, bg="#E6EFB8").place(relx=0.53)
        Label(frame3,text="Precio",font=my_font2, bg="#E6EFB8").place(relx=0.67) 
        Label(frame3,text="Subtotal",font=my_font2, bg="#E6EFB8").place(relx=0.76)

    #creando 6 combobox posicionandolos y colocando a la ventana principal inferior
        #creando 3 combobox para elegir el codigo del producto
        self.opciones=["0","1","2","3","4","5","6"]#coloncando los datos que elegir a nuestro combobox
        self.txt6_Cod1=Combobox(frame3,width=4,values=self.opciones,state="readonly")
        self.txt6_Cod1.place(relx=0.02,rely=0.18) 
        self.txt6_Cod1.bind("<<ComboboxSelected>>", self.Productos,self.fprecios)
        self.txt6_Cod1.current(0)

        self.txt7_Cod2=Combobox(frame3,width=4,values=self.opciones,state="readonly")
        self.txt7_Cod2.place(relx=0.02,rely=0.38)
        self.txt7_Cod2.bind("<<ComboboxSelected>>", self.Productos,self.fprecios2)
        self.txt7_Cod2.current(0)

        self.txt8_Cod3=Combobox(frame3,width=4,values=self.opciones,state="readonly")
        self.txt8_Cod3.place(relx=0.02,rely=0.58)
        self.txt8_Cod3.bind("<<ComboboxSelected>>", self.Productos,self.fprecios3)
        self.txt8_Cod3.current(0)

        #creando 3 combobox para elegir el cantidad seleccionada 

        a=0
        self.opciones1=[]
        for i in range(1,101):#con este ciclo FOR colocamos la cantidad de elementos del 1 al 100 a nuestro combobox y tambien nos ahorramos bastantes lineas de codigo
            a+=1
            self.opciones1+=[a]

        self.txt9_Cant1=Combobox(frame3,width=3,values=self.opciones1,state="readonly")
        self.txt9_Cant1.place(relx=0.55,rely=0.18)
        self.txt9_Cant1.bind("<<ComboboxSelected>>", self.fprecios)
        
        self.txt10_Cant2=Combobox(frame3,width=3,values=self.opciones1,state="readonly")
        self.txt10_Cant2.place(relx=0.55,rely=0.38)
        self.txt10_Cant2.bind("<<ComboboxSelected>>", self.fprecios2)

        self.txt11_Cant3=Combobox(frame3,width=3,values=self.opciones1,state="readonly")
        self.txt11_Cant3.place(relx=0.55,rely=0.58)
        self.txt11_Cant3.bind("<<ComboboxSelected>>", self.fprecios3)

    #creando etiquetas o labels para luego colocar los valores seleccionados al costado de los 6 combobox de la ventana inferior
        #estas 3 etiquetas son para darle nombre a los productos que eligio en los 3 primeros combobox de la ventana inferior 
        self.etiqueta_prod1=Label(frame3,bg="#E6EFB8")
        self.etiqueta_prod1.place(relx=0.18,rely=0.18)
        self.etiqueta_prod2=Label(frame3,bg="#E6EFB8")
        self.etiqueta_prod2.place(relx=0.18,rely=0.38)
        self.etiqueta_prod3=Label(frame3,bg="#E6EFB8")
        self.etiqueta_prod3.place(relx=0.18,rely=0.58)

        #estas 3 etiquetas son para darle el precio por unidad a los productos que eligio en los 3 primeros combobox de la ventana inferior 
        self.etiqueta_Unid1=Label(frame3,bg="#E6EFB8")
        self.etiqueta_Unid1.place(relx=0.42,rely=0.18)
        self.etiqueta_Unid2=Label(frame3,bg="#E6EFB8")
        self.etiqueta_Unid2.place(relx=0.42,rely=0.38)
        self.etiqueta_Unid3=Label(frame3,bg="#E6EFB8")
        self.etiqueta_Unid3.place(relx=0.42,rely=0.58)

       #estas 3 etiquetas son para darle el precio total a pagar de cada fila a los productos que eligio en los 3 ultimos combobox de la ventana inferior 
        self.etiqueta_precio1=Label(frame3,bg="#E6EFB8")
        self.etiqueta_precio1.place(relx=0.73,rely=0.18)
        self.etiqueta_precio2=Label(frame3,bg="#E6EFB8")
        self.etiqueta_precio2.place(relx=0.73,rely=0.38)
        self.etiqueta_precio3=Label(frame3,bg="#E6EFB8")
        self.etiqueta_precio3.place(relx=0.73,rely=0.58)


        #esta etiqueta o label sirve imprimir el precio total de todos los combobox consultados  
        self.etiqueta_total=Label(frame3,text='0',width=4,bg="white")
        self.etiqueta_total.place(relx=0.73,rely=0.80)

    #creando dos etiquetas vacias para luego darles datos y obtenerlos a nuestra tabla y base de datos 
        self.etiquetas_productos=Label(frame3,text='',width=4)

        self.cantidad_Total=Label(frame3,text='')
        
        #estos son los 3 unicos botones que colacaremos en nuestra ventana principal luego le daremos su funcion con el "command"
        self.btn1_Stotal=Button(frame3,text="Total",command=self.total)
        self.btn1_Stotal.place(relx=0.89,rely=0.8)

        self.btn1_Registro=Button(frame3,text="Registrar",command=self.add_datos)
        self.btn1_Registro.place(relx=0.41,rely=0.8)

        self.btn1_VerRegistro=Button(frame3,text="Ver Registro",command=self.ver_registros)
        self.btn1_VerRegistro.place(rely=0.8)
      
#esta es la funcion principal donde creamos la ventana principal y dandole nombre(title) a nuestro programa y para poder ejecutar nuestro programa principal :)
if __name__=='__main__':
        ventana=Tk()
        ventana.wm_title("Ferreteria el tornillo feliz")
        app=Miventana(ventana)
        app.mainloop()
 



