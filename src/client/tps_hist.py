import matplotlib.pyplot as plt


def draw_output(plot):
    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width()/2., 1.002*height,
                 '%d' % int(height), ha='center', va='bottom', size='12')


results = {'native': [[74.82, 53.21], [69.62, 55.15], [74.95, 57.98]], 'vm': [[33.83, 24.54], [29.04, 21.17], [34.14, 24.54]],
           'container': [[55.98, 45.99], [50.87, 42.83], [55.20, 46.90]]}

x = [['js_json', 'js_query'], ['python_json',
                               'python_query'], ['go_json', 'go_query']]
for env in ['native', 'vm', 'container']:
    y = results[env]
    plot1 = plt.bar(x[0], height=y[0],  width=0.6,
                    color="red", label='javascript')
    draw_output(plot1)

    plot2 = plt.bar(x[1], height=y[1],
                    width=0.6, color="blue", label='python')
    draw_output(plot2)

    plot3 = plt.bar(x[2], height=y[2],
                    width=0.6, color="green", label='go')
    draw_output(plot3)

    plt.title(f'{env}', fontdict={
        'family': 'sans-serif', 'weight': 'bold', 'size': 15})

    plt.ylabel("TPS", size=15)
    plt.legend()
    plt.savefig(f'{env}.png', dpi=200)
    plt.close()
# plt.show()
