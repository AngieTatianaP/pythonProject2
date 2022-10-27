import hum
import pres
import temp


def sensors_init(ciudad):
    temp.run(ciudad)
    hum.run(ciudad)
    pres.run(ciudad)

if __name__ == '__main__':
    sensors_init("bogota")