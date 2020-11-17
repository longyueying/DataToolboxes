import os
import utils.xml_util
import numpy as np


def dataset_divide(root_path_list, proportion, annotation_folder='Annotations', jpegimage_folder='JPEGImages',
                   dataset_type='mmdetection'):
    file_path_list = []
    file_name_list = []
    for path, name in utils.xml_util.xml_path_generator(root_path_list):
        annotation_path = os.path.join(path, name)
        jpegimage_path = annotation_path.replace(annotation_folder, jpegimage_folder).replace('.xml', '.jpg')
        if os.path.exists(annotation_path) and os.path.exists(jpegimage_path):
            file_path_list.append((jpegimage_path, annotation_path))
            file_name_list.append(name[:name.find('.xml')])
    total_length = len(file_name_list)
    shuffle_index = np.random.permutation(total_length)

    assert len(proportion) == 2 or len(proportion) == 3, "length of proportion must be 2 or 3"
    assert sum(proportion) == 1, "sum of proportion must equal to 1"

    train_thresh = int(total_length * proportion[0])
    train_index = shuffle_index[:train_thresh]
    val_thresh = int(total_length * (sum(proportion[:2])))
    val_index = shuffle_index[train_thresh:val_thresh]
    print(train_index)

    file_name_list_train = np.array(file_name_list)[train_index]
    file_name_list_val = np.array(file_name_list)[val_index]
    file_path_list_train = np.array(file_path_list)[train_index]
    file_path_list_val = np.array(file_path_list)[val_index]

    if len(proportion) == 3:
        test_index = shuffle_index[val_thresh:]
        file_name_list_test = np.array(file_name_list)[test_index]
        file_path_list_test = np.array(file_path_list)[test_index]

    if dataset_type == 'mmdetection':
        with open('../result/train.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(file_name_list_train))
        with open('../result/val.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(file_name_list_val))
        with open('../result/train_val.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(file_name_list_train))
            f.write('\n')
            f.write('\n'.join(file_name_list_val))
        if len(proportion) == 3:
            with open('../result/test.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(file_name_list_test))


if __name__ == "__main__":
    dataset_divide(['E:/TrainData/biandian/aqzt'], proportion=[0.9, 0.1], annotation_folder='Annotations', jpegimage_folder='JPEGImages')