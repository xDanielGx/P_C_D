import wx
import random

# Definimos un diccionario con jugadores, roles y habilidades
jugadores = {
    "Lancelot": {"nombre": "Lancelot", "rol": "Caballero", "habilidades": ["Espada Sagrada", "Escudo Divino", "Valor"]},
    "Merlín": {"nombre": "Merlín", "rol": "Mago", "habilidades": ["Hechicería Arcana", "Teletransportación", "Sabiduría"]},
    "Arya": {"nombre": "Arya", "rol": "Asesina", "habilidades": ["Sigilo", "Veneno Mortal", "Agilidad"]}
}

# Escenarios y opciones de decisión
escenarios = {
    "1": {"descripcion": "Te encuentras en un bosque oscuro. ¿Qué haces?",
          "opciones": {"1": "Explorar el bosque", "2": "Buscar un camino conocido"}},
    "2": {"descripcion": "Al explorar el bosque, encuentras una cueva misteriosa. ¿Entras?",
          "opciones": {"1": "Entrar a la cueva", "2": "Continuar explorando el bosque"}},
    "3": {"descripcion": "Dentro de la cueva, ves una luz brillante al final. ¿Te acercas?",
          "opciones": {"1": "Acercarme a la luz", "2": "Volver atrás"}},
    "4": {"descripcion": "Al acercarte a la luz, descubres un tesoro brillante. ¿Lo tomas?",
          "opciones": {"1": "Tomar el tesoro", "2": "Dejarlo y salir de la cueva"}}
}

class Ventana(wx.Frame):

    def __init__(self, *args, **kw):
        super(Ventana, self).__init__(*args, **kw)
        self.panel = wx.Panel(self)
        self.boton1 = wx.Button(self.panel, label="Mostrar datos")
        self.boton2 = wx.Button(self.panel, label="Tomar decisión")
        self.combo = wx.ComboBox(self.panel, choices=list(jugadores.keys()), style=wx.CB_READONLY)
        self.Bind(wx.EVT_BUTTON, self.mostrar_datos, self.boton1)
        self.Bind(wx.EVT_BUTTON, self.tomar_decision, self.boton2)
        self.Bind(wx.EVT_COMBOBOX, self.seleccionar_jugador, self.combo)
        self.jugadores_seleccionados = []

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.combo, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.boton1, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.boton2, 0, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizer(sizer)

    def seleccionar_jugador(self, evento):
        jugador_seleccionado = self.combo.GetValue()
        if jugador_seleccionado not in self.jugadores_seleccionados:
            self.jugadores_seleccionados.append(jugador_seleccionado)

    def mostrar_datos(self, evento):
        jugador = jugadores.get(self.combo.GetValue())
        if jugador:
            habilidades = "\n".join(jugador["habilidades"])
            mensaje = f"Nombre: {jugador['nombre']}\nRol: {jugador['rol']}\nHabilidades:\n{habilidades}"
            wx.MessageBox(mensaje, "Datos del jugador")
        else:
            wx.MessageBox("Por favor, seleccione un jugador", "Error")

    def tomar_decision(self, evento):
        if not self.jugadores_seleccionados:
            wx.MessageBox("Por favor, seleccione al menos un jugador", "Error")
            return
        escenario_actual = "1"
        while escenario_actual in escenarios:
            escenario = escenarios[escenario_actual]
            opciones = "\n".join([f"{key}: {value}" for key, value in escenario["opciones"].items()])
            decision = wx.GetTextFromUser(f"{escenario['descripcion']}\n\n{opciones}\n\nElige una opción:", "Toma de decisiones")
            if decision in escenario["opciones"]:
                escenario_actual = decision
            else:
                wx.MessageBox("Opción inválida", "Error")
        wx.MessageBox("Fin de la aventura", "Fin")

aplicacion = wx.App()
frm = Ventana(None, title='Prueba')
frm.Show()
aplicacion.MainLoop()