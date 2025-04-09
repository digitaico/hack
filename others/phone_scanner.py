import bluetooth

def scan_for_mobile_phones(adapter=0):
    """Returns a list of MAC addresses that belong to mobile phones, based on 24bit or 6 first digits of mac address."""
    mobile_phones = []
    phone_brands =['apple', 'iphone', 'samsung', 'oppo', 'huawei', 'xiaomi', 'moto', 'motorola', 'google', 'pixel', 
                   'oneplus', 'sony', 'lg', 'alcatel', 'nokia', 'vivo', 'htc', 'honor', 'blu', 'lenovo', 'acer', 'realme', 
                   'asus', 'amazon', 'amoi', 'cat', 'blackberry', 'orange', 'prestigio', 'razer', 'sagem', 'siemens', 
                   'ericsson', 'sony ericsson', 't-mobile', 'vertu', 'zte']

    try:
        nearby_devices = bluetooth.discover_devices(duration=20, lookup_names=True, lookup_class=True, device_id=adapter)
        print(f"Encontre {len(nearby_devices)} telefonos de interes usando adaptador {adapter}.")

        for device_info in nearby_devices:
            addr = device_info[0]
            device_class_str = device_info[1]
            name = ""
            is_phone = False # flag para saber si un device ha sido identificado como telefono

            if len(device_info) > 2:
                name = device_info[2]

            try:
                device_class_int = int(device_class_str, 16) #convertir el hex string a int.
                major_device_class = (device_class_int >> 8) & 0xFF

                if major_device_class == 2: # 2 is category of phones
                    mobile_phones.append(addr)
                    print(f"Encontre telefono clase: 0x{major_device_class:02x}): {name} - {addr}")
                    is_phone = True

            except ValueError:
                print(f"Warning: No se pudo convertir la clase de dispositivo '{device_class_str}' a INT para {name}-{addr}.")
                print(f"Valor recibido como clase de dispositivo: '{device_class_str}'")

                device_class_lower = device_class_str.lower()
                for brand in phone_brands:
                    if brand in device_class_lower:
                        mobile_phones.append(addr)
                        is_phone = True
                        print(f"Encontre telefono por nombre: '{brand}': {name} - {addr}")
                        break # if found no need to continue loop through the brands list
            if not is_phone:
                print(f"No se pudo determinar tipo de dispositivo para {name} - {addr} -Clase de Dispositivo: '{device_class_str}'")

    except bluetooth.BluetoothError as e:
        print(f"F**k! Ocurrio un error durante el scanneo Bluetooth: {e}")
        print("Porbablemente se requiera usar `root` privilegios. SUDO! mi negto!!")
        print("Revisa que Bluetooth este activado y que el adaptador este UP.")

    return mobile_phones

if __name__ == "__main__":
    target_adapter = 1
    print(f"Scaneando telefonos ofensores/interes adaptador {target_adapter}...")
    #found_phones = scan_for_mobile_phones(target_adapter)
    scan_for_mobile_phones(target_adapter)
"""
    if found_phones:
        print("\nLista de MAC addresses de ofensores/interes encontrados:")
        unique_phones = list(set(found_phones))
        #print(unique_phones)
        return unique_phones
    else:
        print("\nNo se encontro ningun telefono.")
"""
