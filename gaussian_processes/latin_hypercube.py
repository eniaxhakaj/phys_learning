import pyDOE as p
import matplotlib.pyplot as plt

# Create 5 strata for a single variable and randomly select from each strata
lh = p.lhs(1, samples=5)
# e.g.
# [[0.719] [0.468] [0.385] [0.857] [0.143]]

lh = p.lhs(2, samples=3)
# e.g.
# [[0.796 0.524]  [0.616 0.078]  [0.129 0.863]] (or 3,2  2,1, 1,3)
# [[0.389 0.474]  [0.029 0.828]  [0.755 0.289]] (or 2,2  1,3  3,1)
# Ignoring ordering, there are 3! possible pairings

# By default we have been sampling randomly but we can also
lh = p.lhs(2, samples=4, criterion="center")
lh = p.lhs(2, samples=4, criterion="centermaximin") # I don't really understand this...

plt.scatter(
        [i[0] for i in lh],
        [i[1] for i in lh],
)
plt.show()

print(lh)
