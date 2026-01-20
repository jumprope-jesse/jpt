# Automotive Lidar Technology

Reference: https://www.viksnewsletter.com/p/short-intro-to-automotive-lidar

## How It Works
Lidar (Light Detection and Ranging) uses infrared laser light to measure distances to objects.

### Wavelengths
- **905 nm**: More sensitive detectors, cheaper, but eye safety concerns and sunlight interference
- **1550 nm**: Better eye safety, lower solar interference, longer range, but poor in wet conditions (water vapor absorption)

### Ranging Techniques
- **Direct Time-of-Flight (dToF)**: Emits pulses, measures reflection time. 100-200m range. Most common.
- **FMCW**: Modulates laser frequency to measure distance AND velocity simultaneously. Lower peak power needs.

## System Types

### Mechanical
- **Scanning Lidar**: Rotating laser, 360° coverage, costly/bulky (e.g., Waymo's Laser Bear Honeycomb)
- **MEMS-Mirror**: Oscillating micro-mirrors, lower cost via CMOS fabrication, mature tech

### Solid-State
- **Flash Lidar**: Illuminates entire scene at once using VCSELs + SiPM arrays. 30fps, no moving parts, reduced FOV.
- **Optical Phased Arrays (OPA)**: Silicon photonics, electronically steered beams. Still research phase. Thermal challenges.

## Industry State (2024)
- 140+ startups pursuing cost reduction
- Mechanical systems cost thousands of dollars
- Price must drop significantly for mass market adoption
- Key players: Waymo (mechanical), Ouster (850nm), Analog Photonics (OPA from MIT)
