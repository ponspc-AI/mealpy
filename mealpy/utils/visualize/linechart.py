#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 17:12, 09/07/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import platform
from matplotlib import pyplot as plt
from numpy import arange


LIST_LINESTYLES = [
    '-',        # solid line style
    '--',       # dashed line style
    '-.',       # dash-dot line style
    ':',        # point marker
    's',        # square marker
    '*',        # star marker
    'p',        # pentagon marker
    '+',        # plus marker
    'x',        # x marker
    'd',        # thin diamond marker
]

LIST_COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']


def _draw_line_(data=None, title=None, linestyle='-', color='b', x_label="#Iteration", y_label="Function Value",
                     filename=None, exts=(".png", ".pdf"), verbose=True):
    x = arange(0, len(data))
    y = data
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, linestyle=linestyle, color=color,)
    plt.legend()  # show a legend on the plot
    if filename is not None:
        for idx, ext in enumerate(exts):
            plt.savefig(f"./{filename}{ext}", bbox_inches='tight')
    if platform.system() != "Linux" and verbose:
        plt.show()
    plt.close()


def _draw_multi_line_(data=None, title=None, list_legends=None, list_styles=None, list_colors=None,
                      x_label="#Iteration", y_label="Function Value", filename=None, exts=(".png", ".pdf"), verbose=True):
    x = arange(0, len(data[0]))
    for idx, y in enumerate(data):
        plt.plot(x, y, label=list_legends[idx], markerfacecolor=list_colors[idx], linestyle=list_styles[idx])

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()  # show a legend on the plot
    if filename is not None:
        for idx, ext in enumerate(exts):
            plt.savefig(f"./{filename}{ext}", bbox_inches='tight')
    if platform.system() != "Linux" and verbose:
        plt.show()
    plt.close()


def _draw_multi_line_in_same_figure_(data=None, title=None, list_legends=None, list_styles=None, list_colors=None,
                                     x_label="#Iteration", y_label="Objective", filename=None, exts=(".png", ".pdf"), verbose=True):
    n_lines = len(data)
    len_lines = len(data[0])
    x = arange(0, len_lines)

    if n_lines == 1:
        fig, ax = plt.subplots()
        if list_legends is None:
            ax.plot(x, data[0])
        else:
            ax.plot(x, data[0], label=list_legends[0])
        ax.set_title(title)
    elif n_lines > 1:
        fig, ax_list = plt.subplots(n_lines, sharex=True)
        fig.suptitle(title)
        for idx, ax in enumerate(ax_list):
            if list_legends is None:
                ax.plot(x, data[idx], markerfacecolor=list_colors[idx], linestyle=list_styles[idx])
            else:
                ax.plot(x, data[idx], label=list_legends[idx], markerfacecolor=list_colors[idx], linestyle=list_styles[idx])
            ax.set_ylabel(f"Objective {idx + 1}")
            if idx == (n_lines - 1):
                ax.set_xlabel(x_label)


    if filename is not None:
        for idx, ext in enumerate(exts):
            plt.savefig(f"./{filename}{ext}", bbox_inches='tight')
    if platform.system() != "Linux" and verbose:
        plt.show()
    plt.close()



def export_convergence_chart(data=None, title="Convergence Chart", linestyle='-', color='b', x_label="#Iteration",
                       y_label="Function Value", filename="convergence_chart", exts=(".png", ".pdf"), verbose=True):
    _draw_line_(data, title=title, linestyle=linestyle, color=color, x_label=x_label, y_label=y_label,
                    filename=filename, exts=exts, verbose=verbose)


def export_explore_exploit_chart(data=None, title="Exploration vs Exploitation Percentages", list_legends=("Exploration %", "Exploitation %"),
                                 list_styles=('-', '-'), list_colors=('blue', 'orange'), x_label="#Iteration", y_label="Percentage",
                                 filename="explore_exploit_chart", exts=(".png", ".pdf"), verbose=True):
    _draw_multi_line_(data=data, title=title, list_legends=list_legends, list_styles=list_styles, list_colors=list_colors,
                      x_label=x_label, y_label=y_label, filename=filename, exts=exts, verbose=verbose)


def export_diversity_chart(data=None, title='Diversity Measurement Chart', list_legends=None,
                           list_styles=None, list_colors=None, x_label="#Iteration", y_label="Diversity Measurement",
                           filename="diversity_chart", exts=(".png", ".pdf"), verbose=True):
    if list_styles is None:
        list_styles = LIST_LINESTYLES[:len(data)]
    if list_colors is None:
        list_colors = LIST_COLORS[:len(data)]
    _draw_multi_line_(data=data, title=title, list_legends=list_legends, list_styles=list_styles, list_colors=list_colors,
                      x_label=x_label, y_label=y_label, filename=filename, exts=exts, verbose=verbose)


def export_objectives_chart(data=None, title="Objectives chart", list_legends=None, list_styles=None, list_colors=None,
            x_label="#Iteration", y_label="Function Value", filename="Objective-chart", exts=(".png", ".pdf"), verbose=True):
    if list_styles is None:
        list_styles = LIST_LINESTYLES[:len(data)]
    if list_colors is None:
        list_colors = LIST_COLORS[:len(data)]
    _draw_multi_line_in_same_figure_(data=data, title=title, list_legends=list_legends, list_styles=list_styles, list_colors=list_colors,
                                     x_label=x_label, y_label=y_label, filename=filename, exts=exts, verbose=verbose)


def export_trajectory_chart(data=None, title="Trajectory of some first agents after generations", list_legends=None,
                                 list_styles=None, list_colors=None, x_label="#Iteration", y_label="X1",
                                 filename="1d_trajectory", exts=(".png", ".pdf"), verbose=True):
    if list_styles is None:
        list_styles = LIST_LINESTYLES[:len(data)]
    if list_colors is None:
        list_colors = LIST_COLORS[:len(data)]
    _draw_multi_line_(data=data, title=title, list_legends=list_legends, list_styles=list_styles, list_colors=list_colors,
                      x_label=x_label, y_label=y_label, filename=filename, exts=exts, verbose=verbose)











