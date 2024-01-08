# from cProfile import label
# from curses.panel import bottom_panel
import matplotlib.pyplot as plt
import pandas as pd

xls_file_first = pd.ExcelFile('1stgenpiwi.xlsx')
df = xls_file_first.parse(sheet_name = "Sheet1", header=0)
print(df)

#Plotting horizontal bars at x = {from start to end} for each corresponding y = {log2FoldChange}
plt.barh(df.log2FoldChange, df.End-df.Start, height=0.05, left=df.Start, color='green')

xls_file_second = pd.ExcelFile('5thgenpiwi.xlsx')
df = xls_file_second.parse(sheet_name = "Sheet1", header=0)

#Plotting horizontal bars at x = {from start to end} for each corresponding y = {log2FoldChange}
plt.barh(df.log2FoldChange, df.End-df.Start, height=0.05, left=df.Start, color='red')


#Plotting center line at y=0
# plt.rc('axes', axisbelow=True)
plt.axhline(y = 0, color='black', linestyle ='dashed', linewidth = 1, zorder=0)
plt.axhline(y = 0, color='red', linestyle ='solid', linewidth = 1, zorder=0)

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
bar_plot = plt.barh(margine_df.mark, margine_df.x_end-margine_df.x_start, height=0.25, left=margine_df.x_start, color=margine_colors, edgecolor='grey', zorder=1
)
bar_label = ['',1,2,3,4,5,6,7,8,'']
def autolabel(rects):
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height,
                bar_label[idx], ha='center', va='center', rotation=0)
autolabel(bar_plot)


plt.plot([0],[0], color="green", label=r"1stgenpiwi")
plt.plot([0],[0], color="red", label=r"5thgenpiwi")
plt.legend(loc="upper right")

plt.xlim(10990000, 10982000)
plt.ylim(-5,5)

plt.ticklabel_format(useOffset=False, style='plain', axis='x')
#plt.tick_params(labelbottom=False)

plt.title("Upregulated gene- Piwi ovary (1st gen vs 5th gen)")
plt.xlabel("Gene Position")
plt.ylabel("Log fold")

plt.show()
