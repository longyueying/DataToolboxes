from tqdm import tqdm
from analysis.data.image_analysis import get_image_number
from utils.image_util import image_path_generator
import os


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


if __name__ == "__main__":
    image_rename(["E:/Data/yiwu/shudian/daodixian_yw_1/JPEGImages"])