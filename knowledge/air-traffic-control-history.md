# Air Traffic Control History

## Source
- [Air Traffic Control](https://computer.rip/2025-05-11-air-traffic-control.html) by J.B. Crawford
- computer.rip newsletter (excellent tech history writing)
- Added: 2026-01-18

## Key Themes

ATC exemplifies how complex systems evolve through necessity rather than design. Its development was shaped by:
- Military technology hand-me-downs (radar, GCI)
- Reactive responses to disasters (1956 Grand Canyon collision, 1958 Nevada collision)
- Bureaucratic fragmentation (FSS vs ATC, military vs civilian)
- Underinvestment and regulatory capture

## Timeline

### 1910s-1920s: Aviation Radio
- 1913: US Army Signal Corps experiments with aircraft radio
- WWI: Ground control emerges for reconnaissance coordination
- Post-war: Airlines adopt radio for schedule/weather coordination
- 1920: Transcontinental Air Mail route (NYC to SF in 33 hours via relay)
- Post Office builds 17 Air Mail Radio Stations along transcontinental route

### 1926-1940s: Government Takes Over
- 1926: Watres Act creates Aeronautic Branch (Dept of Commerce)
- Air Mail Radio Stations become **Flight Service Stations** (FSS)
- 1935: First en-route ATC center opens in Newark (airline-owned)
- 1936: Bureau of Air Commerce takes ownership of control centers
- Controllers use **flight strips** (paper slips with flight info) and plotting tables

### 1940s-1950s: Radar Revolution
- WWII: British invent radar/magnetron (treated as secret as nukes)
- **Ground-Controlled Interception (GCI)**: Ground observers direct aircraft via radio
- **Plan Position Indicator (PPI)**: The familiar circular radar scope
- 1955: ARTCCs adopt "Air Route Traffic Control Center" name, install radar
- Controllers replace plotting tables with PPI displays, still push markers

### 1958: FAA Created
- 1956: 128 die in Grand Canyon mid-air collision
- 1958: 49 die when military fighter hits airliner over Nevada
- **FAA created** with authority over both civil AND military aviation
- This was revolutionary: unified all US airspace under one system
- Project Beacon report recommends computer automation

### 1950s-1960s: SAGE and Failed Integration
- **SAGE** (Semi-Automated Ground Environment): Air Force's computerized air defense
  - Lincoln Labs + IBM + Air Force
  - First large-scale networked computer system
  - Direction centers on Air Force bases
- **SATIN** (SAGE Air Traffic Integration): Planned upgrade to add ATC functions
  - Would put SAGE consoles in ARTCCs
  - Canceled 1960 due to cost overruns
- FAA left in the lurch, starts own automation program
- Solution: "buy their own SAGE" - National Airspace System En Route Stage A
- Uses IBM System/360 (off-the-shelf vs SAGE's bespoke AN/FSQ-7)

## Flight Service Stations: The Odd Survivor

FSS have never gone away despite being obsolete:
- Originally Post Office Air Mail stations (1920s)
- Transferred: Post Office → CAB → CAA → FAA → Leidos (2005)
- Still provide weather briefings, flight plan filing
- Play "go-between" for ATC in remote areas
- Privatized to Leidos in 2005, now single centralized facility
- Expected to sunset with current staff (no new hires)
- Fun URL: 1800wxbrief.com (phone number domain!)

## Institutional Schisms

### FSS vs ATC
- Different departments, facilities, functions, practices
- Both provide weather info: 1800wxbrief.com vs aviationweather.gov vs weathercams.faa.gov
- Three competing government/contractor weather portals

### Military vs Civilian
- Pre-1958: Completely separate, no coordination
- Post-1958: Unified under FAA (with military privileges like transponder exemptions)
- SAGE was purely military; sharing with ATC failed politically

## Lessons for Software/Organizations

1. **Systems trail necessity**: ATC perpetually behind the need, reactive to disasters
2. **Military tech cascade**: GCI → radar → PPI → modern ATC all military origins
3. **Bureaucratic fragmentation persists**: FSS/ATC split survives 90+ years
4. **Grand unification is rare**: 1958 FAA creation was exceptional
5. **Procurement kills innovation**: SATIN canceled due to cost spiral
6. **Legacy lives forever**: Flight strips still in use today

## Related
- [[complex-systems-failure]] - ATC as a complex system running in degraded mode
- [[us-digital-service-history]] - Government technology modernization challenges

## Author
J.B. Crawford writes excellent tech infrastructure history at computer.rip. Also covers:
- Telecom history
- Nuclear infrastructure
- Government computing systems
