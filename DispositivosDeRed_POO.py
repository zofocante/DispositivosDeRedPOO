import random
from pyfiglet import Figlet
import time 

class Dispositivo_de_red:
    lista_formato_activos = []
    lista_formato_inactivos = []

    def __init__(self, dispositivo, ip_host, marca, modelo, estado):
        self.dispositivo = dispositivo
        self.ip_host = ip_host
        self.marca = marca
        self.modelo = modelo
        self.estado = estado
        
    def mostrar_contenido(self):
        formato = "{:18}{:18}{:18}{:18}{}".format(self.dispositivo, self.marca, self.modelo, self.ip_host, self.estado)
        
        if self.estado == "Activo":
            Dispositivo_de_red.lista_formato_activos.append(formato)
        elif self.estado == "Inactivo":
            Dispositivo_de_red.lista_formato_inactivos.append(formato) 

    @classmethod
    def mostrar_dispositivos(cls):
        if opcion == 'a':
            print("\nEsta cargando su lista [*]...\n")
            time.sleep(2)
            
            titulo_dispositivo = "{:18}{:18}{:18}{:18}{}".format('Dispositivos:', 'Marcas:','Modelos:', 'IPs:', 'Estados:')
            print(len(titulo_dispositivo)*'-')
            print(titulo_dispositivo)
            print(len(titulo_dispositivo)*'-')
            
            print('\n'.join(cls.lista_formato_activos))
            print('\n'.join(cls.lista_formato_inactivos))
        if opcion == 'b':
            print("\nEsta cargando su lista [*]...\n")
            time.sleep(2)
            
            titulo_dispositivo = "{:18}{:18}{:18}{:18}{}".format('Dispositivos:', 'Marcas:','Modelos:', 'IPs:', 'Estados:')
            print(len(titulo_dispositivo)*'-')
            print(titulo_dispositivo)
            print(len(titulo_dispositivo)*'-')
            
            print('\n'.join(cls.lista_formato_activos))
        if opcion == 'c':
            print("\nEsta cargando su lista [*]...\n")
            time.sleep(2)
            
            titulo_dispositivo = "{:18}{:18}{:18}{:18}{}".format('Dispositivos:', 'Marcas:','Modelos:', 'IPs:', 'Estados:')
            print(len(titulo_dispositivo)*'-')
            print(titulo_dispositivo)
            print(len(titulo_dispositivo)*'-')
            
            print('\n'.join(cls.lista_formato_inactivos))
            
        if opcion == 'd':
            print("\nEsta cargando su lista [*]...\n")
            time.sleep(2)
            
            texto_activos = '\n'.join(cls.lista_formato_activos) 
            texto_inactivos = '\n'.join(cls.lista_formato_inactivos)
            
            texto_activos_inactivos = texto_activos + texto_inactivos
            
            file1 = open("dispositivos_activos_inactivos.txt", 'w')
            file1.write(texto_activos_inactivos)
            print("Ya esta tu archivo descargado")


class Firewalls(Dispositivo_de_red):
    def __init__(self, ip_host, marca, modelo, estado):
        super().__init__("Firewall", ip_host, marca, modelo, estado)

class Routers(Dispositivo_de_red):
    def __init__(self, ip_host, marca, modelo, estado):
        super().__init__("Router", ip_host, marca, modelo, estado)

class Switch(Dispositivo_de_red):
    def __init__(self, ip_host, marca, modelo, estado):
        super().__init__("Switch", ip_host, marca, modelo, estado)

class Accesspoint(Dispositivo_de_red):
    def __init__(self, ip_host, marca, modelo, estado):
        super().__init__("Accesspoint", ip_host, marca, modelo, estado)

class CamaraIP(Dispositivo_de_red):
    def __init__(self, ip_host, marca, modelo, estado):
        super().__init__("CamaraIP", ip_host, marca, modelo, estado)

def mostrar_firewalls():
    rango_ip = str(random.randint(0, 255))
    ip_host = "10.0." + rango_ip + "." + rango_ip
    marcas = ["Cisco", "Fortinet", "Palo Alto", "Juniper"]
    modelos = ["ASA 5500-X", "FortiGate 60E", "PA-220", "SRX340"]
    estado = random.choice(estados)

    Firewalls(ip_host, random.choice(marcas), random.choice(modelos), estado).mostrar_contenido()

def mostrar_routers():
    rango_ip = str(random.randint(0, 255))
    ip_host = "192.168." + rango_ip + "." + "1"
    marcas =  ["Cisco", "Mikrotik", "Huawei", "Juniper"] 
    modelos = ["ISR 4321", "CRS328-24P-4S+RM", "AR1220", "MX104"]
    estado = random.choice(estados)

    Routers(ip_host, random.choice(marcas), random.choice(modelos), estado).mostrar_contenido()

def mostrar_switch():
    rango_ip = str(random.randint(0, 255))
    ip_host = "172.168." + rango_ip + "." + rango_ip
    marcas = ["Cisco", "Aruba", "Juniper", "Mikrotik"]
    modelos = ["Catalyst 2960X", "Aruba 2530-24G", "EX2300", "CRS305-1G-4S+IN"]
    estado = random.choice(estados)

    Switch(ip_host, random.choice(marcas), random.choice(modelos), estado).mostrar_contenido()

def mostrar_accesspoint():
    rango_ip = str(random.randint(0, 255))
    ip_host = "172.0." + rango_ip + "." + rango_ip
    marcas = ["Cisco", "Aruba", "Ubiquiti", "Ruckus"]
    modelos = ["Aironet 1815", " Instant On AP11", "UniFi AP AC Lite", "ZoneFlex R510"]
    estado = random.choice(estados)

    Accesspoint(ip_host, random.choice(marcas), random.choice(modelos), estado).mostrar_contenido()

def mostrar_camaraip():
    rango_ip = str(random.randint(0, 255))
    ip_host = "10.0." + rango_ip + "." + rango_ip
    marcas = ["Axis", "Hikvision", "Dahua", "Bosch"]
    modelos = ["Axis M3045-V", "DS-2CD2347G2-LU", "IPC-HFW2231T-ZS", "Flexidome 8000i"]
    estado = random.choice(estados)

    CamaraIP(ip_host, random.choice(marcas), random.choice(modelos), estado).mostrar_contenido()

estados = ["Activo", "Inactivo"]
dispositivos = ["Router", "Switch", "PC", "CamaraIP", "Laptop", "Accesspoint", "Servidor", "CamaraIP", "Tablet", "Firewall"]
marcas = ["Toshiba", "Alienware", "Dell", "HP", "ASUS", "Acer", "MSI", "Lenovo", "macbook", "razer"]
modelos = ["zx-01", "mk2", "4567", "zx-0100", "mk25", "1067", "zx-02", "mk10", "2067", "zx-03"]

while True:
    figlet = Figlet(font='slant')
    ascii_art = figlet.renderText("Network Devices")
    ascii_art_coloreado = "\033[35m" + ascii_art + "\033[32m"
    print(ascii_art_coloreado)

    titulo = "\tDISPOSITIVOS DE RED"
    print(len(titulo) * "--")
    print(titulo)
    print(len(titulo) * "--")

    opcion = input("""
TABLA de OPCIONES:

a) Lista de dispositivos activos e inactivos
b) Lista de activos
c) Lista de inactivos
d) Imprimir archivos
e) Salir

Tipear entre [a,b,c,d,e]:

>>> """)

    if opcion == 'a':
        Dispositivo_de_red.lista_formato_activos = []
        Dispositivo_de_red.lista_formato_inactivos = []
        for _ in range(10):
            rango_ip = str(random.randint(0, 255))
            ip_host = "192.168." + rango_ip + "." + rango_ip

            dispositivo = random.choice(dispositivos)
            marca = random.choice(marcas)
            modelo = random.choice(modelos)
            estado = random.choice(estados)

            if dispositivo == "Firewall":
                mostrar_firewalls()
            elif dispositivo == "Router":
                mostrar_routers()
            elif dispositivo == "Switch":
                mostrar_switch()
            elif dispositivo == "Accesspoint":
                mostrar_accesspoint()
            elif dispositivo == "CamaraIP":
                mostrar_camaraip()
            else:
                Dispositivo_de_red(dispositivo, ip_host, marca, modelo, estado).mostrar_contenido()

        Dispositivo_de_red.mostrar_dispositivos()

    elif opcion == 'b':
        Dispositivo_de_red.lista_formato_activos = []
        for _ in range(10):
            rango_ip = str(random.randint(0, 255))
            ip_host = "192.168." + rango_ip + "." + rango_ip

            dispositivo = random.choice(dispositivos)
            marca = random.choice(marcas)
            modelo = random.choice(modelos)
            estado = random.choice(estados)

            if dispositivo == "Firewall":
                mostrar_firewalls()
            elif dispositivo == "Router":
                mostrar_routers()
            elif dispositivo == "Switch":
                mostrar_switch()
            elif dispositivo == "Accesspoint":
                mostrar_accesspoint()
            elif dispositivo == "CamaraIP":
                mostrar_camaraip()
            else:
                Dispositivo_de_red(dispositivo, ip_host, marca, modelo, estado).mostrar_contenido()

        Dispositivo_de_red.mostrar_dispositivos()

    elif opcion == 'c':
        Dispositivo_de_red.lista_formato_inactivos = []
        for _ in range(10):
            rango_ip = str(random.randint(0, 255))
            ip_host = "192.168." + rango_ip + "." + rango_ip

            dispositivo = random.choice(dispositivos)
            marca = random.choice(marcas)
            modelo = random.choice(modelos)
            estado = random.choice(estados)

            if dispositivo == "Firewall":
                mostrar_firewalls()
            elif dispositivo == "Router":
                mostrar_routers()
            elif dispositivo == "Switch":
                mostrar_switch()
            elif dispositivo == "Accesspoint":
                mostrar_accesspoint()
            elif dispositivo == "CamaraIP":
                mostrar_camaraip()
            else:
                Dispositivo_de_red(dispositivo, ip_host, marca, modelo, estado).mostrar_contenido()

        Dispositivo_de_red.mostrar_dispositivos()

    elif opcion == 'd':
        Dispositivo_de_red.lista_formato_inactivos = []
        for _ in range(10):
            rango_ip = str(random.randint(0, 255))
            ip_host = "192.168." + rango_ip + "." + rango_ip

            dispositivo = random.choice(dispositivos)
            marca = random.choice(marcas)
            modelo = random.choice(modelos)
            estado = random.choice(estados)

            if dispositivo == "Firewall":
                mostrar_firewalls()
            elif dispositivo == "Router":
                mostrar_routers()
            elif dispositivo == "Switch":
                mostrar_switch()
            elif dispositivo == "Accesspoint":
                mostrar_accesspoint()
            elif dispositivo == "CamaraIP":
                mostrar_camaraip()
            else:
                Dispositivo_de_red(dispositivo, ip_host, marca, modelo, estado).mostrar_contenido()

        Dispositivo_de_red.mostrar_dispositivos()       
    
    elif opcion == 'e':
        print(f"Saliendo...[*]")
        time.sleep(2)
        break

    else: 
        print("\nError, opción inválida... Vuelve a escribir\n")