import os


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
    for path, name in image_path_generator(root_path_list):
        if '.JPG' in name or '.JPEG' in name or '.jpeg' in name:
            file_path = os.path.join(path, name)
            file_path_rename = file_path.replace(".JPG", ".jpg").replace('.JPEG', '.jpg').replace('.jpeg', '.jpg')
            os.rename(file_path, file_path_rename)
