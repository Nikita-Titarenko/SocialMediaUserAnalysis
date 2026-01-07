import os
import seaborn as sns
import matplotlib.pyplot as plt

def build_corr(df, columns, columns_title, title, output_dir):
    corr = df[columns].corr()
    corr.columns = columns_title
    corr.index = columns_title

    f = plt.figure(figsize=(8,6), num=title)
    sns.heatmap(corr)
    plt.tight_layout()
    plt.title(title, y=1.05)
    save_figure(f, output_dir, title)
    plt.close(f)

def build_lmplot(df, x, y, output_dir):
    for x_column in x:
        for y_column in y:
            title = f'Relationship {x_column} vs {y_column}'
            g = sns.lmplot(
                data=df,
                x=x_column,
                y=y_column,
                scatter_kws={'alpha':0.1, 's':10},
                line_kws={'color': 'red'})
            g.figure.suptitle(title, y=1.05)
            g.figure.canvas.manager.set_window_title(title)
            plt.tight_layout()
            save_figure(g.figure, output_dir, title)
            plt.close(g.figure)

def save_figure(f, output_dir, title):
    f.savefig(
        os.path.join(
            output_dir, 
            f'{title.lower().replace(' ', '_')}.png'
        ),
        bbox_inches='tight'
    )