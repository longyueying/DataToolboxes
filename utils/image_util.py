import os
from tqdm import tqdm
from analysis.data.image_analysis import get_image_number


def image_path_generator(root_path_list):
    """
    :param root_path_list:
    :return: path of  image and name of image
    """
    path_queue = root_path_list.copy()
    # traverse root path
    while path_queue:
        current_path = path_queue.pop(0)
        for item in os.listdir(current_path):
            current_name = item
            item = os.path.join(current_path, item)
            if os.path.isdir(item):
                path_queue.append(item)
            elif item.split('.')[-1].lower() in ['png', 'jpg', 'jpeg']:
                yield current_path, current_name


def image_rename(root_path_list):
    length = get_image_number(root_path_list)
    rename_file_number = 0

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        if '.JPG' in name or '.JPEG' in name or '.jpeg' in name:
            rename_file_number += 1
            file_path = os.path.join(path, name)
            file_path_rename = file_path.replace(".JPG", ".jpg").replace('.JPEG', '.jpg').replace('.jpeg', '.jpg')
            os.rename(file_path, file_path_rename)

    print("There are {}/{} images have be renamed".format(rename_file_number, length))
