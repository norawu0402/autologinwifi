import netifaces

for device in netifaces.interfaces():
	if 'wl' in device:
		print(device)