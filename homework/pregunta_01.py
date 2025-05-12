"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import matplotlib.pyplot as plt
    import pandas as pd
    import os

    output_dir = "files/plots"
    os.makedirs(output_dir, exist_ok=True)
    config = {
        "Television": {
            "color": "dimgray",
            "zorder": 1,
            "linewidth": 2
        },
        "Newspaper": {
            "color": "grey",
            "zorder": 1,
            "linewidth": 2
        },
        "Internet": {
            "color": "tab:blue",
            "zorder": 2,
            "linewidth": 4
        },
        "Radio": {
            "color": "lightgrey",
            "zorder": 1,
            "linewidth": 2
        },
    }

    df = pd.read_csv("files/input/news.csv", index_col=0)

    plt.Figure()

    for col in df.columns:
        plt.plot(
            df[col],
            label=col,
            color=config[col]["color"],
            zorder=config[col]["zorder"],
            linewidth=config[col]["linewidth"]
        )
        first_year = df.index[0]
        last_year = df.index[-1]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=config[col]["color"],
            zorder=config[col]["zorder"],
        )
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=config[col]["color"],
            zorder=config[col]["zorder"],
        )
        plt.text(
            x=first_year - 0.2,
            y=df[col][first_year],
            s=f"{col} {df[col][first_year]}%",
            ha="right",
            va="center",
            color=config[col]["color"],
        )
        plt.text(
            x=last_year + 0.2,
            y=df[col][last_year],
            s=f"{df[col][last_year]}%",
            ha="left",
            va="center",
            color=config[col]["color"],
        )
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha="center"
    )
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "news.png"))
    plt.show()


pregunta_01()
