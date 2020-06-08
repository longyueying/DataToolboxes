import os
import shutil


def path_generator(txt_path,
                   source_annotations_path,
                   source_images_path,
                   target_annotations_path,
                   target_images_path,
                   rm_origin_path=False):
    if os.path.exists(target_annotations_path):
        if rm_origin_path:
            shutil.rmtree(target_annotations_path)
            os.makedirs(target_annotations_path)
    else:
        os.makedirs(target_annotations_path)
    if os.path.exists(target_images_path):
        if rm_origin_path:
            shutil.rmtree(target_images_path)
            os.makedirs(target_images_path)
    else:
        os.makedirs(target_images_path)
    with open(txt_path, "r") as f:
        for line in f.readlines():
            if os.path.exists(os.path.join(source_annotations_path, line.strip()) + ".xml"):
                source_xml_path = os.path.join(source_annotations_path, line.strip()) + ".xml"
                target_xml_path = os.path.join(target_annotations_path, line.strip()) + ".xml"
            else:
                print("{} not exists!".format(os.path.join(source_annotations_path, line.strip()) + ".xml"))
            if os.path.exists(os.path.join(source_images_path, line.strip()) + ".jpg"):
                source_image_path = os.path.join(source_images_path, line.strip()) + ".jpg"
                target_image_path = os.path.join(target_images_path, line.strip()) + ".jpg"
            else:
                print("{} not exists!".format(os.path.join(source_images_path, line.strip()) + ".jpg"))
            yield source_xml_path, source_image_path, target_xml_path, target_image_path


def unit_test_path_generator():
    txt_path = "results/class_select_result.txt"
    source_annotations_path = "E:/Data/biandian/2019-biandian-1936/Annotations"
    source_images_path = "E:/Data/biandian/2019-biandian-1936/JPEGImages"
    target_annotations_path = "../tmp/Annotations"
    target_images_path = "../tmp/JPEGImages"
    for source_xml_path, source_image_path, target_xml_path, target_image_path \
            in path_generator(txt_path, source_annotations_path, source_images_path, target_annotations_path, target_images_path):
        print(source_xml_path)
        print(source_image_path)
        print(target_xml_path)
        print(target_image_path)


def cp_files(txt_path, source_annotations_path, source_images_path, target_annotations_path, target_images_path):
    for source_xml_path, source_image_path, target_xml_path, target_image_path \
            in path_generator(txt_path, source_annotations_path, source_images_path, target_annotations_path, target_images_path):
        print("copying {} and {}".format(source_image_path, source_xml_path))
        shutil.copy(source_xml_path, target_xml_path)
        shutil.copy(source_image_path, target_image_path)


def delete_files(txt_path, source_annotations_path, source_images_path):
    for source_xml_path, source_image_path, target_xml_path, target_image_path \
            in path_generator(txt_path, source_annotations_path, source_images_path, "./", "./"):
        print("copying {} and {}".format(source_image_path, source_xml_path))
        os.remove(source_xml_path)
        os.remove(source_image_path)


if __name__ == "__main__":
    unit_test_path_generator()
