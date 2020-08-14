import numpy as np
import matplotlib.pyplot as plt


class Pie:
    def __init__(self, figsize=(8, 6)):
        self.figsize = figsize

    def autopct_func(self, pct, allvals):
        # absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%".format(pct)

    def pic_for_dict(self, data):
        data = sorted(data.items(), key=lambda k: k[1], reverse=True)
        vals = [item[1] for item in data]
        ingredients = ["{:<10d}:{}".format(item[1], item[0]) for item in data]

        fig, ax = plt.subplots(figsize=self.figsize, subplot_kw=dict(aspect="equal"))
        wedges, texts, autotexts = ax.pie(vals, autopct=lambda pct: self.autopct_func(pct, vals),
                                          textprops=dict(color="w"))
        ax.legend(wedges, ingredients,
                  title="Ingredients",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        plt.setp(autotexts, size=6, weight="light")
        plt.show()