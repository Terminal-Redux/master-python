import clases

persona = clases.Persona()
persona.setNombre("Amilcar")
persona.setApellidos("Gonzalez")
persona.setAltura("173cm")
persona.setEdad("27 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")
informatico.setAltura("173cm")
informatico.setEdad("27 años")

print("---------------")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("-------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())
