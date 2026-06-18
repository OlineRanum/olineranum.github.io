---
title: 'BackTranslation2.0 accepted at ECCV 2026'
date: 2026-06-18
permalink: /posts/backtranslation2/
tags:
  - BackTranslation2.0
  - Sign Language Production
  - Evaluation
  - BSL
  - ECCV 2026
---

<table style="border-collapse: collapse; border: none;" border="0">
<tr>
<td style="border: none; text-align: left; font-size: 16px;">

<strong>BackTranslation2.0: A Linguistically Motivated Metric to Assess Sign Language Production</strong> was accepted at <strong>ECCV 2026</strong>.

<br><br>

<strong>Venue:</strong> ECCV 2026<br>
<strong>Authors:</strong> Cory, O., Ivashechkin, M., Ranum, O., Low, J., Fish, E., Pelykh, A., Sahin, K., Mercanoglu Sincan, O., Bowden, R.

</td>
</tr>
</table>

[🌐 Project Page](https://cogvis-cvssp.github.io/BackTranslation2/){:target="_blank"} &nbsp;·&nbsp; [📄 Paper (PDF)](https://cogvis-cvssp.github.io/BackTranslation2/assets/BackTranslation2_0___ECCV_2026_Submission.pdf){:target="_blank"}

**Abstract:** Sign Languages (SLs) are the primary means of communication for millions of Deaf individuals, yet existing evaluation metrics for generated SL remain simplistic and poorly aligned with human judgements. We introduce BackTranslation2.0, a linguistically grounded evaluation metric for text-to-sign translation that moves beyond naïve backtranslation. Our approach adopts an agentic framework in which a deterministic pipeline orchestrates a suite of specialised tools to assess four scoring dimensions (grammatical correctness, phonological accuracy, motion fluency, and generation fidelity) aligned with human rater assessments.

Tool outputs are not treated independently: a set of LLM-based cross-referential comparison modules evaluates consistency across tools and checks outputs against linguistic expectations, enabling structured reasoning over grammatical, phonological, and motion-level evidence. Final dimension scores are computed through deterministic weighted formulas over validated tool outputs. To validate BackTranslation2.0, we introduce and evaluate on a British Sign Language (BSL) dataset annotated by native Deaf raters across the same quality dimensions, benchmarking against six baseline metrics. Our method demonstrates strong correlation with human judgements across all dimensions, providing a more comprehensive, interpretable, and linguistically principled evaluation framework for sign language production systems.
