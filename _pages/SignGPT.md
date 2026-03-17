---
layout: archive
title: "SignGPT and the Visual Language Toolkit"
permalink: /SignGPT/
author_profile: true
description: "SignGPT and the Visual Language Toolkit — Oline Ranum's contribution to the LREC 2026 Sign Language Workshop paper on linguistically grounded BSL processing."
---

{% include base_path %}

<table style="border-collapse: collapse; border: none; width: 100%; margin-bottom: 1.5em;" border="0">
<tr>
<td style="border: none; width: 140px; vertical-align: middle; padding-right: 20px;">
<img src="/images/blog/publications/signGPT/projectlogo.png" alt="SignGPT project logo" style="width: 130px; height: auto;">
</td>
<td style="border: none; vertical-align: middle;">
<span style="font-size: 0.95em; color: #444;">
<strong>Brown, M., Ranum, O., Fish, E., Proctor, H., Woll, B., Bowden, R., Cormier, K.</strong><br>
12th Workshop on the Representation and Processing of Sign Languages: Language in Motion<br>
<em>LREC 2026 · Palma de Mallorca, Spain · 16 May 2026</em>
</span>
</td>
</tr>
</table>

[📄 Paper (PDF)](/images/blog/publications/signGPT/SignGPTpaper.pdf){:target="_blank"} &nbsp;·&nbsp; [🌐 SignGPT Project](https://sites.google.com/view/signgpt){:target="_blank"}

---

## Overview

SignGPT is a UKRI EPSRC Programme Grant (University of Surrey, University of Oxford, and University College London) building the first generative predictive transformer for bidirectional translation between British Sign Language (BSL) and English. A central component of this effort is the **Visual Language Toolkit (VLT)** — a modular suite of semi-automatic annotation and recognition tools designed to scale linguistically grounded BSL corpora without sacrificing linguistic validity.

This paper presents both the motivation for the VLT and its current capabilities, covering sign segmentation, sign spotting, non-manual feature tracking, and 3D signer reconstruction.

---

## The Data Problem in Sign Language Processing (Section 2)

My contribution to this paper is Section 2, which frames the core linguistic and data challenges that motivated the VLT's design. The argument is that progress in Sign Language Processing (SLP) is fundamentally constrained not just by the scale of available data, but by its **ecological validity** — whether the data actually reflects how sign languages are used in everyday, naturalistic communication.

### Why existing data falls short

The vast majority of SLP datasets are built from interpreted broadcast media, social media, or captions. While these sources are scalable, they introduce systematic biases:

- **Interpreted signing** is produced under live broadcast constraints and differs substantially from everyday Deaf communication. Interpreters routinely omit, simplify, and restructure signing relative to the spoken source, making the resulting material a poor proxy for naturalistic language.
- **Social media and web-scraped content** raises ethical concerns around consent, copyright, and unknown signer proficiency — and captions are typically not verbatim representations of the signing.

The result is that current benchmarks measure performance on data that diverges from real-world signing in ways that are rarely acknowledged in model evaluation.

### Why glosses are not enough

Most SLP systems use **gloss annotations** — approximate word-level transcriptions of manual signs — as the primary supervision signal. This is both useful and fundamentally limiting:

- A single sign form can carry multiple meanings depending on context (polysemy), and sociolinguistic variation means the same concept may be realised differently across signers (Stamp et al., 2014).
- Glosses collapse **productive constructions** — pointing, depicting signs, spatial indexing, classifiers — into coarse categories or ignore them entirely, even though these constructions are central to BSL grammar.
- Roughly **60% of spontaneous BSL consists of non-lexical elements** (Fenlon et al., 2014): brow raises, eye gaze, mouthings, head movements, and body posture that interact simultaneously across multiple articulators to convey grammatical and prosodic meaning.

<figure style="margin: 1.5em 0;">
<img src="/images/blog/publications/signGPT/figure6.png" alt="Predicted non-manual articulations — lip movement, head nod, head shake, gaze, eye blink detection" style="width: 100%; max-width: 520px; height: auto;">
<figcaption style="font-size: 0.88em; color: #555; margin-top: 0.4em;">Predicted non-manual articulations based on keypoints extracted from the method described in Liu et al. (2025). These features — lip movement, head nods, gaze direction, and eye blinks — are grammatically significant in BSL but absent from gloss-based supervision.</figcaption>
</figure>

### The simultaneity problem

Sign languages are not simply sequences of discrete manual signs. Grammatical information is distributed **simultaneously** across multiple articulators rather than encoded sequentially. The linear, token-based modelling paradigms inherited from spoken-language NLP are a poor structural match for this:

- Signed grammatical structures may map onto multiple spoken-language sequences, and vice versa — making n-gram metrics like BLEU a poor fit for evaluation.
- Gloss strings and caption-aligned tokens introduce an **information bottleneck** that obscures spatial grammar, productive constructions, and flexible constituent ordering.

### Towards real-world generalisation

Addressing these issues requires data that is fluent, naturalistic, and Deaf-produced — along with annotation tools that can scale to such data without relying on costly expert annotation at every step. This motivates the VLT's design: semi-automatic glossing tools, dense temporal segmentation, and linguistically principled evaluation methods that go beyond surface-level sign-to-text matching.

---

## The Visual Language Toolkit

The VLT provides practical infrastructure for the annotation and analysis described above:

<table style="border-collapse: collapse; border: none; width: 100%;" border="0">
<tr>
<td style="border: none; width: 48%; vertical-align: top; padding-right: 16px;">

<figure>
<img src="/images/blog/publications/signGPT/figure1.png" alt="Sign segmentation accuracy on MeinDGS — BIO labelling showing success, over-segmentation, and under-segmentation cases" style="width: 100%; height: auto;">
<figcaption style="font-size: 0.88em; color: #555; margin-top: 0.4em;"><strong>Segmentation tool:</strong> BIO boundary prediction on the MeinDGS dataset, including success, over-segmentation, and under-segmentation cases.</figcaption>
</figure>

</td>
<td style="border: none; width: 48%; vertical-align: top; padding-left: 16px;">

<figure>
<img src="/images/blog/publications/signGPT/figure2.png" alt="Sign segmenter and sign spotter VLT interface — video with predicted segments and ranked candidate signs" style="width: 100%; height: auto;">
<figcaption style="font-size: 0.88em; color: #555; margin-top: 0.4em;"><strong>Sign spotting tool:</strong> Combined segmentation and spotting interface, comparing segments against a reference dictionary using SignRep embeddings.</figcaption>
</figure>

</td>
</tr>
</table>

The **segmentation tool** identifies temporal sign boundaries in continuous video using a self-attention model over body and hand features (He et al., 2025), achieving up to 85% accuracy on annotated datasets. The **sign spotting tool** builds on SignRep (Wong et al., 2025), a masked autoencoder trained on skeletal features, to embed and compare sign segments against reference dictionaries in a signer-invariant latent space.

Additional tools include 3D body pose and hand reconstruction, facial landmark tracking for non-manual feature detection, and signer anonymisation via differentiable re-skinning — all designed to interoperate with ELAN annotation files and expose a Python API.

<figure style="margin: 1.5em 0;">
<img src="/images/blog/publications/signGPT/figure5.png" alt="Re-skinning a signer into a continuous sequence using SMPL body meshes and Guava Gaussian splatting" style="width: 100%; max-width: 480px; height: auto;">
<figcaption style="font-size: 0.88em; color: #555; margin-top: 0.4em;">Signer anonymisation and avatar driving via SMPL mesh reconstruction and Gaussian splatting — enabling privacy-preserving dataset expansion and sign language production.</figcaption>
</figure>

---

## Links

[📄 Paper (PDF)](/images/blog/publications/signGPT/SignGPTpaper.pdf){:target="_blank"} &nbsp;·&nbsp; [🌐 SignGPT Project](https://sites.google.com/view/signgpt){:target="_blank"}
