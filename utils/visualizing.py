from matplotlib import pyplot as plt
from sklearn.manifold import TSNE
import seaborn as sns


def _t_sne_preproc(perp: int, x_data):
    tsne = TSNE(init='random', n_components=2, perplexity=perp, random_state=123, learning_rate='auto')
    tsne_features = tsne.fit_transform(x_data)
    return tsne_features


def draw_scatter_plot(perp: int, x_data, y_data):
    tsne_features = _t_sne_preproc(perp, x_data)
    plt_data = x_data.copy()
    plt_data['x'] = tsne_features[:, 0]
    plt_data['y'] = tsne_features[:, 1]
    fig, ax = plt.subplots()
    ax.set_title(f'perplexity={perp}')
    g = sns.scatterplot(x='x', y='y', hue=y_data, data=plt_data)
    g.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
