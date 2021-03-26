import matplotlib.pyplot as plt


def calculate_quantity_life(half_life, disintegration_time):
    return int(disintegration_time / half_life)


# Return the rest amount of a substance
def final_amount(initial_amount, quantity_life):
    return initial_amount / 2 ** quantity_life


def plot_line(initial_amount, quantity_life):
    # The range of quantity life is + 1
    # Because the range will start with 0
    # Ex: if you input 5 in the plt.show
    # will show 0 to 4
    x = [i for i in range(quantity_life+1)]
    y = [final_amount(initial_amount, x) for x in range(quantity_life+1)]
    plt.plot(x, y, marker='o')
    plt.title('Half Life Graphic')
    plt.xlabel('Amount Half Life')
    plt.ylabel('Amount Of The Substance')
    plt.savefig('3')
    plt.show()



i_amount = 2
q_life = calculate_quantity_life(60, 360)

plot_line(2, 3)
