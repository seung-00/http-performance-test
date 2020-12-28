import matplotlib.pyplot as plt


def draw_output(plot):
    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width()/2., 1.002*height,
                 '%d' % int(height), ha='center', va='bottom', size='12')


results = {'native': [[6.06, 12.65], [7.10, 12.15], [5.33, 10.52]], 'vm': [[25.08, 36.13], [29.37, 38.58], [23.89, 30.66]],
'container': [[7.69, 13.49], [10.84, 14.76], [5.47, 12.81]]}

x = [['native'], ['container'], ['vm']]
for env in ['memory usage']:
    y = [17, 19, 28]
    plot1 = plt.bar(x[0], height=y[0],  width=0.6,
                    color="red", label='native')
    draw_output(plot1)

    plot2 = plt.bar(x[1], height=y[1],
                    width=0.6, color="blue", label='container')
    draw_output(plot2)

    plot3 = plt.bar(x[2], height=y[2],
                    width=0.6, color="green", label='vm')
    draw_output(plot3)

    plt.title(f'{env}', fontdict={
        'family': 'sans-serif', 'weight': 'bold', 'size': 15})

    plt.ylabel("memory usage (%)", size=15)
    plt.legend()
    plt.savefig(f'{env}.png', dpi=200)
    plt.close()
# plt.show()
