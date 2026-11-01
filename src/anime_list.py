import os
import subprocess

anime_folder = os.listdir("animes")
anime_array = []
anime_name = ""
for i in anime_folder:
    anime_array.append(i)

def open_video_file(selected_path_files, option):
    #gostou da referencia ne vadia
    final_destination = os.path.join("animes", option, selected_path_files)
    subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe", final_destination])


def scan_shi(option):
    selected_path = os.path.join("animes", option)
    print(os.listdir(selected_path))
    selected_path_files = os.listdir(selected_path)
    #print(episodes_folder)
   # if option in selected_path_files:
     #   open_video_file(option)
    return selected_path_files

#while True:
   # option = input("Qual pasta gostaria de abrir? (digite Sair para sair)")
   # if option in anime_array:

    #elif option == "Sair":
       # break

#print(anime_list)
#print(os.listdir("animes"))