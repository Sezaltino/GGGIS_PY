c=0

fig, ax=plt.subplots()
for a in lista:
    c+=1
    a.plot(ax=ax, zorder=c)

axis = df_places.plot(ax=ax)


html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()
