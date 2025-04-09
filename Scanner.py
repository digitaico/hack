import bluetooth
from constants import PHONE_BRANDS, SPEAKER_BRANDS, SPEAKER_KEYWORDS

class Scanner:
    def __init__(self, adapter=0):
        self.adapter = adapter
        self.phone_brands = PHONE_BRANDS
        self.speaker_brands = SPEAKER_BRANDS
        self.speaker_keywords = SPEAKER_KEYWORDS

    def scan_for_devices(self, major_device_class):

        devices = []
        device_type_name = ""
        if major_device_class == 2:
            device_type_name = "mobile phones"
        elif major_device_class == 4:
            device_type_name = "Bluetooth speakers"
        else:
            device_type_name = f"devices with major class 0x{major_device_class:02x}"

        try:
            nearby_devices = bluetooth.discover_devices(duration=20, lookup_names=True, lookup_class=True, device_id=adapter)
            print(f"Scaneando {device_type_name} usando adaptador {adapter}...")

            for device_info in nearby_devices:
                addr = device_info[0]
                device_class_str = device_info[1]
                name = ""
                is_target_device = False 

                if len(device_info) > 2:
                    name = device_info[2]

                try:
                    device_class_int = int(device_class_str, 16) #convertir el hex string a int.
                    detected_major_class = (device_class_int >> 8) & 0xFF

                    if detected_major_class == major_device_class:
                        devices.append(addr)
                        print(f"Encontre {device_type_name.rstrip('s')} -Clase: 0x{detected_major_class:02x}): {name} - {addr}")
                        is_target_device = True
                    elif major_device_class == 2:
                        device_class_lower = device_class_str.lower()
                        for brand in self.phone_brands:
                            if brand in device_class_lower:
                                devices.append(addr)
                                is_target_device = True
                                print(f"Encontre telefono por nombre: '{brand}': {name} - {addr}")
                                break # if found no need to continue loop through the brands list
                    elif major_device_class == 4:
                        device_class_lower = device_class_str.lower()
                        for brand in self.speaker_brands:
                            if brand in device_class_lower:
                                devices.append(addr)
                                is_target_device = True
                                print(f"Encontre Parlante Bluetooth por nombre: '{brand}': {name} - {addr}")
                                break # if found no need to continue loop through the brands list
                            else: # check si no es igual a marca
                                for keyword in self.speaker_brands:
                                    if keyword in device_class_lower:
                                        devices.append(addr)
                                        print(f"Encontre Parlante Bluetooth por keywords contiene '{keyword}': {name} - {addr}")
                                        is_target_device = True
                                        break

                except ValueError:
                    device_class_lower = device_class_str.lower()
                    if major_device_class == 2:
                        for brand in self.phone_brands:
                            if brand in device_class_lower:
                                devices.append(addr)
                                is_target_device = True
                                print(f"Encontre telefono por nombre: '{brand}': {name} - {addr}")
                                break # if found no need to continue loop through the brands list
                    elif major_device_class == 4:
                        for brand in self.speaker_brands:
                            if brand in device_class_lower:
                                devices.append(addr)
                                is_target_device = True
                                print(f"Encontre Parlante Bluetooth por nombre: '{brand}': {name} - {addr}")
                                break # if found no need to continue loop through the brands list
                            else:
                                for keyword in self.speaker_brands:
                                    if keyword in device_class_lower:
                                        devices.append(addr)
                                        print(f"Encontre Parlante Bluetooth por keywords contiene '{keyword}': {name} - {addr}")
                                        is_target_device = True
                                        break

                    print(f"Warning: No pude convertir la clase '{device_class_str}' a INT para {name} - {addr}.")
                    print(f"Valor recibido como device class: '{device_class_str}'")

                if not is_target_device:
                    print(f"Encontre clase -no {device_type_name.rstrip('s')}: {name} -{addr} Class: '{device_class_str}'")

        except bluetooth.BluetoothError as e:
            print(f"F**k! Ocurrio un error durante el scanneo Bluetooth: {e}")
            print("Porbablemente se requiera usar `root` privilegios. SUDO! mi negto!!")
            print("Revisa que Bluetooth este activado y que el adaptador este UP.")

        print(f"Devices {devices}")
        return devices

