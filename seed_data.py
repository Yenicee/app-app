from ejemplo.models import Familiar

Familiar(nombre="Yenice", direccion="General Paz 677", numero_pasaporte=122343).save()
Familiar(nombre="Ivan", direccion="Av del Prado 3874", numero_pasaporte=8965120).save()
Familiar(nombre="Liliana", direccion="San la Quinta 85", numero_pasaporte=359345).save()
Familiar(nombre="Martha", direccion="San Lorenzo 74", numero_pasaporte=567309).save()
Familiar(nombre="Dardo", direccion="Av Buen Senior 456", numero_pasaporte=75663524).save()

print("Se cargo con éxito los usuarios de pruebas")