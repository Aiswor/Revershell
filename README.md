# README

## English Version

### Reverse Shell

This script creates a reverse shell that connects to a remote server, allowing remote command execution on the target machine.

### Features:
1. Establishes a connection with a remote server (attacker machine).
2. Redirects input, output, and errors to the remote connection.
3. Executes commands received from the attacker machine.
4. Allows navigation through directories using `cd`.

### How to Use:

#### On the Attacker Machine:
Start a listener to receive the connection:
```bash
nc -lvnp 4444
```
Ensure the IP and port in the script match the attacker's machine.

#### On the Target Machine:
Run the script using Python:
```bash
python3 script.py
```
Once executed, the attacker will have remote shell access.

### Notes:
- Script designed for Linux systems.
- Requires Python 3.
- Use only for ethical and legal penetration testing.

---

## Versión en Español

### Shell Reversa

Este script crea una shell reversa que se conecta a un servidor remoto, permitiendo la ejecución remota de comandos en la máquina objetivo.

### Características:
1. Establece una conexión con un servidor remoto (máquina atacante).
2. Redirige la entrada, salida y errores a la conexión remota.
3. Ejecuta los comandos recibidos desde la máquina atacante.
4. Permite la navegación entre directorios usando `cd`.

### Cómo usarlo:

#### En la Máquina Atacante:
Inicia un listener para recibir la conexión:
```bash
nc -lvnp 4444
```
Asegúrate de que la IP y el puerto en el script coincidan con la máquina atacante.

#### En la Máquina Objetivo:
Ejecuta el script usando Python:
```bash
python3 script.py
```
Una vez ejecutado, el atacante tendrá acceso a la shell remota.

### Notas:
- Script diseñado para sistemas Linux.
- Requiere Python 3.
- Usar solo para pruebas de penetración éticas y legales.

