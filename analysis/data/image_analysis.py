from utils.image_util import image_path_generator
from utils.image_util import image_md5
from tqdm import tqdm
import os
import json


def get_image_number(root_path_list):
    root_path_list = root_path_list.copy()
    return sum(1 for _, _ in image_path_generator(root_path_list))


def dup_hash(root_path_list):
    length = get_image_number(root_path_list)
    hash_dict = {}
    print("正在计算图片哈希值……")
    for path, filename in tqdm(image_path_generator(root_path_list), total=length):
        img_path = os.path.join(path, filename)
        img_hash = image_md5(img_path)
        hash_dict.setdefault(img_hash, [])
        hash_dict[img_hash].append(img_path)
    with open("../../result/dup_hash.json", "w") as f:
        json.dump(hash_dict, f, indent=4)
    print("总共{}张图片，去重后图片数量为{}".format(length, len(hash_dict)))


if __name__ == "__main__":
    # print(get_image_number(["E:/Data/shudian/201912-wuhan"]))
    dup_hash(["E:/Data/shudian/wgs_5-7"])
