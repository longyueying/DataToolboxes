import os
import shutil


txt_path = "./results/class_select_result.txt"
source_annotations_path = "D:/biandian/Annotations"
source_images_path = "D:/biandian/JPEGImages"
target_annotations_path = "../tmp/Annotations"
target_images_path = "../tmp/JPEGImages"

if os.path.exists(target_annotations_path):
    shutil.rmtree(target_annotations_path)
os.makedirs(target_annotations_path)
if os.path.exists(target_images_path):
    shutil.rmtree(target_images_path)
os.makedirs(target_images_path)
with open(txt_path, "r") as f:
    for line in f.readlines():
        if os.path.exists(os.path.join(source_annotations_path, line.strip()) + ".xml"):
            source_file_path = os.path.join(source_annotations_path, line.strip()) + ".xml"
            target_file_path = os.path.join(target_annotations_path, line.strip()) + ".xml"
            shutil.copy(source_file_path, target_file_path)
        else:
            print("{} not exists!".format(os.path.join(source_annotations_path, line.strip()) + ".xml"))
        if os.path.exists(os.path.join(source_images_path, line.strip()) + ".jpg"):
            source_file_path = os.path.join(source_images_path, line.strip()) + ".jpg"
            target_file_path = os.path.join(target_images_path, line.strip()) + ".jpg"
            shutil.copy(source_file_path, target_file_path)
        else:
            print("{} not exists!".format(os.path.join(source_images_path, line.strip()) + ".jpg"))

