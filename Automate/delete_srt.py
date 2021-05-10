#!python3
# -*- coding: utf-8 -*-
import os
# import send2trash
# from mutagen.mp4 import MP4
import zipfile


def deleteSRT(path, delete=False):
    os.chdir(path)
    for folder in os.listdir():
        try:
            os.chdir(folder)
        except NotADirectoryError as err:
            print(err)
            continue
        for f in os.listdir():
            if f.endswith('.srt') or f.endswith('.vtt') or f.endswith('.url') or f.endswith('.html'):
                print(f)
                try:
                    if delete:
                        os.remove(f)
                except Exception as err:
                    print(err)
                    continue
        os.chdir("..")

def unzipFiles(path):
    os.chdir(path)
    for folder in os.listdir():
        try:
            os.chdir(folder)
        except NotADirectoryError as err:
            print(err)
            continue
        for file in os.listdir():
            if file.endswith(".zip"):
                print("deleting: {}".format(file))
                os.remove(file)
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(file[:-8])
        os.chdir("..")

def renameBullshit(path):
    os.chdir(path)
    for folder in listdir(): 
        try:
            os.chdir(folder)    
        except NotADirectoryError:
            continue

        for file in listdir():
            if "--- [ FreeCourseWeb.com ] ---" in file:
                name, extension = file[:-33], file.split(".")[-1]
                name = "{}.{}".format(name, extension)
                print(name)
                os.rename(file, name)
        os.chdir("..")

def countTimeOfVideos(path):
    os.chdir(path)
    a = 0
    count = 0
    for section in os.listdir(".")[:2]:
        os.chdir(section)
        print(section)

        for file in os.listdir("."):
            if file.endswith(".mp4"):
                print("\t" + file)
                try:
                    audio = MP4(file)
                    a += audio.info.length
                    count += 1
                except Exception as e:
                    pass
        os.chdir("..")

    print("MP4 files: {}".format(count))
    print("Duration: {}h/{}m/{}s".format(
        a//3600, 
        (a-a//3600*3600)//60,
        round(a-(a-a//3600*3600)//60-a//3600*3600)
    ))

if __name__=="__main__":
    location = "/mnt/700fb3dd-e744-44eb-9443-b95947712511/Udemy/Spring"
    deleteSRT(path=location, delete=True)