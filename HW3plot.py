import matplotlib.pyplot as plt

# Read centrality data from the file
with open('centrality_data.txt', 'r') as file:
    lines = file.readlines()
    degree_centrality_values = list(map(float, lines[1].strip().split(',')))
    closeness_centrality_values = list(map(float, lines[3].strip().split(',')))
    betweenness_centrality_values = list(map(float, lines[5].strip().split(',')))
    top_200_nodes = list(map(int, lines[7].strip().split(',')))
    closeness_top_200_values = list(map(float, lines[9].strip().split(',')))
    betweenness_top_200_values = list(map(float, lines[11].strip().split(',')))
    mean_closeness = float(lines[13].split(":")[1])
    median_closeness = float(lines[14].split(":")[1])
    std_closeness = float(lines[15].split(":")[1])
    mean_betweenness = float(lines[16].split(":")[1])
    median_betweenness = float(lines[17].split(":")[1])
    std_betweenness = float(lines[18].split(":")[1])

# Plot histograms
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(degree_centrality_values, bins=30, alpha=0.7, color='blue')
plt.title('Degree Centrality Histogram')
plt.xlabel('Degree Centrality')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(closeness_centrality_values, bins=30, alpha=0.7, color='green')
plt.title('Closeness Centrality Histogram')
plt.xlabel('Closeness Centrality')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(betweenness_centrality_values, bins=30, alpha=0.7, color='red')
plt.title('Betweenness Centrality Histogram')
plt.xlabel('Betweenness Centrality')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Print statistics for top 200 nodes
print("Statistics for the top 200 nodes by degree centrality:")
print("Closeness Centrality:")
print("Mean:", mean_closeness)
print("Median:", median_closeness)
print("Standard Deviation:", std_closeness)
print()
print("Betweenness Centrality:")
print("Mean:", mean_betweenness)
print("Median:", median_betweenness)
print("Standard Deviation:", std_betweenness)
