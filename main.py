import networkx as nx
import matplotlib.pyplot as plt
import json
import community  # for community detection
import csv

class CyberSecurityVisualizer:
    def __init__(self):
        # Initialize an empty graph
        self.graph = nx.Graph()

    def add_entity(self, entity, **attributes):
        """Add an entity to the graph."""
        self.graph.add_node(entity, **attributes)

    def add_relationship(self, entity1, entity2, **attributes):
        """Add a relationship (edge) between two entities."""
        self.graph.add_edge(entity1, entity2, **attributes)

    def visualize(self, layout='spring', title="Cybersecurity Visualization"):
        """Visualize the graph."""
        plt.figure(figsize=(12, 8))

        # Choose layout
        if layout == 'spring':
            pos = nx.spring_layout(self.graph)
        elif layout == 'circular':
            pos = nx.circular_layout(self.graph)
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(self.graph)
        else:
            pos = nx.random_layout(self.graph)

        # Draw the graph
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color='skyblue',
            edge_color='gray',
            node_size=3000,
            font_size=10,
            font_color='black'
        )

        plt.title(title)
        plt.show()

    def export_to_file(self, file_name="graph.gexf"):
        """Export the graph to a file."""
        nx.write_gexf(self.graph, file_name)
        print(f"Graph exported to {file_name}")

    def import_from_json(self, json_data):
        """Import entities and relationships from JSON data."""
        data = json.loads(json_data)

        # Add entities from JSON
        for entity in data.get("entities", []):
            self.add_entity(entity["name"], **entity.get("attributes", {}))

        # Add relationships from JSON
        for relationship in data.get("relationships", []):
            self.add_relationship(
                relationship["source"],
                relationship["target"],
                **relationship.get("attributes", {})
            )

    def cluster_nodes(self):
        """Detect communities (clusters) within the graph."""
        partition = community.best_partition(self.graph)
        nx.set_node_attributes(self.graph, partition, "cluster")
        return partition

    def highlight_path(self, source, target):
        """Highlight the path between two entities (nodes)."""
        try:
            path = nx.shortest_path(self.graph, source, target)
            edge_colors = ['red' if (u, v) in zip(path[:-1], path[1:]) else 'gray' for u, v in self.graph.edges()]
            nx.draw(self.graph, with_labels=True, edge_color=edge_colors, node_color='skyblue', node_size=3000)
            plt.show()
        except nx.NetworkXNoPath:
            print(f"No path found between {source} and {target}")

    def create_heatmap(self, vulnerability_metric=None):
        """Create a heatmap for critical vulnerabilities or high-risk areas."""
        node_sizes = []
        node_colors = []
        for node in self.graph.nodes():  # This should be self.graph.nodes
            # Assume `vulnerability_metric` is a node attribute that is already set.
            vulnerability_value = self.graph.nodes[node].get(vulnerability_metric, 0)
            node_sizes.append(500 + 100 * vulnerability_value)  # Adjust the size based on the vulnerability score
            node_colors.append(vulnerability_value)  # Adjust color intensity
        nx.draw(self.graph, with_labels=True, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.Reds)
        plt.show()

    def export_to_csv(self, file_name="graph_summary.csv"):
        """Export the nodes and relationships to CSV."""
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write node attributes
            writer.writerow(['Entity', 'Type', 'Attributes'])
            for node, data in self.graph.nodes(data=True):  # Use self.graph.nodes
                writer.writerow([node, data.get('type', 'N/A'), json.dumps(data)])

            # Write relationships
            writer.writerow(['Source', 'Target', 'Relationship'])
            for source, target, data in self.graph.edges(data=True):  # Use self.graph.edges
                writer.writerow([source, target, json.dumps(data)])

        print(f"Graph exported to CSV: {file_name}")

    def export_to_json(self, file_name="graph_summary.json"):
        """Export the graph to JSON."""
        data = {
            "entities": [{"name": node, "attributes": data} for node, data in self.graph.nodes(data=True)],  # Use self.graph.nodes
            "relationships": [{"source": source, "target": target, "attributes": data} for source, target, data in self.graph.edges(data=True)]  # Use self.graph.edges
        }
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Graph exported to JSON: {file_name}")

# Example usage
if __name__ == "__main__":
    visualizer = CyberSecurityVisualizer()

    # Add entities and relationships manually
    visualizer.add_entity("Domain: example.com", type="Domain")
    visualizer.add_entity("IP: 192.168.1.1", type="IP")
    visualizer.add_entity("Person: Alice", type="Person")

    visualizer.add_relationship("Domain: example.com", "IP: 192.168.1.1", relationship="Resolves to")
    visualizer.add_relationship("Person: Alice", "Domain: example.com", relationship="Owns")

    # Clustering
    cluster_data = visualizer.cluster_nodes()
    print("Clusters:", cluster_data)

    # Pathfinding (highlight path between two entities)
    visualizer.highlight_path("Person: Alice", "Domain: example.com")

    # Heatmap visualization (assuming some vulnerability data exists)
    visualizer.create_heatmap(vulnerability_metric="vulnerability_score")

    # Export to CSV and JSON
    visualizer.export_to_csv("cybersecurity_summary.csv")
    visualizer.export_to_json("cybersecurity_summary.json")

    # Visualize the graph
    visualizer.visualize(layout='spring', title="Cybersecurity Network")

    # Export to GEXF
    visualizer.export_to_file("cybersecurity_graph.gexf")
