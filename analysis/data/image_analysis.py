from utils.image_util import image_path_generator


def get_image_number(root_path_list):
    root_path_list = root_path_list.copy()
    return sum(1 for _, _ in image_path_generator(root_path_list))


if __name__ == "__main__":
    print(get_image_number(["E:/Data/shudian/201912-wuhan"]))
