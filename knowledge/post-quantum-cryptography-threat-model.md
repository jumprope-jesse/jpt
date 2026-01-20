# Post-Quantum Cryptography: Google's Threat Model

Source: Google Bug Hunters Blog (early 2024)
https://bughunters.google.com/blog/5108747984306176/google-s-threat-model-for-post-quantum-cryptography

## The Core Threat

**Store-Now-Decrypt-Later (SNDL)**: Attackers can store encrypted communications today and decrypt them once cryptographically relevant quantum computers (CRQC) exist. This makes PQC migration urgent even though CRQCs are 10-15 years away.

## How Quantum Breaks Cryptography

| Algorithm | What It Attacks | Impact |
|-----------|-----------------|--------|
| **Shor's** | Factoring integers, discrete logarithms | Breaks RSA, ECDH, ECDSA |
| **Grover's** | Black-box function inversion | Theoretically halves symmetric key strength, but infeasible in practice |

**Safe**: Symmetric cryptography (AES, etc.) is NOT practically impacted by quantum computers.

## NIST-Standardized PQC Algorithms

| Algorithm | FIPS | Type | Key Size | Signature/Ciphertext |
|-----------|------|------|----------|---------------------|
| ML-KEM (Kyber) | 203 | Key encapsulation | ~1.5 KB | ~1 KB |
| ML-DSA (Dilithium) | 204 | Signatures | ~2 KB | ~3.3 KB |
| SLH-DSA (SPHINCS+) | 205 | Signatures (hash-based) | ~64 B | ~17-50 KB |

**Key trade-off**: PQC signatures are MUCH larger than classical. A single Dilithium3 signature + public key exceeds 5 KB.

## Use Case Prioritization

### 1. Encryption in Transit (URGENT)
- TLS, SSH, Signal, MLS, ALTS
- Vulnerable to SNDL attacks NOW
- **Recommendation**: Kyber768 hybrid with X25519 or P256
- Good news: Limited number of stacks, ephemeral keys, already rolling out

### 2. Firmware Signatures (URGENT)
- Public keys burned into silicon, can't be changed
- Devices with 10+ year lifespans need PQC NOW
- **Recommendation**: SPHINCS+ (SLH-DSA)

### 3. Software Signatures (Relaxed timeline)
- Binaries, source code signing for secure boot
- Keys can be updated, relies on lower-level signatures
- **Recommendation**: Dilithium3 hybrid with ECDSA/EdDSA/RSA, or SPHINCS+

### 4. PKI (Problematic)
- Certificate chains multiply the size problem
- Single Dilithium3 sig + pubkey > 5 KB
- Some devices fail when packets exceed 10-30 KB
- **Status**: Active research, no clear solution yet

### 5. Tokens/JWTs (Problematic)
- Cookie limit: 4096 bytes total
- Dilithium3 sig alone: 3309 bytes (binary), 4412 bytes (base64)
- **Recommendation**: Move to stateful tokens where possible

## Hybrid Deployment

**Always use hybrid mode**: Combine classical + PQC algorithms so attacker must break BOTH.

Rationale: PQC algorithms are less mature than classical crypto. Hybrid provides defense-in-depth while the algorithms mature.

## Threat Actors & Timeline

### Who Gets CRQC First?
**Nation states** - most likely first operators, will use deniably to avoid revealing capabilities. Initial targets:
- Other nations' cloud deployments
- Political dissidents
- Infrastructure providers

### Timeline Estimates (Global Risk Institute)
- 10-15 year window for cryptographically relevant quantum computers
- Significant improvements expected by 2030 (good checkpoint)
- Financially motivated attackers (ransomware) become relevant when quantum computing is commercially accessible

## Regulatory Landscape

- **US**: Executive orders requiring PQC adoption
- **CNSA 2.0**: Requires PQC on short timelines
- **FIPS**: Standards being updated
- **Europe**: BSI and ANSSI requesting PQC roadmaps

## What Requires More Research

- PKI with certificate chains (size explosion)
- Stateless tokens (size constraints)
- "Fancy" cryptography: blind signatures, OPRF, other privacy-preserving techniques
- Hardware roots of trust (security keys, TPMs) with hardware constraints

## Key Takeaways

1. **Symmetric crypto is fine** - Don't panic about AES
2. **Start with key agreement** - Kyber hybrid for TLS/SSH is the immediate priority
3. **Signatures can wait** - Except for firmware with long device lifespans
4. **PKI is the hard problem** - No good solution yet for certificate chains
5. **Hybrid deployment is essential** - Never deploy PQC-only

---

See also: [[quantum-computing-fundamentals]], [[quantum-supremacy-skepticism]]
