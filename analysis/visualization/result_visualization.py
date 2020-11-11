import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# metric visualization
def metric_with_label_quantity(label_quantity_file='../../result/label_analysis.txt',
                               metric_result_file='../../result/eval_result.csv'):
    label_names = []
    label_quantities = []
    recalls = []
    aps = []
    with open(label_quantity_file) as f:
        for line in f.readlines():
            label_name, label_quantity = line.strip().split(',')
            label_names.append(label_name)
            label_quantities.append(int(label_quantity))
    # 根据标签数量排序
    label_names = np.asarray(label_names)
    label_quantities = np.asarray(label_quantities)
    label_index = np.argsort(-label_quantities)
    label_names = label_names[label_index]
    label_quantities = label_quantities[label_index]
    # 读入metric结果
    df_metric = pd.read_csv(metric_result_file)
    for label_name in label_names:
        recalls.extend(df_metric.loc[df_metric['class'] == label_name]['recall'].values)
        aps.extend(df_metric.loc[df_metric['class'] == label_name]['ap'].values)

    fig, ax1 = plt.subplots(figsize=(9, 6))

    plt.gcf().subplots_adjust(bottom=0.2)
    # plt.ylim(0, 2000)
    plt.xticks(rotation=90)
    ax1.plot(label_names, label_quantities, marker='.')

    ax2 = ax1.twinx()
    ax2.plot(label_names, aps, ls='--', c="#F44336")
    plt.show()


def metric_with_label_size():
    pass


# loss visualization


if __name__ == "__main__":
    metric_with_label_quantity()