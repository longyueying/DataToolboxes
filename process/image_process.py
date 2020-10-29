from tqdm import tqdm
from analysis.data.image_analysis import get_image_number
from utils.image_util import image_path_generator
import os
from PIL import ImageFile
import piexif
from PIL import Image


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


def rm_orientation(root_path_list):
    length = get_image_number(root_path_list)
    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        image_path = os.path.join(path, name)
        img = Image.open(image_path)
        if "exif" in img.info:
            exif_dict = piexif.load(img.info["exif"])
            if piexif.ImageIFD.Orientation in exif_dict['0th']:
                print(image_path)
                orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
                exif_dict['Exif'][41729] = b'1'
                exif_bytes = piexif.dump(exif_dict)
                img.save(image_path, exif=exif_bytes)


if __name__ == "__main__":
    image_rename(["E:/测试数据/shudian/test_niaocao_tonghang/JPEGImages"])