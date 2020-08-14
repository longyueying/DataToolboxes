import cv2 as cv
from utils.image_util import *
from PIL import Image
from tqdm import tqdm
from analysis.data.image_analysis import get_image_number


def valid_checkup(root_path_list):
    broken_list = []
    length = get_image_number(root_path_list)

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        image_path = os.path.join(path, name)
        try:
            Image.open(image_path)
        except Exception:
            sub_root_path = path[:path.find(path.split("\\")[-1].split('/')[-1])-1]
            name = name.split('.')[0]
            broken_list.append(f'{sub_root_path},{name}')
    with open("../result/checkup_broken_images.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(broken_list))
    print("There are {}/{} images broken".format(len(broken_list), length))


if __name__ == "__main__":
    valid_checkup(["E:/训练数据/shudian/dingwei"])