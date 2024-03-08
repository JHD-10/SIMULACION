import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GeneradorCuadradosMedios:
    def __init__(self, semilla, digitos=4):
        self.semilla = semilla
        self.digitos = digitos
        self.numeros_generados = []

    def generar(self, iteraciones):
        self.numeros_generados = []
        for _ in range(iteraciones):
            self.semilla = self.cuadrado_medio(self.semilla)
            self.numeros_generados.append(self.normalizar(self.semilla))
        return self.numeros_generados

    def cuadrado_medio(self, numero):
        cuadrado = numero ** 2
        str_numero = str(cuadrado).zfill(2 * self.digitos)
        indice_medio = self.digitos // 2
        digitos_medios = str_numero[indice_medio:-indice_medio]
        return int(digitos_medios)

    def normalizar(self, numero):
        return numero / (10 ** self.digitos)
class GeneradorProductosMedios:
    def __init__(self, semilla1, semilla2, digitos=4):
        self.semilla1 = semilla1
        self.semilla2 = semilla2
        self.digitos = digitos
        self.numeros_generados = []

    def generar(self, iteraciones):
        self.numeros_generados = []
        for _ in range(iteraciones):
            producto = self.semilla1 * self.semilla2
            producto_str = str(producto).zfill(2 * self.digitos)
            self.semilla1 = int(producto_str[:self.digitos])
            self.semilla2 = int(producto_str[self.digitos:])
            self.numeros_generados.append(self.normalizar(producto))
        return self.numeros_generados

    def normalizar(self, numero):
        return numero / (10 ** (2 * self.digitos))
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elige Algoritmo")
        self.geometry("500x500")

        # Crear botones
        boton1 = tk.Button(self, text="Algoritmo 1", command=self.abrir_ventana1)
        boton2 = tk.Button(self, text="Algoritmo 2", command=self.abrir_ventana2)
        boton3 = tk.Button(self, text="Algoritmo 3", command=self.abrir_ventana3)
        boton4 = tk.Button(self, text="Algoritmo 4", command=self.abrir_ventana4)
        boton5 = tk.Button(self, text="Algoritmo 5", command=self.abrir_ventana5)
        boton6 = tk.Button(self, text="Algoritmo 6", command=self.abrir_ventana6)

        # Posicionar botones
        boton1.place(y=0,  x=0)
        boton2.place(y=60, x=0)
        boton3.place(y=120,x=0)
        boton4.place(y=180,x=0)
        boton5.place(y=240,x=0)
        boton6.place(y=300,x=0)
        self.ban=True

    def abrir_ventana1(self):
        

        if self.ban==False:
            self.ventana_secundaria.destroy()
            self.ban=True
        self.ban=False
        self.ventana_secundaria = tk.Toplevel()
        master = self.ventana_secundaria
        master.title("Generador de Números Pseudoaleatorios - Productos Medios")

        label_semilla1 = tk.Label(master, text="Ingrese la primera semilla:")
        label_semilla1.pack()
        entry_semilla1 = tk.Entry(master)
        entry_semilla1.pack()
        label_semilla2 = tk.Label(master, text="Ingrese la segunda semilla:")
        label_semilla2.pack()

        entry_semilla2 = tk.Entry(master)
        entry_semilla2.pack()
        label_digitos = tk.Label(master, text="Ingrese la cantidad de dígitos para el cálculo:")
        label_digitos.pack()
        entry_digitos = tk.Entry(master)
        entry_digitos.pack()
        label_iteraciones = tk.Label(master, text="Ingrese la cantidad de números pseudoaleatorios a generar:")
        label_iteraciones.pack()
        entry_iteraciones = tk.Entry(master)
        entry_iteraciones.pack()
        result_label = tk.Label(master, text="")
        result_label.pack()
        def generate():
            semilla1 = int(   entry_semilla1.get())
            semilla2 = int(   entry_semilla2.get())
            digitos = int(    entry_digitos.get())
            iteraciones = int(entry_iteraciones.get())
    
            generador = GeneradorProductosMedios(semilla1=semilla1, semilla2=semilla2, digitos=digitos)
            numeros_aleatorios = generador.generar(iteraciones)
    
            result_label.config(text="Números generados: " + str(numeros_aleatorios))
        generate_button = tk.Button(master, text="Generar", command=generate)
        generate_button.pack()
    def abrir_ventana2(self):
        if self.ban==False:
            self.ventana_secundaria.destroy()
            self.ban=True
        self.ban=False
        self.ventana_secundaria = tk.Toplevel()
        master = self.ventana_secundaria
        master.title("Generador de Números Pseudoaleatorios")
        label_semilla = tk.Label(master, text="Ingrese la semilla inicial:")
        label_semilla.pack()
        entry_semilla = tk.Entry(master)
        entry_semilla.pack()
        label_digitos = tk.Label(master, text="Ingrese la cantidad de dígitos para el cálculo:")
        label_digitos.pack()
        entry_digitos = tk.Entry(master)
        entry_digitos.pack()
        label_iteraciones = tk.Label(master, text="Ingrese la cantidad de números pseudoaleatorios a generar:")
        label_iteraciones.pack()
        entry_iteraciones = tk.Entry(master)
        entry_iteraciones.pack()
        resulta_label = tk.Label(master, text="")
        resulta_label.pack()
        def generate():
            semilla = int(    entry_semilla.get())
            digitos = int(    entry_digitos.get())
            iteraciones = int(entry_iteraciones.get())
    
            generador = GeneradorCuadradosMedios(semilla=semilla, digitos=digitos)
            numeros_aleatorios = generador.generar(iteraciones)
    
            resulta_label.config(text="Números generados: " + str(numeros_aleatorios))
        generate_button = tk.Button(master, text="Generar", command=generate)
        generate_button.pack()
    def abrir_ventana3(self):
        if self.ban==False:
            self.ventana_secundaria.destroy()
            self.ban=True
        self.ban=False
        self.ventana_secundaria = tk.Toplevel()
        root=self.ventana_secundaria
        root.title("Generador de Números Pseudoaleatorios")
        
        # Crear widgets
        seed_label = tk.Label(root, text="Semilla inicial:")
        seed_entry = tk.Entry(root)
        a_label = tk.Label(root, text="Constante multiplicadora:")
        a_entry = tk.Entry(root)
        digits_label = tk.Label(root, text="Número de dígitos del centro:")
        digits_entry = tk.Entry(root)
        n_label = tk.Label(root, text="Cantidad de números a generar:")
        n_entry = tk.Entry(root)
        def generar_numeros_pseudoaleatorios():
            seed_value = int(seed_entry.get())
            constant_a = int(a_entry.get())
            num_digits_center = int(digits_entry.get())
            num_random_numbers = int(n_entry.get())
            
            random_sequence = multiplicador_constante(seed_value, constant_a, num_digits_center, num_random_numbers)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, random_sequence)

        generate_button = tk.Button(root, text="Generar", command=generar_numeros_pseudoaleatorios)
        result_text = tk.Text(root, height=10, width=40)
        
        seed_label.grid(row=0, column=0)
        seed_entry.grid(row=0, column=1)
        a_label.grid(row=1, column=0)
        a_entry.grid(row=1, column=1)
        digits_label.grid(row=2, column=0)
        digits_entry.grid(row=2, column=1)
        n_label.grid(row=3, column=0)
        n_entry.grid(row=3, column=1)
        generate_button.grid(row=4, columnspan=2)
        result_text.grid(row=5, columnspan=2)
        def multiplicador_constante(seed, a, num_digits, n):

            result = []
            xi = seed
            
            for _ in range(n):
                # Multiplicamos xi por la constante a
                xi = a * xi
                
                # Tomamos los dígitos del centro
                xi_str = str(xi)
                center_digits = xi_str[-num_digits:]
                
                # Convertimos los dígitos a un número entre 0 y 1
                ri = int(center_digits) / (10 ** num_digits)
                result.append(ri)
            
            return result


    def abrir_ventana4(self):
        if self.ban==False:
            self.ventana_secundaria.destroy()
            self.ban=True

        self.ban=False
        self.ventana_secundaria = tk.Toplevel()
        def congruencial_mixto(semilla, a, c, m, n):
            numeros = []
            for _ in range(n):
                semilla = (a * semilla + c) % m
                numeros.append(semilla)
            return numeros

        def calcular_numeros():
            a = int(a_entry.get())
            c = int(c_entry.get())
            m = int(m_entry.get())
            n = int(n_entry.get())
        
            numeros_generados = congruencial_mixto(semilla=1, a=a, c=c, m=m, n=n)
            resultado_label.config(text=f"Números generados: {numeros_generados}")
        
        # Crear ventana
        root = self.ventana_secundaria
        root.title("Generador Congruencial Mixto")
        root.geometry("400x200")
        
        # Campos de entrada
        a_label = tk.Label(root, text="Factor multiplicativo (a):")
        a_entry = tk.Entry(root)
        c_label = tk.Label(root, text="Constante aditiva (c):")
        c_entry = tk.Entry(root)
        m_label = tk.Label(root, text="Módulo (m):")
        m_entry = tk.Entry(root)
        n_label = tk.Label(root, text="Cantidad de números a generar (n):")
        n_entry = tk.Entry(root)
        
        # Botón para calcular
        calcular_button = tk.Button(root, text="Calcular", command=calcular_numeros)
        
        # Etiqueta para mostrar resultados
        resultado_label = tk.Label(root, text="")
        
        # Posicionar widgets en la ventana
        a_label.pack()
        a_entry.pack()
        c_label.pack()
        c_entry.pack()
        m_label.pack()
        m_entry.pack()
        n_label.pack()
        n_entry.pack()
        calcular_button.pack()
        resultado_label.pack()
        
    def abrir_ventana5(self):
        if self.ban==False:
            self.ventana_secundaria.destroy()
            self.ban=True
        self.ban=False
        self.ventana_secundaria = tk.Toplevel()
        def congruencial_multiplicativo(semilla, a, m, n):
            numeros = []
            for _ in range(n):
                semilla = (a * semilla) % m
                numeros.append(semilla)
            return numeros

        def calcular_numeros():
            a = int(a_entry.get())
            m = int(m_entry.get())
            n = int(n_entry.get())
        
            numeros_generados = congruencial_multiplicativo(semilla=1, a=a, m=m, n=n)
            resultado_label.config(text=f"Números generados: {numeros_generados}")
        
        # Crear ventana
        root = self.ventana_secundaria
        root.title("Generador Congruencial Multiplicativo")
        root.geometry("400x200")
        
        # Campos de entrada
        a_label = tk.Label(root, text="Factor multiplicativo (a):")
        a_entry = tk.Entry(root)
        m_label = tk.Label(root, text="Módulo (m):")
        m_entry = tk.Entry(root)
        n_label = tk.Label(root, text="Cantidad de números a generar (n):")
        n_entry = tk.Entry(root)
        
        # Botón para calcular
        calcular_button = tk.Button(root, text="Calcular", command=calcular_numeros)
        
        # Etiqueta para mostrar resultados
        resultado_label = tk.Label(root, text="")
        
        # Posicionar widgets en la ventana
        a_label.pack()
        a_entry.pack()
        m_label.pack()
        m_entry.pack()
        n_label.pack()
        n_entry.pack()
        calcular_button.pack()
        resultado_label.pack()
    def abrir_ventana6(self):
        if self.ban==False:
            self.ventana_secundaria.destroy()
            self.ban=True
        self.ban=False
        self.ventana_secundaria = tk.Toplevel()
        def congruencial_aditivo(semillas, m, n):
            numeros = []
            semillas_len = len(semillas)
            for i in range(n):
                semilla = sum([semillas[(i - j) % semillas_len] for j in range(semillas_len)]) % m
                semillas[i % semillas_len] = semilla
                numeros.append(semilla)
            return numeros
        
        def calcular_numeros():
            semillas = list(map(int, semillas_entry.get().split()))
            m = int(m_entry.get())
            n = int(n_entry.get())
        
            numeros_generados = congruencial_aditivo(semillas=semillas, m=m, n=n)
            resultado_label.config(text=f"Números generados: {numeros_generados}")
        
        # Crear ventana
        root = self.ventana_secundaria
        root.title("Generador Congruencial Aditivo")
        root.geometry("400x200")
        semillas_label = tk.Label(root, text="Semillas (separadas por espacios):")
        semillas_entry = tk.Entry(root)
        m_label = tk.Label(root, text="Módulo (m):")
        m_entry = tk.Entry(root)
        n_label = tk.Label(root, text="Cantidad de números a generar (n):")
        n_entry = tk.Entry(root)
        
        # Botón para calcular
        calcular_button = tk.Button(root, text="Calcular", command=calcular_numeros)
        
        # Etiqueta para mostrar resultados
        resultado_label = tk.Label(root, text="")
        
        # Posicionar widgets en la ventana
        semillas_label.pack()
        semillas_entry.pack()
        m_label.pack()
        m_entry.pack()
        n_label.pack()
        n_entry.pack()
        calcular_button.pack()
        resultado_label.pack()
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
