import networkx as nx
import time

start = time.time()

# Read the directed graph from the dataset
G = nx.read_edgelist("twitter_combined.txt", create_using=nx.DiGraph(), nodetype=int)

# Convert the directed graph to an undirected graph
G_undirected = G.to_undirected()

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G_undirected)
closeness_centrality = nx.closeness_centrality(G_undirected)
betweenness_centrality = nx.betweenness_centrality(G_undirected)

# Get top 200 nodes by degree centrality
top_degree_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:200]

# Calculate closeness and betweenness centrality for top nodes
closeness_values_top = [closeness_centrality[node] for node in top_degree_nodes]
betweenness_values_top = [betweenness_centrality[node] for node in top_degree_nodes]

# Analyze closeness and betweenness centrality for top nodes
mean_closeness = sum(closeness_values_top) / len(closeness_values_top)
median_closeness = sorted(closeness_values_top)[len(closeness_values_top)//2]
std_closeness = (sum((x - mean_closeness) ** 2 for x in closeness_values_top) / len(closeness_values_top)) ** 0.5

mean_betweenness = sum(betweenness_values_top) / len(betweenness_values_top)
median_betweenness = sorted(betweenness_values_top)[len(betweenness_values_top)//2]
std_betweenness = (sum((x - mean_betweenness) ** 2 for x in betweenness_values_top) / len(betweenness_values_top)) ** 0.5

# Write centrality data to a file
with open('centrality_data.txt', 'w') as file:
    file.write("Degree Centrality Values:\n")
    file.write(','.join(map(str, degree_centrality.values())) + '\n')
    file.write("Closeness Centrality Values:\n")
    file.write(','.join(map(str, closeness_centrality.values())) + '\n')
    file.write("Betweenness Centrality Values:\n")
    file.write(','.join(map(str, betweenness_centrality.values())) + '\n')
    file.write("Top 200 Nodes by Degree Centrality:\n")
    file.write(','.join(map(str, top_degree_nodes)) + '\n')
    file.write("Closeness Centrality for Top 200 Nodes:\n")
    file.write(','.join(map(str, closeness_values_top)) + '\n')
    file.write("Betweenness Centrality for Top 200 Nodes:\n")
    file.write(','.join(map(str, betweenness_values_top)) + '\n')
    file.write("Statistics for Top 200 Nodes by Degree Centrality:\n")
    file.write(f"Mean Closeness: {mean_closeness}\n")
    file.write(f"Median Closeness: {median_closeness}\n")
    file.write(f"Standard Deviation of Closeness: {std_closeness}\n")
    file.write(f"Mean Betweenness: {mean_betweenness}\n")
    file.write(f"Median Betweenness: {median_betweenness}\n")
    file.write(f"Standard Deviation of Betweenness: {std_betweenness}\n")

end = time.time()
print("Execution Time:", end - start, "seconds")