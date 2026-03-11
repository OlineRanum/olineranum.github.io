---
layout: archive
title: "Sign Language Processing"
permalink: /SignLanguageProcessing/
author_profile: true
---

{% include base_path %}

Sign languages are fully natural, visually expressed languages with rich grammatical structure. Unlike spoken language, they unfold in three-dimensional space through the coordinated use of hands, arms, body posture, and facial expressions. Each country or region typically has its own sign language — Norwegian Sign Language (NTS), British Sign Language (BSL), Sign Language of the Netherlands (NGT), and American Sign Language (ASL) are among the hundreds worldwide, none of which are mutually intelligible.

**Sign Language Processing (SLP)** is the subfield of AI concerned with the automatic analysis and generation of sign language. It sits at the intersection of computer vision, natural language processing, and sign language linguistics.

---

## Core Tasks

**Sign Language Recognition (SLR)** maps signed video or pose data to linguistic representations. *Isolated Sign Recognition (ISR)* classifies individual signs from segmented clips. *Continuous Sign Language Recognition (CSLR)* transcribes connected signing into a gloss sequence without predefined boundaries — substantially harder due to coarticulation, signer variation, and unsegmented input.

**Sign Language Translation (SLT)** maps a sign language utterance to a spoken or written language sentence, requiring cross-modal and cross-lingual transfer. Historically framed as a recognition-then-translation pipeline, recent work increasingly pursues *gloss-free* end-to-end approaches that model sign-to-text directly.

**Sign Language Production (SLP/G)** generates sign language from text, typically via pose synthesis or photorealistic video generation. This encompasses motion synthesis, avatar animation, and increasingly diffusion-based approaches. Despite the name, it is a translation task in the opposite direction from SLT.

**Other tasks** include *sign segmentation* (identifying temporal boundaries in continuous signing), *sign spotting* (locating specific signs within a stream), *signer anonymisation*, and *sign-text alignment* for corpus annotation.

---

## Beyond the Lexicon

A key challenge — and active research frontier — is that sign languages are not purely lexical. In spontaneous signing, roughly 40% of signs are *non-lexical*, consisting of **productive constructions** that exploit three-dimensional space, iconicity, and discourse context. These include:

- **Spatial indexing** (pointing): signers assign discourse entities to spatial loci and later re-reference them through pointing — a pronominal and locative mechanism embedded in space rather than form.
- **Depicting signs**: handshape, location, and movement together encode the shape, size, or path of a referent.
- **Non-manual features**: brow movements, mouthings, head tilt, and gaze contribute grammatical, prosodic, and discourse-level information simultaneously with manual signs.

Most current benchmarks and models treat signing as a linear sequence of glosses, implicitly assuming a discrete and finite lexicon. This misses the spatial grammar and simultaneity that are central to how sign languages actually work.

---

## Current Trends

- **Gloss-free translation**: moving from gloss-label intermediates toward direct sign-to-text models using large language models and self-supervised pretraining.
- **Large-scale models**: scaling sign language models (Uni-Sign, SignRep, SIGN2GPT) on internet and broadcast data, analogous to LLMs in spoken NLP.
- **Geometric and 3D representations**: using body mesh reconstruction (SMPL) and 3D hand pose (WiLoR/HaMeR) to encode spatial grammar more faithfully than 2D skeletons.
- **Non-lexical modelling**: explicit treatment of pointing, depicting signs, and non-manual features — moving beyond lexicon-centric supervision.
- **Community and ethics**: growing awareness of the need for deaf-led evaluation, consent in data collection, and ecologically valid training data beyond interpreted broadcasts.

---

## Key Challenges

- **Data scarcity**: sign language datasets are orders of magnitude smaller than spoken-language counterparts, due to high annotation cost and the absence of a written form.
- **Annotation bottleneck**: gloss annotation requires linguists and fluent signers; only a fraction of existing corpora is annotated at all.
- **Simultaneity vs. linearity**: sign languages express meaning simultaneously across multiple articulators, which does not map cleanly onto the sequential assumptions of standard NLP pipelines.
- **Ecological validity**: most large-scale training data comes from interpreted broadcast or social media, which differs systematically from natural, spontaneous signing.
- **Evaluation**: automatic metrics like BLEU do not capture the flexible word order, spatial grammar, or productive constructions of sign languages well.
