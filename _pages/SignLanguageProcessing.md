---
layout: archive
title: "Sign Language Processing"
permalink: /SignLanguageProcessing/
author_profile: true
---

{% include base_path %}

Sign languages are fully natural, visually expressed languages with rich grammatical structure. Unlike spoken language, they unfold in three-dimensional space through coordinated use of the hands, arms, body posture, and facial expressions. Each country or region typically has its own sign language — Norwegian Sign Language (NTS), British Sign Language (BSL), Sign Language of the Netherlands (NGT), and American Sign Language (ASL) are among the hundreds that exist worldwide, none of which are mutually intelligible.

**Sign Language Processing (SLP)** is the subfield of AI concerned with the automatic analysis and generation of sign language. It encompasses several core tasks:

### Recognition
**Isolated Sign Recognition (ISR)** classifies individual signs from video or motion-capture data. **Continuous Sign Language Recognition (CSLR)** transcribes connected, continuous signing into a gloss sequence without relying on sentence boundaries — a substantially harder problem due to coarticulation, signer variation, and the need to segment an unsegmented signal.

### Translation and Interpretation
**Sign Language Translation (SLT)** maps a sign language utterance to a spoken/written language sentence, requiring cross-modal and cross-lingual transfer. Unlike ISR/CSLR, SLT must capture meaning rather than surface form.

### Production and Generation
**Sign Language Production (SLP)** generates sign language from text, typically via skeletal avatar animation or video synthesis. This includes **pose estimation**, **motion synthesis**, and increasingly **diffusion-based video generation**.

### Linguistic Grounding
SLP research increasingly draws on formal sign linguistics: **phonology** (handshape, location, movement, orientation, non-manual markers), **morphology** (agreement verbs, spatial grammar), and **discourse structure** (topic-comment, role shift, classifier predicates). Linguistically-informed representations consistently outperform purely data-driven baselines on low-resource benchmarks.

---

## Challenges

- **Data scarcity**: Sign language datasets are orders of magnitude smaller than their spoken-language counterparts, due to high annotation cost and the need for expert signers and linguists.
- **Signer variation**: Signing style varies significantly across individuals, regions, and registers.
- **Modality gap**: Video-based methods must bridge high-dimensional visual input to discrete linguistic units.
- **Lack of standardisation**: No universally agreed annotation schemes or evaluation protocols exist across sign languages.

---

## Selected Resources

| Resource | Description |
|---|---|
| [BOBSL](https://www.robots.ox.ac.uk/~vgg/data/bobsl/) | Large-scale British Sign Language corpus from broadcast TV |
| [PHOENIX-2014T](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/) | German Sign Language weather broadcast corpus; standard CSLR/SLT benchmark |
| [3D-LEX](https://aclanthology.org/2024.signlang-1.33/) | 3D motion-capture lexicons for ASL and NGT |
| [NGT200](https://openreview.net/forum?id=idkNzTC67X) | Multi-view isolated sign dataset for NGT with geometric annotations |
| [WMT-SLP](https://www.wmt-slt.com/) | Annual shared task on sign language translation |

---

> "Without sign language, Deaf people are not equal." — L. Kozik, Human Rights Watch, 2019
