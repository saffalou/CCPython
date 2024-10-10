# aliasing -  using the as keyword:
#  import module_name as name_you_pick_for_the_module
#  Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.


# import seaborn - installed this using pip. This will spin up a graph of plot points

# Add your code below:
# using an alias to rename matplotlib
# importing only part of matplotlib not the entire module functionality
from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(numbers_a, 12)

plt.plot(numbers_a, numbers_b)

plt.show()
