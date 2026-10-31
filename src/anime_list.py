import os
import subprocess

anime_folder = os.listdir("animes")
anime_list = []

def open_video_file():
    #gostou da referencia ne vadia
    final_destination = os.path.join(selected_path, option)
    subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe", final_destination])

for i in anime_folder:
    anime_list.append(i)

while True:
    option = input("Qual pasta gostaria de abrir? (digite Sair para sair)")
    if option in anime_list:
        selected_path = os.path.join("animes", option)
        print(os.listdir(selected_path))
        selected_path_files = os.listdir(selected_path)

        option = input("qual ep gostaria de assistir")
        option = option.replace(" ","")
        if option in selected_path_files:
            open_video_file()
    elif option == "Sair":
        break

#print(anime_list)
#print(os.listdir("animes"))