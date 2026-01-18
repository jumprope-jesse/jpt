---
type: link
source: notion
url: https://github.com/originalankur/maptoposter
notion_type: Software Repo
tags: ['Running']
created: 2026-01-17T14:33:00.000Z
---

# GitHub - originalankur/maptoposter: Transform your favorite cities into beautiful, minimalist designs. MapToPoster lets you create and export visually striking map posters with code.

## Overview (from Notion)
- Create a personalized map poster of New York City to capture family memories and adventures.
- Use the minimalist design to declutter visual space in your home, blending functionality with aesthetics.
- Explore various themes that resonate with your family's style, from warm beige to ocean blues, making art that reflects your life.
- Engage your kids in the process, teaching them about geography and design while fostering creativity.
- Consider the significance of location in family life: how neighborhoods shape experiences and memories.
- Alternate view: while focusing on aesthetics, reflect on the importance of functionality in home decor—how design impacts daily life.
- The poster creation process can be a fun bonding experience, reinforcing family values while celebrating the uniqueness of your urban environment.

## AI Summary (from Notion)
Generate minimalist map posters for any city using Python. Installation requires pip, and usage involves specifying city and country with various options for themes and distances. The project includes multiple themes, a guide for distances, and a structure for adding custom themes. Key functions and rendering layers are outlined for contributors looking to extend the script.

## Content (from Notion)

# City Map Poster Generator

Generate beautiful, minimalist map posters for any city in the world.

## Examples

## Installation

```plain text
pip install -r requirements.txt
```

## Usage

```plain text
python create_map_poster.py --city <city> --country <country> [options]
```

### Options

### Examples

```plain text
# Iconic grid patterns
python create_map_poster.py -c "New York" -C "USA" -t noir -d 12000           # Manhattan grid
python create_map_poster.py -c "Barcelona" -C "Spain" -t warm_beige -d 8000   # Eixample district

# Waterfront & canals
python create_map_poster.py -c "Venice" -C "Italy" -t blueprint -d 4000       # Canal network
python create_map_poster.py -c "Amsterdam" -C "Netherlands" -t ocean -d 6000  # Concentric canals
python create_map_poster.py -c "Dubai" -C "UAE" -t midnight_blue -d 15000     # Palm & coastline

# Radial patterns
python create_map_poster.py -c "Paris" -C "France" -t pastel_dream -d 10000   # Haussmann boulevards
python create_map_poster.py -c "Moscow" -C "Russia" -t noir -d 12000          # Ring roads

# Organic old cities
python create_map_poster.py -c "Tokyo" -C "Japan" -t japanese_ink -d 15000    # Dense organic streets
python create_map_poster.py -c "Marrakech" -C "Morocco" -t terracotta -d 5000 # Medina maze
python create_map_poster.py -c "Rome" -C "Italy" -t warm_beige -d 8000        # Ancient layout

# Coastal cities
python create_map_poster.py -c "San Francisco" -C "USA" -t sunset -d 10000    # Peninsula grid
python create_map_poster.py -c "Sydney" -C "Australia" -t ocean -d 12000      # Harbor city
python create_map_poster.py -c "Mumbai" -C "India" -t contrast_zones -d 18000 # Coastal peninsula

# River cities
python create_map_poster.py -c "London" -C "UK" -t noir -d 15000              # Thames curves
python create_map_poster.py -c "Budapest" -C "Hungary" -t copper_patina -d 8000  # Danube split

# List available themes
python create_map_poster.py --list-themes
```

### Distance Guide

## Themes

17 themes available in themes/ directory:

## Output

Posters are saved to posters/ directory with format:

```plain text
{city}_{theme}_{YYYYMMDD_HHMMSS}.png

```

## Adding Custom Themes

Create a JSON file in themes/ directory:

```plain text
{
  "name": "My Theme",
  "description": "Description of the theme",
  "bg": "#FFFFFF",
  "text": "#000000",
  "gradient_color": "#FFFFFF",
  "water": "#C0C0C0",
  "parks": "#F0F0F0",
  "road_motorway": "#0A0A0A",
  "road_primary": "#1A1A1A",
  "road_secondary": "#2A2A2A",
  "road_tertiary": "#3A3A3A",
  "road_residential": "#4A4A4A",
  "road_default": "#3A3A3A"
}
```

## Project Structure

```plain text
map_poster/
├── create_map_poster.py          # Main script
├── themes/               # Theme JSON files
├── fonts/                # Roboto font files
├── posters/              # Generated posters
└── README.md

```

## Hacker's Guide

Quick reference for contributors who want to extend or modify the script.

### Architecture Overview

```plain text
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│   CLI Parser    │────▶│  Geocoding   │────▶│  Data Fetching  │
│   (argparse)    │     │  (Nominatim) │     │    (OSMnx)      │
└─────────────────┘     └──────────────┘     └─────────────────┘
                                                     │
                        ┌──────────────┐             ▼
                        │    Output    │◀────┌─────────────────┐
                        │  (matplotlib)│     │   Rendering     │
                        └──────────────┘     │  (matplotlib)   │
                                             └─────────────────┘

```

### Key Functions

### Rendering Layers (z-order)

```plain text
z=11  Text labels (city, country, coords)
z=10  Gradient fades (top & bottom)
z=3   Roads (via ox.plot_graph)
z=2   Parks (green polygons)
z=1   Water (blue polygons)
z=0   Background color

```

### OSM Highway Types → Road Hierarchy

```plain text
# In get_edge_colors_by_type() and get_edge_widths_by_type()
motorway, motorway_link     → Thickest (1.2), darkest
trunk, primary              → Thick (1.0)
secondary                   → Medium (0.8)
tertiary                    → Thin (0.6)
residential, living_street  → Thinnest (0.4), lightest
```

### Adding New Features

New map layer (e.g., railways):

```plain text
# In create_poster(), after parks fetch:
try:
    railways = ox.features_from_point(point, tags={'railway': 'rail'}, dist=dist)
except:
    railways = None

# Then plot before roads:
if railways is not None and not railways.empty:
    railways.plot(ax=ax, color=THEME['railway'], linewidth=0.5, zorder=2.5)
```

New theme property:

1. Add to theme JSON: "railway": "#FF0000"
1. Use in code: THEME['railway']
1. Add fallback in load_theme() default dict
### Typography Positioning

All text uses transform=ax.transAxes (0-1 normalized coordinates):

```plain text
y=0.14  City name (spaced letters)
y=0.125 Decorative line
y=0.10  Country name
y=0.07  Coordinates
y=0.02  Attribution (bottom-right)

```

### Useful OSMnx Patterns

```plain text
# Get all buildings
buildings = ox.features_from_point(point, tags={'building': True}, dist=dist)

# Get specific amenities
cafes = ox.features_from_point(point, tags={'amenity': 'cafe'}, dist=dist)

# Different network types
G = ox.graph_from_point(point, dist=dist, network_type='drive')  # roads only
G = ox.graph_from_point(point, dist=dist, network_type='bike')   # bike paths
G = ox.graph_from_point(point, dist=dist, network_type='walk')   # pedestrian
```

### Performance Tips

- Large dist values (>20km) = slow downloads + memory heavy
- Cache coordinates locally to avoid Nominatim rate limits
- Use network_type='drive' instead of 'all' for faster renders
- Reduce dpi from 300 to 150 for quick previews

