def sort_dict_by_value(d,reverse=False):
    return dict(sorted(d.items(),key=lambda x:x[1],reverse=reverse))
colors={'red':4,'blue':5,'black':1,'green':3,'white':2}
print("Original dictionary elements:\n",colors)
print("\nSort elements by ascending by value:")
print(sort_dict_by_value(colors))
print("\nSort elements by descending by value:")
print(sort_dict_by_value(colors,True))