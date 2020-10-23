from ola.ClientWrapper import ClientWrapper
from gpiozero import OutputDevice

u0 = 1
g0 = 17
o17 = OutputDevice(g0, initial_value=None)
o04 = OutputDevice(g1, initial_value=None)

def print_data(data):
  d510 = data[509]
  if d510 > 127:
    o17.on()
    print("==aan==\n\n{}\n".format(data))
  else:
    o17.off()
    print("type: {}\ndata[510]: {}".format(type(d510), d510))
    print("\nuit\n")

w0 = ClientWrapper()
c0 = w0.Client()
c0.RegisterUniverse(u0, c0.REGISTER, print_data)

w0.Run()
