import psutil
import pyudev

class USBBackend:
    def __init__(self):
        self.has_pyudev = False
        try:
            import pyudev
            self.has_pyudev = True
        except ImportError:
            pass

    def detect_usb_devices(self):
        appareils_usb = []

        for partition in psutil.disk_partitions():
            if 'removable' in partition.opts:
                appareils_usb.append(partition.device)

        if self.has_pyudev:
            context = pyudev.Context()
            for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
                if 'ID_BUS' in device and device['ID_BUS'] == 'usb':
                    appareils_usb.append(device.device_node)

        return appareils_usb