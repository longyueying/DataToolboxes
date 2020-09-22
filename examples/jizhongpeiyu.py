import shutil
import os
import pandas as pd
import numpy as np
from utils.image_util import image_path_generator


def mv_xml():
    root_path = "E:/Data/shudian/wgs_5-7"
    target_root_path = "E:/jizhongpeiyu_anno/"
    target_folder_signature = "ganta"
    path_stack = [root_path]

    while len(path_stack) > 0:
        current_path = path_stack.pop()
        for item in os.listdir(current_path):
            tmp = os.path.join(current_path, item)
            if os.path.isdir(tmp):
                if target_folder_signature in tmp:
                    ind = tmp.find("wgs_5-7")
                    target_path = target_root_path + tmp[ind:-4]
                    os.makedirs(target_path)
                    print(target_path)
                    shutil.move(tmp, target_path)
                else:
                    path_stack.append(tmp)


def jzpy_stastic():
    df = pd.read_csv('./label_dict.csv', index_col=None, encoding="GBK", dtype=str)
    df['number'] = np.zeros(df.shape[0])
    df['code'] = df['code'].astype(str)
    code_array = np.asarray(df['code'])
    with open("./data.txt") as f:
        for line in f.readlines():
            fault_name, fault_num = line.strip().split(":")
            if fault_name in code_array:
                df.loc[df["code"] == fault_name, "number"] = fault_num
            else:
                print(fault_name)

    df.to_csv("./result.csv", index=None)


if __name__ == "__main__":
    # img_count()
    mv_xml()