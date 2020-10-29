import os
import shutil


def path_generator(txt_path, target_path, annotations_folder, images_folder, rm_origin_path=True):
    target_annotations_folder_path = os.path.join(target_path, annotations_folder)
    target_images_folder_path = os.path.join(target_path, images_folder)
    if os.path.exists(target_annotations_folder_path):
        if rm_origin_path:
            shutil.rmtree(target_annotations_folder_path)
            os.makedirs(target_annotations_folder_path)
    else:
        os.makedirs(target_annotations_folder_path)
    if os.path.exists(target_images_folder_path):
        if rm_origin_path:
            shutil.rmtree(target_images_folder_path)
            os.makedirs(target_images_folder_path)
    else:
        os.makedirs(target_images_folder_path)
    with open(txt_path, encoding='utf-8') as f:
        for line in f.readlines():
            path, name = line.strip().split(',')
            source_annotations_folder_path = os.path.join(path, annotations_folder)
            source_images_folder_path = os.path.join(path, images_folder)
            source_annotation_path = os.path.join(source_annotations_folder_path, name + '.xml')
            source_image_path = os.path.join(source_images_folder_path, name + '.jpg')
            target_annotation_path = os.path.join(target_annotations_folder_path, name+'.xml')
            target_image_path = os.path.join(target_images_folder_path, name + '.jpg')
            yield source_annotation_path, source_image_path, target_annotation_path, target_image_path


def cp_files(txt_path,
             target_path,
             annotations_folder="Annotations",
             images_folder="JPEGImages",
             rm_origin_path=True):
    for source_xml_path, source_image_path, target_xml_path, target_image_path \
            in path_generator(txt_path,
                              target_path,
                              annotations_folder,
                              images_folder,
                              rm_origin_path):
        print("copying {} and {}".format(source_image_path, source_xml_path))
        if os.path.exists(source_xml_path):
            shutil.copy(source_xml_path, target_xml_path)
        else:
            print(f'{source_xml_path} not exists')
        if os.path.exists(source_image_path):
            shutil.copy(source_image_path, target_image_path)
        else:
            print(f'{source_image_path} not exists')


def delete_files(txt_path, annotations_folder="Annotations", images_folder="JPEGImages",):
    with open(txt_path, encoding='utf-8') as f:
        for line in f.readlines():
            path, name = line.strip().split(',')
            source_annotations_folder_path = os.path.join(path, annotations_folder)
            source_images_folder_path = os.path.join(path, images_folder)
            source_annotation_path = os.path.join(source_annotations_folder_path, name+'.xml')
            source_image_path = os.path.join(source_images_folder_path, name + '.jpg')

            os.remove(source_annotation_path)
            os.remove(source_image_path)


if __name__ == "__main__":
    # delete_files("../result/checkup_broken_images.txt")
    cp_files("../result/select_by_classes.txt", "E:/daodixian-dingwei",
             annotations_folder="Annotations", images_folder="JPEGImages")
    # delete_files("../result/select_by_classes.txt")
