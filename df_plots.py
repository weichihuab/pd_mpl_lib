
# %%
import pandas as pd
import sys
sys.path.insert(1, '/Users/weichih/python_practice/hiweichihchen/pd_mpl_lib')
from df_plots_lib import plot_2d_scatter

# %%
file1 = 'pokemon_data.csv'
df = pd.read_csv(file1)
col = 'Type_1'
groups = ['Grass','Fire','Water']
colors = ['green', 'red', 'blue']
kwarg = {'colors': colors, 'alpha': 0.5, 'label_size':40}
plot_2d_scatter(df,col,groups,'Attack','Defense',**kwarg)
# %%

