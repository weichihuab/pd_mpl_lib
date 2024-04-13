

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.insert(1, '/Users/weichih/python_practice/hiweichihchen/pd_mpl_lib')
from df_plots_lib import plot_2d_scatter
from df_plots_lib import plot_3d_scatter


def main():
    file1 = 'pokemon_data.csv'
    df = pd.read_csv(file1)
    col = 'Type_1'
    groups = ['Grass','Fire','Water']
    colors = ['green', 'red', 'blue']
    kwarg = {'colors': colors, 'alpha': 0.5, 'label_size':40}
    plot_2d_scatter(df,col,groups,'Attack','Defense',**kwarg)
    #plot_3d_scatter(df,col,groups,'Attack','Defense','HP',**kwarg)

if __name__ == '__main__':
    main()
