import subprocess

# Configuración de la conexión SSH
hostname = "localhost"
port = 22022  # Puerto que estás usando para SSH
username = "hadoop"

# Función para ejecutar comandos de manera segura
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Transferir archivo desde Windows a CentOS usando SCP
#direccion del txt de windows(editar)
local_file_path = "D:/MAIN/HadoopMapReduce/ext/noticias.txt"

#direccion del txt en centOS(editar opcional)
remote_file_path = "/home/hadoop/extraido.txt"
scp_command = f'scp -P {port} "{local_file_path}" {username}@{hostname}:{remote_file_path}'
stdout, stderr = run_command(scp_command)
print("SCP stdout:", stdout)
print("SCP stderr:", stderr)
# Nombre de la carpeta donde estara el txt de centos a hadoop (editar)
carpetaEntradaHadoop = "noticia"

#Nombre de la carpeta de salida del mapreduce de hadoop (editar siempre)
carpetaSalidaHadoop = "salida_noticias"
# Subir el archivo al sistema de archivos distribuido de Hadoop (HDFS)

hdfs_vaciar_command = f'ssh -p {port} {username}@{hostname} "hdfs dfs -rm -r -f /salida_noticias && hdfs dfs -rm -r -f /noticia/*"'
stdout, stderr = run_command(hdfs_vaciar_command)
print("HDFS vaciar stdout:", stdout)
print("HDFS vaciar stderr:", stderr)

hdfs_put_command = f'ssh -p {port} {username}@{hostname} "hdfs dfs -put {remote_file_path} /{carpetaEntradaHadoop}"'
stdout, stderr = run_command(hdfs_put_command)
print("HDFS put stdout:", stdout)
print("HDFS put stderr:", stderr)


# Cambiar directorio y ejecutar el comando Hadoop WordCount
hadoop_command = f'ssh -p {port} {username}@{hostname} "cd /opt/hadoop/hadoop-2.7.7/share/hadoop/mapreduce && hadoop jar hadoop-mapreduce-examples-2.7.7.jar wordcount /{carpetaEntradaHadoop} /{carpetaSalidaHadoop}"'
stdout, stderr = run_command(hadoop_command)
print("Hadoop stdout:", stdout)
print("Hadoop stderr:", stderr)


# Descargar el archivo de salida de Hadoop desde HDFS a la máquina CentOS
hdfs_get_command = f'ssh -p {port} {username}@{hostname} "cd /opt/hadoop/hadoop-2.7.7/share/hadoop/mapreduce && rm -r part-r-00000 && hdfs dfs -get /{carpetaSalidaHadoop}/part-r-00000 "'
stdout, stderr = run_command(hdfs_get_command)
print("HDFS get stdout:", stdout)
print("HDFS get stderr:", stderr)

# Descargar el archivo de resultado desde CentOS a Windows
usuario = "adrian"
windowsIp = "192.168.56.1"
#direccion de la carpeta donde se guardara el txt en windows (editar)
ubicacionWindows = "D:/MAIN/HadoopMapReduce/ext"
scp_command = f'ssh -p {port} {username}@{hostname} "cd /opt/hadoop/hadoop-2.7.7/share/hadoop/mapreduce &&  scp  part-r-00000 {usuario}@{windowsIp}:{ubicacionWindows}" '
stdout, stderr = run_command(scp_command)
print("SCP stdout:", stdout)
print("SCP stderr:", stderr)
#cd /opt/hadoop/hadoop-2.7.7/share/hadoop/mapreduce

#correr el programa de encontrar palabra mas frecuente
stdout, stderr = run_command(f"python {ubicacionWindows}/encontrar_palabra_mas_frecuente.py")
print("Python stdout:", stdout)