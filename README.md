# Bluetooth Deauthor

This package uses your local machine `bluetooth` tools to scan and find Bluetooth Speakers and __deauthorize__ or break the 
communication with any device that is feeding music to it. 

It uses Major Device Class as argument to define which type of device: 2 for mobile phone, 4 for Bluetooth Audio devices like 
speakers.  First it scans and returns a list of devices MAC addresses.  Then to each MAC performs a flood attack.

## Installation

Being a python package,t shall be installed with `pip`.


```bash
pip install bluetooth_deauther-0.1.7.tar.gz
```

## Use

```bash
sudo python3 -n Deauther <Major Device Class 2 || 4>
```

Created by @digitaico.
