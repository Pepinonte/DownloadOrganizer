import shutil, os

rep = os.listdir("C:/Users/GROS Christian/Downloads")

if not os.path.exists('C:/Users/GROS Christian/Downloads/EXECUTABLES'):
    os.makedirs('C:/Users/GROS Christian/Downloads/EXECUTABLES')
if not os.path.exists('C:/Users/GROS Christian/Downloads/PDF'):
    os.makedirs('C:/Users/GROS Christian/Downloads/PDF')
if not os.path.exists('C:/Users/GROS Christian/Downloads/COMPRESSES'):
    os.makedirs('C:/Users/GROS Christian/Downloads/COMPRESSES')
if not os.path.exists('C:/Users/GROS Christian/Downloads/TORRENTS'):
    os.makedirs('C:/Users/GROS Christian/Downloads/TORRENTS')

for fichier in rep:
    if fichier.endswith(".exe") or fichier.endswith(".msi"):
        print(fichier)
        path = "C:/Users/GROS Christian/Downloads/" + fichier
        shutil.move(path, 'C:/Users/GROS Christian/Downloads/EXECUTABLES')
    elif fichier.endswith(".pdf"):
      print(fichier)
      path = "C:/Users/GROS Christian/Downloads/" + fichier
      shutil.move(path, 'C:/Users/GROS Christian/Downloads/PDF')
    elif fichier.endswith(".zip") or fichier.endswith(".rar"):
      print(fichier)
      path = "C:/Users/GROS Christian/Downloads/" + fichier
      shutil.move(path, 'C:/Users/GROS Christian/Downloads/COMPRESSES')
    elif fichier.endswith(".torrent"):
      print(fichier)
      path = "C:/Users/GROS Christian/Downloads/" + fichier
      shutil.move(path, 'C:/Users/GROS Christian/Downloads/TORRENTS')
