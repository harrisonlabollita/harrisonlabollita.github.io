---
layout: page
title: Research
permalink: /research/
standfirst: >-
  Designing and understanding quantum materials from first principles. 

# Rendered as the "on this page" index. Anchors must match the <h2 id="…"> below.
contents:
  - title: Quantum embedding
    anchor: embedding
  - title: Predicting experiments
    anchor: experiment
  - title: Materials
    anchor: materials
  - title: Software
    anchor: software
  - title: Output
    anchor: output
---

Designing and understanding quantum materials from first principles is the
overarching goal of my research. Quantum materials — unconventional
superconductors, strongly correlated metals, exotic magnets, and topological
materials — host emergent phenomena arising from electronic interactions,
topology, and their interplay, with profound implications for both fundamental
physics and future technologies. Predicting these phenomena in real materials
remains one of the biggest challenges in condensed matter physics.


<h2 id="embedding">Quantum embedding</h2>

Quantum embedding methods provide a practical route for dealing with strong
correlation physics at the first-principles scale. The central idea is to partition the electronic degrees of freedom 
into a weakly correlated environment, which can be treated using a comparatively inexpensive approximation, and an active correlated subspace, which is treated using a higher-level many-body method. The two descriptions are coupled through an embedding and a self-consistency condition. A particularly successful realization of this idea is the combination of density-functional theory (DFT) and dynamical mean-field theory (DMFT) ([Georges et al., Rev. Mod. Phys. 68, 13 (1996)](https://doi.org/10.1103/RevModPhys.68.13)). 

Dynamical mean-field theory replaces the lattice problem with a single impurity site 
(usually an atom or a couple of atoms) exchanging electrons with a self-consistent bath. 
Using this method with electronic codes is a significant software engineering challenge. 
To address this software challenge, I've led the development of [ModEST]({{ '/software/' | relative_url }}), a 
modular electronic structure toolkit designed for generic quantum embedding calculations of quantum materials.

<h2 id="experiment">Predicting what experiments measure</h2>

Understanding, interpreting, and predicting experiments is central to my research program.
The ultimate test of a microscopic theory is whether it reproduces what 
an experiment actually measures. Some recent experiment–theory collaborations that we've 
worked on:

- **Resistivity** — DFT+DMFT accounts quantitatively for the Fermi-liquid
  T² resistivity of high-conductivity correlated metals, and, once
  electron-phonon coupling is included, for the unconventional resistivity of
  moderately correlated perovskite oxides
  ([PRB 113, L081105](https://doi.org/10.1103/f4p8-5xb8),
  [PRB 113, 085125](https://doi.org/10.1103/71c6-sb7v),
  [PRL 136, 216301](https://journals.aps.org/prl/abstract/10.1103/vjb8-qghf)).
- **Spin and charge excitations** — how capping layers reshape the excitation
  spectrum of parent and superconducting Nd₁₋ₓSrₓNiO₂
  ([PRL 133, 206501](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.206501)).
- **Optical conductivity** — the electronic layer decoupling driven by
  density-wave order in La₄Ni₃O₁₀
  ([PRL 136, 216501](https://journals.aps.org/prl/abstract/10.1103/qgl1-zh9f)).
- **Phonons** — lattice–charge coupling in a trilayer nickelate with
  intertwined density-wave order
  ([PRX 16, 011013](https://doi.org/10.1103/s5j9-cbg7)).
- **Seebeck coefficient** — the band structure of a superconducting nickelate,
  read out thermoelectrically in the disordered limit
  ([PRX 14, 041021](https://doi.org/10.1103/PhysRevX.14.041021)).
- **Superconducting phase diagram** — the full multilayer square-planar
  nickelate family, from synthesis through to T<sub>c</sub>
  ([Science 392, 1390](https://www.science.org/doi/abs/10.1126/science.adp4440)).


<h2 id="materials">Materials</h2>

Quantum embedding methods are general and can be applied to a number of materials classes. Here
are some applications so far:

- **Nickel oxides** — square-planar and Ruddlesden-Popper families, from the
  correlated electronic structure of individual compounds to the multilayer
  superconducting phase diagram
  ([Science 392, 1390](https://www.science.org/doi/abs/10.1126/science.adp4440),
  [Nature Materials 21, 160](https://doi.org/10.1038/s41563-021-01142-9)).
- **Perovskite oxides** — cubic perovskites as a clean testbed for correlated
  transport; the resistivity work [above](#experiment).
- **Kagomé metals** — Van Hove singularities in AV₃Sb₅ under pressure and doping
  ([PRB 104, 205129](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.205129)).
- **Twisted and low-dimensional magnets** — moiré skyrmions in CrX₃ bilayers
  ([Nano Letters 21, 6633](https://doi.org/10.1021/acs.nanolett.1c02096)).
- **Frustrated oxides** — the polaronic ground state of LiTi₂O₄
  ([Nature Communications 17, 1303](https://www.nature.com/articles/s41467-025-68068-7)).

<h2 id="software">Software</h2>

Quantum embedding calculations require the combination of electronic structure
and many-body methods. In general, this combination is a significant software
engineering effort.

[ModEST]({{ '/software/' | relative_url }}), a modular electronic structure
toolkit, is built as a state-of-the-art library for generic quantum embedding calculations 
of quantum materials. It is open source and built to be user-friendly for both experts and 
researchers just getting started.

<h2 id="output">Research output</h2>

{% include metrics.html %}

<p class="section__more">
  <a href="{{ '/publications/' | relative_url }}">Publications &rarr;</a>
  &nbsp;·&nbsp;
  <a href="{{ '/software/' | relative_url }}">Software &rarr;</a>
</p>
