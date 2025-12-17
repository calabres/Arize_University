# Arize_University

Prerrequisitos
Antes de empezar, asegúrate de tener instalado:

Google Antigravity (El IDE).

GitHub CLI (gh): Es la herramienta de línea de comandos de GitHub. Si no la tienes, descárgala aquí.

PowerShell (si estás en Windows) o tu terminal favorita.

Paso 1: Iniciar sesión en GitHub desde la terminal
Abre tu terminal (PowerShell o CMD) y ejecuta el siguiente comando para conectar tu cuenta:

PowerShell

gh auth login
Selecciona GitHub.com.

Elige SSH como protocolo preferido.

Sigue los pasos para autorizar en el navegador.

Paso 2: Crear el Codespace (Tu computadora en la nube)
Ahora vamos a crear el entorno remoto para tu repositorio. En la terminal escribe:

PowerShell

gh codespace create -r TuUsuario/TuRepositorio
(Reemplaza TuUsuario/TuRepositorio por el nombre real, por ejemplo juanperez/mi-proyecto-antigravity).

Elige la rama (branch) por defecto (usualmente main o master).

Espera unos segundos a que se configure.

Paso 3: Configurar el acceso SSH (El paso clave del video)
Antigravity necesita una "dirección" para conectarse. GitHub CLI puede generar esta configuración automáticamente.

Primero, lista tus codespaces para ver el nombre del que acabas de crear:

PowerShell

gh codespace list
(Anota el nombre raro que te da, por ejemplo: automatic-goggles-xp9r).

Ahora, inyecta la configuración SSH en tu archivo de sistema:

PowerShell

gh codespace ssh --config > ~/.ssh/config
Nota: Si estás en Windows y este comando te da error, puedes hacerlo manualmente copiando el output de gh codespace ssh --config y pegándolo en tu archivo C:\Users\TuUsuario\.ssh\config.

Paso 4: Conectar Antigravity al Codespace
Aquí es donde ocurre la magia:

Abre Google Antigravity.

Busca el icono de Remote Explorer (Explorador Remoto) en la barra lateral o presiona F1 y escribe Remote-SSH: Connect to Host.

Deberías ver una lista de servidores. Selecciona el que tiene el nombre de tu codespace (ej. codespaces-auto-...).

Antigravity abrirá una nueva ventana, instalará un pequeño servidor en el codespace y ¡listo!

Ahora verás los archivos de tu repositorio GitHub en el explorador de archivos de Antigravity, pero todo el código se estará ejecutando en la nube de GitHub, tal como en el video.

¿Solo quieres clonar el repositorio localmente?
Si todo esto te parece muy complicado y solo quieres trabajar en tu PC sin usar la nube (Codespaces), el proceso es mucho más simple:

Abre Antigravity.

Presiona Ctrl + Shift + P (o F1).

Escribe Git: Clone.

Pega la URL de tu repositorio (https://github.com/TuUsuario/TuRepo.git).

Elige una carpeta en tu PC y listo.



Ve a tu perfil de GitHub en el navegador (github.com/calabres) y revisa el nombre exacto del repositorio.

Si se llama Arize_University (con 'y'), el comando correcto es:

PowerShell

gh codespace create -R calabres/Arize_University




El error HTTP 403: Must have admin rights to Repository tiene una causa un poco confusa, pero la pista real está en la segunda parte del mensaje:

"This API operation needs the 'codespace' scope."

Esto significa que cuando te logueaste con gh auth login, no le diste permiso a la herramienta para crear Codespaces.

Solución: Refrescar los permisos
Copia y pega el comando exacto que te sugiere el error en tu terminal:

PowerShell

gh auth refresh -h github.com -s codespace
Al ejecutarlo, te pedirá que vuelvas a autenticarte (probablemente abriendo el navegador).

Esta vez, en la pantalla de autorización de GitHub, asegúrate de que estás concediendo permisos para Codespaces.

Una vez completado, vuelve a intentar crear el codespace:

PowerShell

gh codespace create -R calabres/Arize_University
(Nota: Asegúrate de que el repositorio calabres/Arize_University realmente existe en tu cuenta. Si es un fork, debería funcionar sin problemas una vez actualices los permisos).


Ahora solo falta el "puente" para que Antigravity pueda entrar a esa computadora. Sigue estos pasos exactos en tu PowerShell:

Paso 1: Obtener la configuración de acceso
Ejecuta este comando para ver los datos de conexión:

PowerShell

gh codespace ssh --config
Esto te imprimirá un bloque de texto que empieza con Host codespaces-auto-... y tiene varias líneas debajo (User, HostName, IdentityFile, etc.). Copia todo ese bloque de texto.

Paso 2: Guardar la configuración en tu PC
Necesitamos pegar ese texto en tu archivo de configuración SSH de Windows.

En la misma terminal, escribe esto para abrir el archivo con el Bloc de notas (o VS Code si prefieres):

PowerShell

notepad C:\Users\user\.ssh\config
(Si te dice que el archivo no existe, crea un archivo nuevo en blanco en esa ruta).

Pega el texto que copiaste en el Paso 1 al final del archivo.

Guarda y cierra el Bloc de notas.

Paso 3: Conectar Antigravity
Ahora sí, la parte final:

Abre Google Antigravity.

Presiona F1 (o Ctrl + Shift + P) para abrir la paleta de comandos.

Escribe y selecciona: Remote-SSH: Connect to Host...

Debería aparecerte en la lista una opción que dice algo como: codespaces-auto-jubilant-memory-jr9ggv5x9qgcq64p... (Si no aparece, selecciona "Configure SSH Hosts", elige tu archivo config, y vuelve a intentar conectar).

Dale clic. Se abrirá una ventana nueva, instalará el servidor remoto (tardará unos segundos) y verás que abajo a la izquierda dice "SSH: codespaces...".

¡Listo! Estarás usando Antigravity en tu PC, pero todo el código y la ejecución estarán ocurriendo en el servidor de GitHub.


OPEN FOLDER WORKSPACE/Arize_University