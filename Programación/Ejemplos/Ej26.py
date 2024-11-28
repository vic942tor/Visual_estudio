# Desarrolla un programa que sugiera cursos a estudiantes basándose en sus
# intereses y en la oferta de cursos disponibles.

# Datos de entrada:
estudiantes = {
 "Luis": {"Python", "Data Science", "Machine Learning"},
 "Ana": {"Ciberseguridad", "Redes", "Python"},
 "Juan": {"Diseño", "Frontend", "React"}
}
cursos = {
 "Curso1": {"Python", "Introducción a la programación"},
 "Curso2": {"Data Science", "Estadística"},
 "Curso3": {"Ciberseguridad", "Hacking ético"},
 "Curso4": {"Frontend", "React", "JavaScript"}
}
for estudiante in estudiantes:
    curso_est = set()
    for curso in cursos:
        if estudiantes[estudiante].intersection(cursos[curso]):
            curso_est.add(curso)


