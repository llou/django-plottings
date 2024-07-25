import matplotlib.pyplot as plt


def plotter_function(data, **kwargs):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    return fig
