from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ciclo( models.Model ):
    nombre              =   models.CharField ( max_length=140 )
    abreviatura         =   models.CharField ( max_length=10 )
    nivel_profesional   =   models.IntegerField()
    def __str__(self ):
        return self.abreviatura
    
    class Meta:
        db_table="ciclos"

class Curso( models.Model ):
    num_curso           = models.IntegerField()
    nombre_curso        = models.CharField ( max_length = 20 )
    ciclo               = models.ForeignKey ( Ciclo )
    def __str__(self):
        return self.nombre_curso
    class Meta:
        db_table="cursos"
        
class Grupo ( models.Model ):
    nombre_grupo    =   models.CharField(max_length=15)
    curso           =   models.ForeignKey ( Curso )
    class Meta:
        db_table="grupos"
        
        
class EspecialidadProfesor ( models.Model ):
    ESPECIALIDADES = [ ("PS", "Prof. Secundaria"),
                        ("PT", "Prof. Tecnico") ]
    especialidad = models.CharField ( max_length = 30, choices = ESPECIALIDADES )
    def __str__(self):
        return self.especialidad
    class Meta:
        db_table="especialidesprofesorado"
        verbose_name_plural = "Especialidades"


class Profesor ( models.Model ):
    nombre = models.CharField( max_length = 20 )
    horas_minimas = models.IntegerField()
    num_posicion=models.IntegerField()
    especialidad = models.ForeignKey ( EspecialidadProfesor )
    def to_java(self):
        inicializacion_java="""
        Profesor m{0} = new Profesor({0}, {1}, {2},\"{3}\", \"{4}\")""".format(self.id, self.nombre, self.horas_minimas)
        return inicializacion_java
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ["num_posicion"]
        db_table="profesores"
        verbose_name_plural = "Profesores"
        
class Modulo( models.Model ):
    nombre          =   models.CharField ( max_length=140 )
    codigo_junta    =   models.IntegerField()
    horas_anuales   =   models.IntegerField()
    horas_semanales =   models.IntegerField()
    curso           =   models.ForeignKey(Curso)
    especialidad    =   models.CharField(max_length=10)
    def __str__(self ):
        return self.nombre + "("+ str(self.curso) + ")"
    
    def to_java(self, nombre_vector,indice):
        inicializacion_java="""
        Modulo m{0} = new Modulo({0}, {1}, {2},\"{3}\", \"{4}\");""".format(self.id, self.codigo_junta, self.horas_semanales, self.nombre,str(self.curso))
        inicializacion_java+="\n\t\t{0}[{1}]=m{2}".format(nombre_vector, indice, self.id)
        return inicializacion_java.strip()
        
    class Meta:
        db_table="modulos"
        verbose_name_plural = "Modulos"
        ordering = ["nombre", "curso"]

class Reparto ( models.Model ):
    nombre  =   models.CharField( max_length= 20)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Repartos"
    
class ModulosAsignados ( models.Model ):
    reparto     =   models.ForeignKey ( Reparto )
    modulo      =   models.ForeignKey ( Modulo )
    profesor    =   models.ForeignKey ( Profesor )
    
class ModulosNoAsignados ( models.Model ):
    reparto     =   models.ForeignKey ( Reparto )
    modulo      =   models.ForeignKey ( Modulo )
    