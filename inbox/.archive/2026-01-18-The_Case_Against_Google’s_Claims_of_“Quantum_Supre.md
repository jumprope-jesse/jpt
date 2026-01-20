---
type: link
source: notion
url: https://gilkalai.wordpress.com/2024/12/09/the-case-against-googles-claims-of-quantum-supremacy-a-very-short-introduction/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-11T12:04:00.000Z
---

# The Case Against Google’s Claims of “Quantum Supremacy”: A Very Short Introduction. | Combinatorics and more

## Content (from Notion)

The 2019 paper “Quantum supremacy using a programmable superconducting processor” asserted that Google’s Sycamore quantum computer, with 53 qubits and a depth of 20, performed a specific computation in about 200 seconds. According to Google’s estimate, a state-of-the-art classical supercomputer would require approximately 10,000 years to complete the same computation.

The Google experiment had two major components:

1. The “Fidelity Claims”: Assertions regarding the fidelity of the samples produced by the quantum computer.
1. The “Supremacy Claims”: Assertions that translated fidelity into a measure of advantage over classical computation.
There are valid reasons to question both of these claims in the context of Google’s 2019 experiment. In my view, these claims may reflect serious methodological mistakes rather than an objective scientific reality. I do not recommend treating Google’s past or future claims as a solid foundation for policy-making decisions.

Below is a brief review of the case against Google’s 2019 claims of quantum supremacy:

A) The “Supremacy” Assertions: Flawed Estimation of Classical Running Time

A.1) The claims regarding classical running times were off by 10 orders of magnitude.

A.2) Moreover, the Google team was aware that better classical algorithms existed. They had developed more sophisticated classical algorithms for one class of circuits and subsequently changed the type of circuits used for the “supremacy demonstration” just weeks before the final experiment.

A.3) The 2019 Google paper states, “Quantum processors have thus reached the regime of quantum supremacy. We expect that their computational power will continue to grow at a double-exponential rate.” It is surprising to encounter such an extraordinary claim in a scientific paper.

### B) The “Fidelity” Assertions: Statistically Unreasonable Predictions Indicating Methodological Flaws

The google paper relies on a very simple a priori prediction of the fidelity based on the error-rates of individual components. (Formula (77).)

B.1) The agreement between the a priori prediction and the actual estimated fidelity is statistically implausible (“too good to be true”): It is unlikely that the fidelities of samples from hundreds of circuits would agree within 10-20% with a simple formula based on the multiplication of the fidelities of individual components. In my opinion, this suggests a methodologically flawed optimization process, such as the one described in item C.

B.2) The Google team provided a statistical explanation for this agreement based on three premises. The first premise is that the fidelities for the individual components are exact up to ±20%. The second premise is that this ±20% instability is unbiased. The third premise is that all these fidelities for individual components are statistically independent. These premises are unreasonable and they contradict various other experimental findings.

B.3) As of now, the error rates for individual components have not been released by the Google team. (Most recently, in May 2023, they promised “to push” for this data.) Analysis of the partial data provided for readout errors reinforces these concerns.

### C) The Calibration Process: Evidence of Undocumented Global Optimization

According to the Google paper, calibration was performed prior to running the random circuit experiments and was based on the behavior of 1- and 2-qubit circuits. This process involved modifying the definitions of 1-gates and 2-gates to align with how the quantum computer operates.

C.1) Statistical evidence suggests that the calibration process involved a methodologically flawed global optimization process. (This concern applies even to Google’s assertions about the fidelity of the smallest 12-qubit circuits.)

C.2) Non-statistical evidence also supports this claim. For example, contrary to the description provided by the Google team, it was revealed that they supplied an outdated calibration version (for the experimental circuits) to the Jülich Research Center scientists involved in the experiment. This calibration was later further modified after the experiment was conducted. (This discrepancy is also reflected in a video released by Google particularly between 2:13-3:07.)

C.3) The Google team has not disclosed their calibration programs, citing them as a commercial secret. For technical reasons, they were also unable to share the inputs for the calibration program, although they promised to do so in future experiments—a promise that has not yet been fulfilled.

A slide from my 2019 lecture “The Google quantum supremacy demo” (post), highlights that the error rates for two-qubit gates  have not yet been provided by the Google team as of today (Dec. 2024).

### D) Comparing Google with IBM

As far as we know, there is a significant gap (in favor of Google) between what IBM quantum computers—which are in some ways more advanced than Google’s quantum computers—can achieve for random circuit sampling and what Google claims, even for circuits with 7–12 qubits. While one might argue that Google’s devices or team are simply better, in my view, this gap more likely reflects methodological issues in Google’s experiments.

### E) (Not) Adopting Suggestions for Better Control

In our discussions with the Google team, they endorsed several of our suggestions for future experiments aimed at improving control over the quality of their experiments. However, in practice, later experiments did not implement any of these suggestions. Moreover, the structure of these later experiments makes them even harder to verify compared to the 2019 experiment. Additionally, unlike the 2019 experiment, the data for a subsequent random circuit sampling experiment does not include the amplitudes computed for the experimental circuits, further complicating efforts to scrutinize the results.

### F) My Personal Conclusion

Google Quantum AI’s claims (including published ones) should be approached with caution, particularly those of an extraordinary nature. These claims may stem from significant methodological errors and, as such, may reflect the researchers’ expectations more than objective scientific reality. I do not recommend treating Google’s past or future claims as a solid basis for policy-making decisions.

### G) Remarks

G.1) Google’s supremacy claims (from the 2019 paper) have been refuted in a series of papers by several groups. This began with work by IBM researchers Pednault et al. shortly after Google’s original paper was published and continued with studies by Pan and Zhang; Pan, Chen, and Zhang; Kalachev, Panteleev, and Yung; Gao et al.; Liu et al.; and several other groups. For further details, see this post and the associated comment section, as well as this post.

G.2) Google now acknowledges that using the tensor network contraction method, their 2019 53-qubit result can be computed classically in less than 200 seconds. However, in their more recent 2023/24 paper, “Phase Transitions…” (see Table 1), they claim that with 67 to 70 qubits, classical supercomputers would require many years to generate 1 million such bitstrings, even with tensor network contraction.

G.3) Items B) and C) highlights methodological issues with Google’s fidelity assertions, even for 12-qubit circuits. These concerns persist independently of the broader question of quantum supremacy for larger circuits, where the fidelity assertions are taken at face value.

G.4) For a more comprehensive view of our study of Google’s fidelity claims, refer to the following papers:

- Y. Rinott, T. Shoham, and G. Kalai, Statistical Aspects of the Quantum Supremacy Demonstration, (2020) Statistical Science (2022)
- G. Kalai, Y. Rinott and T. Shoham, Google’s 2019 “Quantum Supremacy” Claims: Data, Documentation, & Discussion (2022) (see this post).
- G. Kalai, Y. Rinott and T. Shoham, Questions and Concerns About Google’s Quantum Supremacy Claim (2023) (see this post).
- G. Kalai, Y. Rinott and T. Shoham, Random circuit sampling: Fourier expansion and statistics. (2024) (see this post)
These papers describe an ongoing project with Yosi Rinott and Tomer Shoham, supported by Ohad Lev and Carsten Voelkmann. Together with Carsten, we plan to expand our study and apply our tools to other experiments. Additionally, see my earlier paper:

- G. Kalai, The argument against quantum computers, the quantum laws of nature, and Google’s supremacy claims, (2020) The Intercontinental Academia Laws: Rigidity and Dynamics (M. J. Hannon and E. Z. Rabinovici, eds.), World Scientific, 2024. arXiv:2008.05188.
G.5) There is also supporting evidence for Google’s 2019 claims, such as a 2020 replication by a group from the University of Science and Technology of China (USTC) and later verifications of some of Google’s fidelity estimations.

G.6) There are some additional concerns regarding the Google experiment. In particular, there are problematic discrepancies between the experimental data, the Google noise model, and simulations.

G.7) In my opinion, the main current challenge for experimental quantum computing is to improve the quality of two-qubit gates and other components, as well as to carefully study the quality of quantum circuits in the 5–20 qubit regime. Experiments on quantum error correction for larger circuits are also important.

### H) Hype and Bitcoin

I usually don’t mind “hype” as a reflection of scientists’ enthusiasm for their work and the public’s excitement about scientific endeavors. However, in the case of Google, some caution is warranted, as the premature claims in 2019 may have had significant consequences. For example, following the 2019 “supremacy” announcement, the value of Bitcoin dropped (around October 24, 2019, after a period of stability) from roughly $9,500 to roughly $8,500 in just a few days, representing a loss for investors of more than ten billion dollars. (The value today is around $100,000.) Additionally, Google’s assertions may have imposed unrealistic challenges on other quantum computing efforts and encouraged a culture of undesirable scientific methodologies.


