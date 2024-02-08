import bluetooth

service_matches = bluetooth.find_service(address='MAC주소입력')

if len(service_matches) == 0:
    print("No services found")
    exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))

# print every return value
print("name: %s" % (first_match["name"]))
print("host: %s" % (first_match["host"]))
print("description: %s" % (first_match["description"]))
print("provider: %s" % (first_match["provider"]))
print("protocol: %s" % (first_match["protocol"]))
print("port: %s" % (first_match["port"]))
print("service-classes: %s" % (first_match["service-classes"]))
print("profiles: %s" % (first_match["profiles"]))
print("service-id: %s" % (first_match["service-id"]))

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("bluetooth socket created")
sock.connect((host, port))
print("connect()...")

sock.send("Hello World!")
print("message sent")

sock.close()
