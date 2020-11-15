import matplotlib.pyplot as plt
import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--episodes", type = int, help = "Number of training episodes. Values used in demo were defaults of 100.")
parser.add_argument("-p", "--path", type = str, help = "Path to CSV file containing Q-values for each update() call.  \
                                                        First row must contain column information (format: north,west,south,east). \
                                                        Default path is ./q_vals_100eps.csv (which is auto-generated here when you execute the Q-learning demo).")

args = parser.parse_args()

episodes = args.episodes if args.episodes else 100
filepath = args.path if args.path else "q_vals_100eps.csv"

# read in csv data
try:
    with open(filepath) as csvfile:
        csv_rows = list(csv.reader(csvfile))

except:
    raise FileNotFoundError("File not found. Make sure you've entered a valid path or run the Q-learning demo once.")

counter = 0
north, west, south, east = [], [], [], []

# store into column-wise arrays
for row in csv_rows[1:]:
    north.append(float(row[0]))
    west.append(float(row[1]))
    south.append(float(row[2]))
    east.append(float(row[3]))

# plot all actions in one plot
iters = list(range(len(csv_rows) - 1))
plt.plot(iters, north, 'r', label = "north")
plt.plot(iters, west, 'b', label = "west")
plt.plot(iters, south, 'g', label = "south")
plt.plot(iters, east, 'c', label = "east")
plt.title("Evolution of Q-Learning Q-Values at State (1, 2) over {} Episodes".format(episodes))
plt.legend(loc = "upper left")
plt.xlabel("Updates")
plt.ylabel("Q-Value")

plt.show()
plt.savefig("qlearning_{}eps_plot.png".format(episodes))