#from cProfile import label
#from curses.panel import bottom_panel
import matplotlib.pyplot as plt
import pandas as pd

xls_file = pd.ExcelFile('piwi.xlsx')
df = xls_file.parse(sheet_name = "Sheet1") #, header=0, nrows= 293, skiprows=lambda x: x in range(99,105))

def set_color(fold_at_value):
    color = ''
    if fold_at_value > 0:
        color = 'green'
    elif fold_at_value < 0:
        color = 'red'
    else:
        color = 'black'
    return color

# def find_min_start_in_negative(df):
#     temp_list = []
#     idx = 0
#     for value in df['Start']:
#         if df['log2FoldChange'][idx] < 0:
#             temp_list.append(value)
#         idx+=1
#     return min(temp_list)

# def find_max_end_in_negative(df):
#     temp_list = []
#     idx = 0
#     for value in df['End']:
#         if df['log2FoldChange'][idx] < 0:
#             temp_list.append(value)
#         idx+=1
#     return max(temp_list)

# def find_min_start_in_positive(df):
#     temp_list = []
#     idx = 0
#     for value in df['Start']:
#         if df['log2FoldChange'][idx] > 0:
#             temp_list.append(value)
#         idx+=1
#     return min(temp_list)

# def find_max_end_in_positive(df):
#     temp_list = []
#     idx = 0
#     for value in df['End']:
#         if df['log2FoldChange'][idx] > 0:
#             temp_list.append(value)
#         idx+=1
#     return max(temp_list)

# Setting colors for negative and positive log2FoldChange values
colors = df.log2FoldChange.apply(set_color)
# print(colors)

#Plotting horizontal bars at x = {from start to end} for each corresponding y = {log2FoldChange}
plt.barh(df.log2FoldChange, df.End-df.Start, height=0.05, left=df.Start, color=colors)

'''
x_value = find_min_start_in_negative(df)
y_value = df['log2FoldChange'][df.index[df['Start'] == x_value]].values[0]
# print(x_value)
# print(y_value)

plt.plot([x_value], [y_value], marker="o", markersize=3, markeredgecolor="blue", markerfacecolor="blue")

x_value = find_max_end_in_negative(df)
y_value = df['log2FoldChange'][df.index[df['End'] == x_value]].values[0]
# print(x_value)
# print(y_value)

plt.plot([x_value], [y_value], marker="o", markersize=3, markeredgecolor="blue", markerfacecolor="blue")

x_value = find_min_start_in_positive(df)
y_value = df['log2FoldChange'][df.index[df['Start'] == x_value]].values[0]
# print(x_value)
# print(y_value)

plt.plot([x_value], [y_value], marker="o", markersize=3, markeredgecolor="orange", markerfacecolor="orange")

x_value = find_max_end_in_positive(df)
y_value = df['log2FoldChange'][df.index[df['End'] == x_value]].values[0]
# print(x_value)
# print(y_value)

plt.plot([x_value], [y_value], marker="o", markersize=3, markeredgecolor="orange", markerfacecolor="orange")
'''

#Plotting center line at y=0
# plt.rc('axes', axisbelow=True)
plt.axhline(y = 0, color='black', linestyle ='dashed', linewidth = 1, zorder=0)

margine_df = pd.DataFrame(
    {
        'id': ['5-Utr', 'exon_1', 'exon_2', 'exon_3', 'exon_4', 'exon_5', 'exon_6', 'exon_7', 'exon_8', '3-Utr'],
        'mark': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'x_start': [10987334, 10987249, 10985544, 10985167, 10984946, 10984141, 10983896, 10983666, 10982658, 10982205],
        'x_end': [10987420, 10987332, 10986128, 10985487, 10985100, 10984341, 10984087, 10983776, 10983540, 10982657]
    }
)

margine_colors = margine_df.id.map(
    {
        '5-Utr': 'gold', 'exon_1': 'orange', 'exon_2': 'indigo', 'exon_3': 'blue', 'exon_4': 'green',
        'exon_5': 'yellow', 'exon_6': 'cyan', 'exon_7': 'magenta', 'exon_8': 'pink', '3-Utr': 'gold'
    }
)

#Plotting Bars for Margine and assigning label
bar_plot = plt.barh(margine_df.mark, margine_df.x_end-margine_df.x_start, height=0.25, left=margine_df.x_start, color=margine_colors, edgecolor='grey', zorder=1)
bar_label = ['',1,2,3,4,5,6,7,8,'']
def autolabel(rects):
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height,
                bar_label[idx], ha='center', va='center', rotation=0)
autolabel(bar_plot)


plt.plot([0],[0], color="green", label=r"Upregulated")
plt.plot([0],[0], color="red", label=r"Downregulated")
plt.legend(loc="upper right")

plt.xlim(10990000, 10982000)
plt.ylim(-5,5)

plt.ticklabel_format(useOffset=False, style='plain', axis='x')

plt.tick_params(labelbottom=False)

plt.title("Upregulated gene-Piwi (Ovary)")
plt.xlabel("Gene Position")
plt.ylabel("Log 2 fold")

plt.show()
