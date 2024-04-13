# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

def plot_2d_scatter(df,col,groups,x_axis,y_axis,**kwarg):
    colors = kwarg['colors']
    alpha = kwarg['alpha']
    label_size = kwarg['label_size']
    fig, ax = plt.subplots(figsize=(8, 8))
    n = 0
    for i in groups:
        color = colors[n]
        x = df[df[col]==i][x_axis]
        y = df[df[col]==i][y_axis]
        ax.scatter(x, y, label=i, alpha=alpha, s=label_size, color=color)
        n += 1
    
    ax.set_xlabel(x_axis, fontsize=16, fontweight='bold')
    ax.set_ylabel(y_axis, fontsize=16, fontweight='bold')
    ax.legend(fontsize=16)
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    [x.set_linewidth(2.0) for x in ax.spines.values()]
    plt.savefig('scatter_plot_2d.png',dpi=300,bbox_inches='tight')
    plt.show()

def plot_3d_scatter(df,col,groups,x_axis,y_axis,z_axis,**kwarg):
    colors = kwarg['colors']
    alpha = kwarg['alpha']
    label_size = kwarg['label_size']
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    n = 0
    for i in groups:
        color = colors[n]
        x = df[df[col]==i][x_axis]
        y = df[df[col]==i][y_axis]
        z = df[df[col]==i][z_axis]
        ax.scatter(x, y, z, label=i, alpha=alpha, s=label_size, color=color)
        n += 1
    
    ax.set_xlabel(x_axis, fontsize=16, fontweight='bold')
    ax.set_ylabel(y_axis, fontsize=16, fontweight='bold')
    ax.set_zlabel(z_axis, fontsize=16, fontweight='bold')
    ax.legend(fontsize=16)
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='z', labelsize=16)
    [x.set_linewidth(2.0) for x in ax.spines.values()]
    plt.savefig('scatter_plot_3d.png',dpi=300,bbox_inches='tight')
    plt.show()

def plot_boxplot(df,x_axis,y_axis,groups):
    grped_bplot = sns.catplot(x=x_axis, y=y_axis, hue=groups, kind="box", data=df, legend=False, height=6, aspect=1.5)
    grped_bplot = sns.stripplot(x=x_axis, y=y_axis, hue=groups, jitter=True,
                                 dodge=True, marker='o', palette="Set1", alpha=0.5, data=df)
    handles, labels = grped_bplot.get_legend_handles_labels()
    #grped_bplot.get_legend().remove()
    num = len(df[groups].unique())
    grped_bplot.set_xlabel(x_axis, fontsize=16, fontweight='bold')
    grped_bplot.set_ylabel(y_axis, fontsize=16, fontweight='bold')
    plt.legend(handles[0:num], labels[0:num], fontsize=16)
    grped_bplot.tick_params(axis='x', labelsize=16)
    grped_bplot.tick_params(axis='y', labelsize=16)
    [x.set_linewidth(2.0) for x in grped_bplot.spines.values()]
    plt.savefig('boxplot.png',dpi=300,bbox_inches='tight')



    #plt.legend('')

# %%



# %% plot scatter by groups
def main():
    file1 = 'pokemon_data.csv'
    df = pd.read_csv(file1)
    col = 'Type_1'
    groups = ['Grass','Fire','Water']
    colors = ['green', 'red', 'blue']
    kwarg = {'colors': colors, 'alpha': 0.5, 'label_size':40}
    plot_2d_scatter(df,col,groups,'Attack','Defense',**kwarg)
    plot_3d_scatter(df,col,groups,'Attack','Defense','HP',**kwarg)

    categories = ['Attack','Defense']
    df = df[(df['Type_1']== 'Grass') | (df['Type_1']== 'Fire')]
    df = df[(df['Type_2']== 'Flying') | (df['Type_2']== 'Fighting')]
    plot_boxplot(df,'Type_2','Attack','Type_1')
# %%
if __name__ == '__main__':
    main()
# %%

