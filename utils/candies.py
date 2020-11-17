import pandas as pd
import numpy as np


def eval_reuslt_pivot(eval_result_file="../result/eval_result.csv"):
    df = pd.read_csv(eval_result_file)
    df = df.T
    # series_class = df.loc[:, 'class']
    # series_ap = df.loc[:, 'ap']
    # series_recall = df.loc[:, 'recall']
    # df_pivot = np.vstack([series_class, series_recall, series_ap])
    # df_pivot = pd.DataFrame(df_pivot)
    # df_pivot.set_index(['recall', 'ap'])
    df.to_csv("../result/eval_result_T.csv", header=False)


if __name__ == "__main__":
    eval_reuslt_pivot()