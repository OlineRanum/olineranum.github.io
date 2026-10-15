"""Generate the inner mockup pages (research, bio, news, cv) into <repo>/_mockups/."""
import datetime
import html
import re
import sys

import yaml

REPO = sys.argv[1]
OUT = REPO + "/_mockups/"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Oline Ranum</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html">Oline Ranum</a>
    <nav class="main">
{nav}
    </nav>
  </div>
</header>

<main class="wrap">
"""

FOOT = """
</main>

<footer class="site">
  <div class="wrap">
    <span>© 2026 Oline Ranum · CVSSP, University of Surrey</span>
    <nav>
      <a href="https://scholar.google.com/citations?user=vv0kBWwAAAAJ&hl=en">Scholar</a>
      <a href="https://github.com/OlineRanum">GitHub</a>
      <a href="https://orcid.org/0000-0001-8627-6259">ORCID</a>
      <a href="#">RSS</a>
    </nav>
  </div>
</footer>

</body>
</html>
"""

NAV = [("index.html", "Home"), ("research.html", "Research"), ("bio.html", "Bio"),
       ("news.html", "News"), ("cv.html", "CV")]


def page(filename, title, body):
    nav = "\n".join(
        f'      <a href="{href}"{" class=\"active\"" if href == filename else ""}>{label}</a>'
        for href, label in NAV)
    with open(OUT + filename, "w") as f:
        f.write(HEAD.format(title=title, nav=nav) + body + FOOT)


def inline_md(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def md_to_html(md):
    """Tiny Markdown subset: ## headings, paragraphs, '-' lists, bold/italic/links."""
    out, toc, in_list = [], [], False
    for block in re.split(r"\n\s*\n", md.strip()):
        lines = [l for l in block.strip().splitlines() if l.strip() and l.strip() != "---"]
        if not lines:
            continue
        if lines[0].startswith("## "):
            heading = lines[0][3:].strip()
            toc.append((slug(heading), heading))
            out.append(f'<h2 id="{slug(heading)}">{inline_md(heading)}</h2>')
            lines = lines[1:]
            if not lines:
                continue
        if all(l.startswith("- ") for l in lines):
            out.append("<ul>\n" + "\n".join(f"  <li>{inline_md(l[2:])}</li>" for l in lines) + "\n</ul>")
        else:
            out.append(f"<p>{inline_md(' '.join(lines))}</p>")
    return "\n".join(out), toc


def front_matter_body(path):
    text = open(path).read()
    body = text.split("---", 2)[2]
    return body.replace("{% include base_path %}", "")


# ---------------------------------------------------------------- Research
body_md = front_matter_body(REPO + "/_pages/SignLanguageProcessing.md")
# The page's own meta description becomes the lede
lede = "An overview of Sign Language Processing: the recognition, translation, and generation of sign languages using computer vision and NLP."
prose_html, toc = md_to_html(body_md)
toc_html = "\n".join(f'        <li><a href="#{s}">{html.escape(t)}</a></li>' for s, t in toc)
page("research.html", "Sign Language Processing", f"""
  <div class="page-head">
    <h1>Sign Language Processing</h1>
    <p class="lede">{inline_md(lede)}</p>
  </div>

  <div class="with-aside">
    <article class="prose">
{prose_html}
    </article>
    <aside class="side toc-wrap">
      <p class="side-label">On this page</p>
      <ul class="toc">
{toc_html}
      </ul>
    </aside>
  </div>
""")

# ---------------------------------------------------------------- Bio
bio_md = front_matter_body(REPO + "/_pages/bio.md")
# Obvious typos in the current text
bio_md = bio_md.replace("My research center on", "My research centres on")
bio_md = bio_md.replace("research assistand", "research assistant")
bio_html, _ = md_to_html(bio_md)
page("bio.html", "Bio", f"""
  <div class="page-head">
    <h1>Bio</h1>
    <p class="lede">Researcher in sign language processing at the Centre for Vision, Speech and Signal Processing, University of Surrey.</p>
  </div>

  <div class="with-aside">
    <article class="prose">
{bio_html}
    </article>
    <aside class="side">
      <div class="facts">
        <dl>
          <dt>Currently</dt>
          <dd>PhD candidate &amp; Research Assistant, CVSSP, University of Surrey</dd>
          <dt>Education</dt>
          <dd><span>MSc Artificial Intelligence, University of Amsterdam — Cum Laude, ELLIS Honours</span><span>BSc, University of Oslo</span></dd>
          <dt>Awards</dt>
          <dd><span>FNWI Master's Thesis Prize 2025</span><span>Amsterdam AI Thesis Award 2024</span></dd>
          <dt>Sign languages</dt>
          <dd><span>Norwegian Sign Language (NTS)</span><span>British Sign Language (learning)</span><span>Sign Language of the Netherlands (some)</span></dd>
          <dt>Previously</dt>
          <dd><span>SignLab Amsterdam &amp; AMLab</span><span>CERN, AEgIS</span><span>Lawrence Berkeley National Lab</span><span>Co-founder, DeepSign AS</span></dd>
        </dl>
      </div>
    </aside>
  </div>
""")

# ---------------------------------------------------------------- News
news = yaml.safe_load(open(REPO + "/_data/small_news.yml"))
news.sort(key=lambda n: n["date"], reverse=True)
years = {}
for item in news:
    years.setdefault(item["date"][:4], []).append(item)
groups = []
for year, items in years.items():
    lis = []
    for item in items:
        d = datetime.date.fromisoformat(item["date"])
        title = html.escape(item["title"])
        text = f'<a href="{item["url"]}">{title}</a>' if item.get("url") else title
        lis.append(f'        <li><time datetime="{item["date"]}">{d:%b}</time><div>{text}</div></li>')
    groups.append(f"""    <div class="year">
      <h2>{year}</h2>
      <ul class="timeline">
{chr(10).join(lis)}
      </ul>
    </div>""")
page("news.html", "News", f"""
  <div class="page-head">
    <h1>News</h1>
    <p class="lede">Papers, projects, and milestones.</p>
  </div>

  <section style="padding-top: 0">
{chr(10).join(groups)}
  </section>
""")

# ---------------------------------------------------------------- CV
def project(thumb, title, url, desc, chip=None, chip_pending=False, links=()):
    chip_html = f'<span class="venue{" pending" if chip_pending else ""}">{chip}</span>' if chip else ""
    title_html = f'<a href="{url}">{title}</a>' if url else title
    links_html = "".join(links)
    return f"""      <li class="project">
        {thumb}
        <div>
          <div class="meta">{chip_html}</div>
          <h3>{title_html}</h3>
          <p>{desc}</p>
          <div class="actions">{links_html}</div>
        </div>
      </li>"""


def img(src, alt, contain=False):
    return f'<div class="thumb{" contain" if contain else ""}"><img src="img/{src}" alt="{alt}" loading="lazy"></div>'


def a(href, label):
    return f'<a href="{href}">{label}</a>'


projects = [
    project(img("beyondbleu.png", "BLEU-4 retention under corruption of the signing", True),
            "Beyond BLEU: A Case for Redefining Sign Language Translation Benchmarks",
            "https://olineranum.github.io/beyondBLEU/",
            "Evaluation study across six SLT systems on Phoenix-2014T and CSL-Daily, showing that gains in BLEU-4 are not on their own evidence of better sign understanding, with an open-weight-LLM QA protocol that scores salient content preservation instead.",
            "WACV 2027", links=(a("https://arxiv.org/pdf/2609.03734", "arXiv"), a("https://olineranum.github.io/beyondBLEU/", "Project page"))),
    project(img("whatsthepoint.png", "Index resolution framework for BSL spatial grammar", True),
            "What's the Point? Spatial Grammar &amp; Index Resolution for Sign Language Processing",
            "https://olineranum.github.io/WhatsThePoint/",
            "Modular framework for spatial indexing in BSL: a pose-based index detector combined with an online entity memory that substantially improves pointing-sign recovery in CSLR without retraining the backbone.",
            "Under review", True, links=(a("https://olineranum.github.io/WhatsThePoint/", "Project page"),)),
    project(img("signgpt.png", "SignGPT project logo", True),
            "SignGPT", "https://olineranum.github.io/SignGPT/",
            "A UKRI EPSRC Programme Grant (University of Surrey, Oxford, UCL) building generative transformers for bidirectional BSL–English translation, combining computer vision, sign linguistics, and machine learning to model the full structure of signed communication.",
            "EPSRC Programme Grant", links=(a("https://olineranum.github.io/SignGPT/", "Project page"), a("https://sites.google.com/view/signgpt", "SignGPT website"))),
    project('<div class="thumb text">Seeing Space</div>',
            "Seeing Space — Directional Verbs and Topographic Placement", None,
            "Computational toolkit for spatial and productive constructions in sign languages: directional verb detection with grammatical-person labelling and a learned pose-based placement module for pronominal indexing.",
            "In development", True, links=('<span class="soon">Project page coming soon</span>',)),
    project(img("ngt200.jpg", "NGT200 multi-view recording setup"),
            "NGT200: Geometric Multi-View Isolated Sign Recognition", "https://olineranum.github.io/GMVISR/",
            "Multi-view benchmark for pose-based isolated sign recognition of Sign Language of the Netherlands (NGT). SE(2)-equivariant Temporal-PONITA improves recognition by 8–22% over the SL-GCN baseline.",
            "ICML 2024 Workshop", links=(a("https://openreview.net/forum?id=idkNzTC67X", "Paper"), a("https://olineranum.github.io/GMVISR/", "Project page"), a("https://osf.io/5zuyd/", "Dataset"))),
    project(img("3dlex.jpg", "A recording session in the 3D-LEX laboratory"),
            "3D-LEX v1.0: 3D Lexicons for ASL and NGT", "https://olineranum.github.io/SAPA/",
            "High-resolution motion capture dataset of 2,000 signs across ASL and Sign Language of the Netherlands, with semi-automatic phonetic annotation that matches or exceeds expert accuracy.",
            "LREC-COLING 2024", links=(a("https://aclanthology.org/2024.signlang-1.33/", "Paper"), a("https://olineranum.github.io/SAPA/", "Project page"), a("https://osf.io/g7u9c/?view_only=8090319e12aa4fd991d81e369a1cbd88", "Dataset"))),
    project('<div class="thumb text">SE(3)</div>',
            "SE(3)-Equivariant Neural Rendering", "https://github.com/elidub/equiv-neural-rendering",
            "Equivariant neural rendering builds on geometric deep learning, computer vision and representation theory; a critical component is the scene representation.",
            links=(a("https://github.com/elidub/equiv-neural-rendering", "GitHub"), a("https://github.com/elidub/equiv-neural-rendering/blob/main/blogpost.md", "Blog post"))),
    project(img("pointe.jpg", "Poster presentation at the University of Amsterdam"),
            "Indoor Scene Generation using Point-E and Training-Free Layout Control", "https://github.com/LBBusser/point_e_team10/",
            "A framework extending point cloud diffusion models to generate indoor scenes directly from text prompts.",
            links=(a("https://github.com/LBBusser/point_e_team10/", "GitHub"),)),
]

page("cv.html", "CV", f"""
  <div class="page-head">
    <h1>CV</h1>
    <p class="lede">PhD researcher in sign language processing at CVSSP, University of Surrey. The full CV is available as a PDF.</p>
    <a class="button" href="https://olineranum.github.io/files/CV_Ranum_Public.pdf"><i class="fa-regular fa-file-lines"></i>Download CV (PDF)</a>
  </div>

  <section id="projects">
    <div class="section-head"><h2>Selected projects</h2></div>
    <ul class="projects">
{chr(10).join(projects)}
    </ul>
  </section>

  <section id="media">
    <div class="section-head"><h2>Media</h2></div>
    <div class="media">
      <figure>
        <a href="https://www.uio.no/om/aktuelt/arrangementer/en-ny-start-festival/student-og-grunder-hvordan-kan-din-ide-bli-til-noe-mer.html"><img src="img/deepsign-uio.jpg" alt="DeepSign AS at En ny start festival, University of Oslo" loading="lazy"></a>
        <figcaption>DeepSign at En ny start, University of Oslo.</figcaption>
      </figure>
      <div class="press">
        <div>
          <h3>SignGPT</h3>
          <a href="https://www.bbc.co.uk/news/articles/c4g9rd4g8w2o">BBC News</a>
        </div>
        <div>
          <h3>Podcast</h3>
          <a href="https://membership.echobox.radio/shows/talk-that-science?episode=35">Talk That Science #35 — AI for Sign Language</a>
          <small>Echobox Radio · June 2025</small>
        </div>
        <div>
          <h3>3D-LEX</h3>
          <a href="https://www.napnieuws.nl/2024/02/20/ai-voor-gebarentaal-uva-werkt-aan-een-nieuw-vertaalprogramma/">Napnieuws.nl (NL)</a>
          <small>SignLab interview, 3D-LEX laboratory</small>
        </div>
        <div>
          <h3>DeepSign AS</h3>
          <a href="https://www.titan.uio.no/innovasjon/2021/studentgrundere-vil-lage-automatisk-tegnsprak-oversetter.html">Titan.uio.no (NO)</a>
          <a href="https://argumentnett.no/2022/02/06/tetter-kommunikasjonsgapet-ved-hjelp-av-kunstig-intelligens/">Argument.no (NO)</a>
          <a href="https://ace-incubator.nl/cohort-fall-2021/">ACE Incubator, cohort 2021</a>
          <a href="https://prosjektbanken.forskningsradet.no/project/FORISS/327456">Research Council of Norway</a>
        </div>
      </div>
    </div>
  </section>
""")

print("ok")
