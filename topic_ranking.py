"""
Topic Ranking Sorter

This script takes in an .csv file with the topic rankings done in Google Forms and prints out the preference order of the topics.

It puts a higher weight on lower rankings. If a topic got a lot of 1st rank votes but wasn't the first pick, it will most likely be the second pick.
"""

import csv
import numpy as np

total = None

# Retrieve data
with open("data.csv") as data_file:
    csv_reader = csv.reader(data_file, delimiter=',')
    total = np.array([csv_reader.__next__()])
    for row in csv_reader:
        total = np.append(total, [row], axis=0)

header = total[0, 1:]
data = np.array(total[1:, 1:], dtype=np.int32)

# Process data into a map with this form:
# {topic_index: {rank1: count1, rank2: count2}, ...}
processed = {}
for i, _ in enumerate(header):
    (ranks, counts) = np.unique(data[:, i], return_counts=True)
    processed[i] = {rank: count for rank, count in zip(ranks, counts)}

for topic_index, ranks in processed.items():
    for i in range(1, len(header) + 1):
        if i not in ranks:
            ranks[i] = 0


# Creating rankings
rankings = []
for i in range(1, len(header) + 1):
    max_topic = 0
    max_count = 0
    for topic_index, ranks in processed.items():
        if i in ranks and ranks[i] > max_count:
            max_topic = topic_index
            max_count = ranks[i]
    rankings.append(max_topic)
    processed.pop(max_topic, None)
    for topic_index, ranks in processed.items():
        ranks[i+1] += ranks[i]*3
        ranks[i] = 0

# Print rankings
print("Here are the rankings:")
for i, ranking in enumerate(rankings):
    print("Topic #{}: {}".format(i + 1, header[ranking]))
