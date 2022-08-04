import os
import shutil


extentions_dict = {
    "winrar_extentions" : (".zip", ".rar"),
    "document_extentions" : (".pdf", ".docx", ".doc", ".txt"),
    "audio_extentions" : (".mp3") ,
    "ppt_extentions" : (".ppt", ".pptx"),
    "image_extentions" : (".eps", ".png", ".gif", ".jpg", ".jpeg", ".ai", ".raw", ".cr2", ".nef", ".orf", ".sr2"),
    "video_extentions" : (".mp4", ".mkv"),
    }



# Asks user for the directory path
path = input("Please enter the folder path you want to organise and clean: ")


# Returns a lsit of files present in the input folder with the provided file extentions
def extract_in_list(folder_path, file_extentions):
    files_list = []
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                files_list.append(file)
    return files_list


# 
for type_extentions, type_tuple in extentions_dict.items():
    files_list = extract_in_list(path, type_tuple)

    # print(files_list)
    # print()

    directory_name = type_extentions.split("_")[0] + " " + "files"
    directory_path = os.path.join(path, directory_name)

    if len(files_list):
        if os.path.exists(directory_path) == False:
            os.mkdir(directory_path)

        for file in files_list:
            old_path = os.path.join(path, file)
            new_path = os.path.join(directory_path, file)

            shutil.move(old_path, new_path)


print("Program execution successfull")
print("Check your folder for organised files")


