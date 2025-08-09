-- Just an example to visualise the results of each technique --

import matplotlib.pyplot as plt

methods = ["Full", "Incremental", "Differential"]
durations = [4.18, 1.15, 1.54]

plt.bar(methods, durations)
plt.ylabel("Duration (s)")
plt.title("Backup Duration by Method")
plt.show()
