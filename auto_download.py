import os
import subprocess
import time
import pyautogui

def search_and_download_song(song_name):
    command = f'python orpheus.py luckysearch kkbox track "{song_name}"'
    subprocess.call(command, shell=True)
    

# 获取指定路径下的文件名列表
def get_file_names(directory):
    file_names = []
    for filename in os.listdir(directory):
        if filename.endswith('.flac'):  # 假设只处理MP3文件
            file_names.append(filename)
    return file_names

# 主函数
def main():
    directory = 'D:/user/Music'  # 指定路径
    file_names = get_file_names(directory)
    
    for file_name in file_names:
        song_name = os.path.splitext(file_name)[0]  # 去除文件名的扩展名
        search_and_download_song(song_name)

if __name__ == '__main__':
    main()