import os
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def plot_progress(df, n_rows, title, xaxis, yaxis, xlabel, ylabel, legend=True, fig_fp=None):
    assert type(yaxis) is list, "xaxis should be list type"

    df = df.loc[:n_rows]
    plt.figure(figsize=(7, 4))

    for y in yaxis:
        plt.plot(df.loc[:n_rows, xaxis], df.loc[:n_rows, y], label=y)

    if title is not None:
        plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if legend:
        plt.legend(loc="lower right")

    if fig_fp is None:
        fig_fp = os.path.join(os.path.dirname(__file__), "output", "training_progress.png")
        
    # plt.savefig(fig_fp)
    # print("file saved to ", fig_fp)
    plt.savefig(fig_fp.replace(".png", ".pgf"))
    print("file saved to ", fig_fp.replace(".png", ".pgf"))


if __name__ == "__main__":
    from pathlib import Path
    save_dir = os.path.join(os.path.dirname(__file__), "output", "training_progress")
    Path(save_dir).mkdir(exist_ok=True, parents=True)

    # df = pd.read_csv("data/5_1_1_backbone_overall.csv")
    # fig_fp = os.path.join(save_dir, "BackboneSelection.png")
    # plot_progress(df, n_rows=80, title=None, xaxis='epoch', yaxis=['VC_Vision', 'VC_Proj', 'IC'], xlabel='Epoch', ylabel='mAP', fig_fp=fig_fp)

    # df = pd.read_csv("data/AblationVC.csv")
    # fig_fp = os.path.join(save_dir, "AblationVC.png")
    # plot_progress(df, n_rows=70, title=None, xaxis='epoch', yaxis=["VC_Vision", "VC_Proj", "IC", "VC_AT", "VC_DF"], xlabel='Epoch', ylabel='mAP', fig_fp=fig_fp)

    for segment in ['0_overall', '1_head', '2_middle', '3_tail']:
        df = pd.read_csv("data/4_4_finalscore_" + segment + ".csv")
        fig_fp = os.path.join(save_dir, "4_4_finalscore_" + segment + ".png")
        plot_progress(df, n_rows=40, title=None, xaxis='epoch', yaxis=['IC', 'AFRICAN-AR'], xlabel='Epoch', ylabel='mAP', fig_fp=fig_fp)

    # df = pd.read_csv("data/AFRICANPretraining.csv")
    # fig_fp = os.path.join(save_dir, "AFRICANPretraining.png")
    # plot_progress(df, n_rows=50, title=None, xaxis='epoch', yaxis=["Accuracy"], xlabel='Epoch', ylabel='Accuracy', legend=False, fig_fp=fig_fp)

    # df = pd.read_csv("data/VCBatchSize.csv")
    # fig_fp = os.path.join(save_dir, "7_1_VCBatchSize.png")
    # plot_progress(df, n_rows=40, title=None, xaxis='epoch', yaxis=['VC_AT_bs16', 'VC_AT_bs128'], xlabel='Epoch', ylabel='mAP', fig_fp=fig_fp)


# BackboneSelection
# 0.717222095	0.462386876	0.594823718
# 0.638031185	0.372524142	0.549261451
# 0.490725666	0.199986771	0.460274875
# 0.543613255	0.271938115	0.498190284

# 0	Head	Middle	Tail	Overall
# VC_Vision	0.462386876	0.372524142	0.199986771	0.271938115
# VC_Proj	0.594823718	0.549261451	0.460274875	0.498190284
# IC	0.717222095	0.638031185	0.490725666	0.543613255