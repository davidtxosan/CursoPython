import clases

persona = clases.Persona()
persona.setNombre("david")
persona.setApellidos("sanchez")
persona.setAltura("176cm")
persona.setEdad("45 años")

print(f"la persona es : {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("javier")
informatico.setApellidos("vazquez")
informatico.setAltura("180 cm")
informatico.setEdad("55 años")

print(f"mi nombre es {informatico.nombre} {informatico.apellidos} y tengo {informatico.edad} y mido {informatico.altura}")
print(f"{informatico.programar()} y mas tarde {informatico.repararPc()}, se los siguientes lenguajes de programación: {informatico.getLenguajes()} y tengo {informatico.experiencia} años de experiencia")

print("------------------------------")

Tecnico = clases.TecnicoRedes()

print(f"se los lenguajes de programacion {Tecnico.getLenguajes()} , {Tecnico.auditarRedes} en auditar redes y ahora mismo {Tecnico.auditoria()}")
