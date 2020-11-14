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
topic_range = range(1, len(header) + 1)
num_topics = len(header)

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

# Compile weighted scores
scores = np.zeros(num_topics)
for topic_index, ranks in processed.items():
    score = 0
    for i in range(1, len(header) + 1):
        score += ranks[i] * (3 ** (num_topics - i))
    scores[topic_index] = score

# Print rankings
print("Topic Ranking:")
ranks = np.flip(scores.argsort())
for i, topic_index in enumerate(ranks):
    score = scores[topic_index]
    topic_title = header[topic_index].split("[", )[1][:-1]
    print("Topic #{}: {}".format(i + 1, topic_title))
