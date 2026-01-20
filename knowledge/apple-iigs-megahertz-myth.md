# Apple IIGS Megahertz Myth - Debunked

Source: Userlandia (https://www.userlandia.com/home/iigs-mhz-myth)

## The Myth
Popular claim: Apple intentionally limited the Apple IIGS's CPU clock speed (2.8 MHz) to avoid competition with the Macintosh, supposedly at Steve Jobs' direction.

## Why It's Wrong

### Timeline Problem
- Steve Jobs lost all power at Apple in May 1985 after executive turmoil
- IIGS didn't launch until 16 months later (September 1986)
- Jobs couldn't have "hobbled" something he had no control over

### The Real Reasons for 2.8 MHz

**1. CPU Availability Issues**
- Apple IIx project (1983-84) was cancelled partly because 65C816 chips were buggy and late
- WDC promised 8MHz chips but couldn't deliver - 4MHz was barely achievable
- GTE (the manufacturer) struggled with yields on faster chips

**2. REP/SEP Opcode Timing Problems**
- The 65C816's REP (Reset Status Bits) and SEP (Set Status Bits) opcodes had timing issues at higher speeds
- These problems worsened at smaller process nodes
- Accelerator cards like TransWarp GS needed special GAL logic to stretch clock cycles for these opcodes

**3. Manufacturing Yields**
- GTE's 3-micron process couldn't reliably produce 4MHz chips in volume
- Many IIGSes shipped with 3MHz chips (unofficial rating for chips that failed 4MHz binning)
- Dave Haynie (Amiga engineer) confirmed in 1990: "Apple managed to get enough for the IIGS by actually having a special 2.8MHz version tested"

**4. Clock Source Architecture**
- IIGS derives clock from 28.636 MHz crystal oscillator (NTSC colorburst multiple)
- FPI chip divides by 5 to get 2.8 MHz
- A 1/4 divider would give 3.58 MHz, but reliable chips weren't available

## Key Players

**Steve Wozniak** - Predicted 8MHz 65816 would "beat the pants off the 68000" in Jan 1985 Byte interview. Left Apple Feb 1985 before IIGS shipped.

**Bill Mensch (WDC)** - Designed the 65C816. Had famous confrontation with Jean-Louis Gassee at 1989 AppleFest, claiming he had 12MHz chips if Apple would order them. Reality: having samples ≠ production volume.

**Tony Fadell** - Before iPod fame, founded ASIC Incorporated as a college student. Reverse-engineered 65816 using gate arrays, promised 20MHz speeds. Sold some chips but never reached production scale.

## The Accelerator Era
- TransWarp GS (1989) - 7MHz, struggled with chip supply
- ZipGSX (1990) - Also 7MHz
- Both needed special logic to handle REP/SEP timing issues
- 14MHz Sanyo-fabbed chips finally solved problems in 1992 (with completely new layout)

## Broader Lessons

1. **Corporate conspiracy theories are appealing but often wrong** - Real explanations involve boring things like yields, process nodes, and opcode timing
2. **"Should be available" does a lot of heavy lifting** - Chip roadmaps often miss reality
3. **Platform architecture creates hard ceilings** - Mega II compatibility dragged the whole system down
4. **Memory speed matters** - Even with faster CPUs, period memory couldn't keep up

## Interesting Side Notes

- Super NES used 65816 (Ricoh 5A22) at 3.56 MHz - sold 50M units vs ~1.25M IIGSes
- Apple's Mobius project (1986-87) explored ARM2-based Apple II successor
- That ARM exploration eventually led to Newton partnership and today's Apple Silicon

## The Real Neglect
Apple did neglect the IIGS - just not by artificially limiting clock speed. The neglect was:
- Underfunding marketing vs Mac
- Cancelling Mark Twain revision (1991)
- No meaningful speed improvements in ROM 03 update
- IIe card for Mac LC undermined remaining market
