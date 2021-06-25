#Control de versiones: una forma que se usa para ir registrando cuáles son los cambios que se hacen en un programa.
#Sigue los cambios que se van haciendo dentro de un archivo.
# A cada "foto" del texto le pone información (metadatos) que después me permiten rastrear esa "foto".
#"Foto" = commit = registro de qué había en el archivo en un momento dado y qué se cambió--> git commit.
    #Especificar qué cambios hice en el archivo --> agregar un mensarje sobre los cambios que hice.
#"Stage"= estado intermedio donde está los cambios pero todavía no fueron registrados --> git add.
#Para subir los cambios a la nube, se usa git push.
#Para bajar los cambios de la nube a mi dispositivo, se usa git pull.

#Pasos a seguir en una consola de Bash:

#Para subir archivos a la nube...
git config ==global user.name "MaiaNaidich" #esto se hace una sola vez para linkear tu computadora con tu usuario de GitHub.
git config ==global user.email "manaidich@gmail.com"
#Abrir terminal de Bash en la carpeta donde queremos trabajar.
git clone https://github.com/MaiaNaidich/UCEMA_Teoria_Fundamentos_de_Informatica.git #o el link al repositorio que quiera.
code. #para abrir Visual Code y poder editar la carpeta/repositorio clonado.
#Crear/editar el archivo que quiera.
#Al lado del nombre del archivo aparece una "U" que indica que el archivo fue editado pero que esos cambios todavía no se subieron a la nube.
#De nuevo en la terminal de Bash, hago un ls para asegurarme de estar trabajando sobre el mismo archivo.
git add.
git commit -m "mensaje que nos permita saber qué cambios hicimos y qué hay en esta versión del archivo"
#Hasta acá estoy trabaajndo localmente en mi máquina, por eso ahora hay que empujar los cambios a la nube.
git push
#Te pide tu usuario y contraseña de GitHub para poder subir los cambios.

#Para bajarse los cambios que hizo otro en el repositorio...
git pull #describe todos los cambios que se hicieron.