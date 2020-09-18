import os
import hashlib


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


def image_md5(image_path):
    with open(image_path, 'rb') as f:
        image_file = f.read()
        return hashlib.md5(image_file).hexdigest()


if __name__ == "__main__":
    print(image_md5("E:/Data/biandian/2019-base/JPEGImages/000001.jpg"))