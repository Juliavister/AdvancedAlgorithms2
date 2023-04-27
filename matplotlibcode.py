import matplotlib.pyplot as plt
import numpy as np

# Define the data arrays
naive_build = 0.0320
BBST_build = 0.1020
trie_build = 0.3810
hash_build = 0.0470

naive_check = 0.2910
BBST_check = 0.0010
trie_check = 0.0010
hash_check = 0.0000002

# Set the x-axis labels and positions
labels = ['Naive', 'BBST', 'Trie', 'Hash']
x_pos = np.arange(len(labels))

# Set the data values for the line graph
build_times = [naive_build, BBST_build, trie_build, hash_build]
check_times = [naive_check, BBST_check, trie_check, hash_check]

# Create the line graph
fig, ax = plt.subplots()
ax.plot(x_pos, build_times, '-o', label='Dictionary building')
ax.plot(x_pos, check_times, '-o', label='Spell checking')

# Set the plot labels and legend
ax.set_ylabel('Time (s)')
ax.set_yscale('log')  # Set the y-axis scale to logarithmic
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.legend()

# Add text labels to the data points
for i, j in zip(x_pos, build_times):
    ax.annotate('{:.2e}'.format(j), xy=(i, j), xytext=(5, 0),
                textcoords="offset points", ha='left', va='center')
for i, j in zip(x_pos, check_times):
    ax.annotate('{:.2e}'.format(j), xy=(i, j), xytext=(5, 0),
                textcoords="offset points", ha='left', va='center')

# Show the plot
plt.show()
