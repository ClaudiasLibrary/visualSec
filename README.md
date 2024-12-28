# visualSec
A tool for visualizing and analyzing cybersecurity data as interactive graphs. Supports entity modeling, risk-based coloring, attack path analysis, and data import/export. Designed for OSINT and cybersecurity professionals.

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
