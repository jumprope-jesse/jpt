# Map Poster Project

> Family art project idea - create minimalist map posters of meaningful places

## The Idea

Use **maptoposter** (Python tool) to generate beautiful, minimalist map posters of cities that are meaningful to our family. Great way to:
- Capture family memories and adventures through art
- Teach kids about geography and design
- Create personalized home decor
- Bond as a family through creative activity

## Tool

**GitHub**: https://github.com/originalankur/maptoposter

### Quick Start
```bash
pip install -r requirements.txt
python create_map_poster.py --city "New York" --country "USA" --theme noir --distance 12000
```

### Useful Themes
- `noir` - Classic black/white
- `warm_beige` - Cozy feel
- `ocean` - Blues (good for coastal cities)
- `sunset` - Warm tones
- `japanese_ink` - Artistic style

### Distance Guide
- Neighborhood: 3000-5000m
- City center: 8000-12000m
- Metro area: 15000-20000m

## Poster Ideas

| City | Significance | Theme Idea |
|------|-------------|------------|
| New York City | Family adventures | noir or midnight_blue |
| | | |
| | | |

## Notes

- Output saved to `posters/` directory as PNG
- Can create custom themes via JSON
- Higher DPI (300) for print quality, lower (150) for previews
