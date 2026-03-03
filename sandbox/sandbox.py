# create a class named "Device"
# method is_implant return true if object instance has it's implant field as Y


class Device:
    def __init__(
        self,
        fda_product_code,
        product_code_name,
        regulation_number,
        device_regulatory_class,
        life_sustaining,
        implant,
    ):
        self.fda_product_code = fda_product_code
        self.product_code_name = product_code_name
        self.regulation_number = regulation_number
        self.device_regulatory_class = device_regulatory_class
        self.life_sustaining = life_sustaining
        self.implant = implant

    def is_implant(self):
        if self.implant == "Y":
            return True
        if self.implant == "N":
            return False


# read file from 'devices.txt'
# create a list [] of device objects and read


# open file
# read the file -> returns list of strings (including header)
f = open("devices.txt", "r")
header = f.readline()  # reads header, advances cursor
init_devices = f.readlines()  # rest of the lines after header
f.close()

devices = []  # list of Device objects

# loop list of init devices
for device in init_devices:
    # create a Device
    # remove newline, split by comma
    device_fields = device.strip().split(",")

    # spread the list of device fields into the params of Device class
    # append new device to the devices list

    new_device = Device(
        fda_product_code=device_fields[0],
        product_code_name=device_fields[1],
        regulation_number=device_fields[2],
        device_regulatory_class=device_fields[3],
        life_sustaining=device_fields[4],
        implant=device_fields[5],
    )
    # NOTE: alternatively use unpacking '*'
    # new_device = Device(*device_fields)

    devices.append(new_device)
    # test device
    print(new_device.is_implant())

# add third device
devices.append(Device("BTL", "VENTILATOR", "868.5925", "2", "Y", "N"))

# create a new file 'three_devices.txt'
with open("three_devices.txt", "w") as f:
    f.write(f"{header}")  # headers
    for device in devices:  # device is an object
        f.write(
            f"{device.fda_product_code},{device.product_code_name},{device.regulation_number},{device.device_regulatory_class},{device.life_sustaining},{device.implant}\n"
        )
