import networkx as nx

# Read the directed graph from the dataset
G = nx.read_edgelist("twitter_combined.txt", create_using=nx.DiGraph(), nodetype=int)

# Calculate the triadic census
triadic_census = nx.triadic_census(G)

# Print the results
print("Triadic Census:")
for key, value in triadic_census.items():
    print(f"{key}: {value}")