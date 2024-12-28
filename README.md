# visualSec

**visualSec** is a dynamic tool for visualizing and analyzing cybersecurity data as interactive graphs. Designed for OSINT practitioners, ethical hackers, and cybersecurity analysts, it simplifies the exploration of complex relationships between entities.

## Features

- **Graph Visualization**: Display entities (e.g., domains, IPs, emails) and relationships with customizable layouts.
- **Risk-Based Node Coloring**: Highlight nodes using colormaps like `Reds` based on attributes such as vulnerabilities or risks.
- **Data Import/Export**:
  - Import entities and relationships from JSON.
  - Export graphs to GEXF for use with other tools.
- **Analysis Tools**:
  - Clustering: Group related nodes (e.g., domains by ASN).
  - Pathfinding: Identify attack paths or entity dependencies.
  - Heatmaps: Visualize critical vulnerabilities.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ClaudiasLibrary/visualSec.git
   cd visualSec
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Import the `CyberSecurityVisualizer` class in your script:
   ```python
   from visualizer import CyberSecurityVisualizer
   ```

2. Create a visualizer instance and add entities and relationships:
   ```python
   visualizer = CyberSecurityVisualizer()

   visualizer.add_entity("Domain: example.com", type="Domain")
   visualizer.add_entity("IP: 192.168.1.1", type="IP")
   visualizer.add_relationship("Domain: example.com", "IP: 192.168.1.1", relationship="Resolves to")
   ```

3. Visualize the graph:
   ```python
   visualizer.visualize(layout='spring', title="Cybersecurity Graph")
   ```

4. Export the graph:
   ```python
   visualizer.export_to_file("cybersecurity_graph.gexf")
   ```

## Example

Import and visualize data from JSON:

```python
import json
from visualizer import CyberSecurityVisualizer

visualizer = CyberSecurityVisualizer()

# Sample JSON data
sample_json = json.dumps({
    "entities": [
        {"name": "Domain: example.com", "attributes": {"type": "Domain"}},
        {"name": "IP: 192.168.1.1", "attributes": {"type": "IP"}}
    ],
    "relationships": [
        {"source": "Domain: example.com", "target": "IP: 192.168.1.1", "attributes": {"relationship": "Resolves to"}}
    ]
})

# Import data and visualize
visualizer.import_from_json(sample_json)
visualizer.visualize(layout='spring', title="OSINT Graph")
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

