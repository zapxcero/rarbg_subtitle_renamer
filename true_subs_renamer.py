import os
from pathlib import Path

path = os.getcwd()

keywords = ['RARBG', '1080P', 'BLURAY', 'REMASTERED', 'x265']


def check_keywords(folder):
    for key in keywords:
        if key in folder:
            return True


for folder in os.listdir(path):
    try:
        if os.path.isdir(folder) and check_keywords(folder):
            filepath = Path.cwd() / folder / 'Subs'
            filename = os.listdir(filepath)
            filepath = Path.cwd() / folder / 'Subs' / filename[0]
            movie_name = folder + '.srt'
            filepath.rename(Path.cwd() / folder / movie_name)
            filepath = Path.cwd() / folder / 'Subs'
            filepath.rmdir()
            print(f'Renaming subtitles for {folder}')
        else:
            continue
    except:
        pass
    # take all files out and move it up one directory
    # rename .srt files

input('Press ENTER to exit')
