# Outside meat: the same shape in other domains

**Summary.** The abstract shape of this project — one continuous object, several culturally
distinct schemes that partition it into named regions, all registered into one shared coordinate
frame, with a region in scheme A expressible as a percentage of a region in scheme B — exists in
neuroimaging under the name **the brain atlas concordance problem**, and Bohland et al. (2009,
PLoS ONE) computes *exactly* the quantity this atlas computes, from exactly the same motivation.
The critical vocabulary distinction, which runs through every analogue below: there are **two**
different things people compute when comparing partitions of one object. (a) *Region-to-region
overlap*, a **matrix**: the **non-symmetric conditional overlap** P(i|j) = |r_i ∩ r_j| / |r_j|
("what fraction of region j lies inside region i"), whose symmetric partners are Dice, Jaccard,
and the **cosine coefficient** O_ij = |r_i ∩ r_j| / sqrt(|r_i||r_j|) = sqrt(P_ij · P_ji).
(b) *Whole-partition-to-whole-partition similarity*, a **scalar**: Adjusted Rand Index, Adjusted
Mutual Information, Variation of Information, or Bohland's purpose-built **S-index**. This atlas
currently computes (a), the directional one. **P(i|j) ≠ P(j|i)**, so every percentage the atlas
publishes must name its direction or it is meaningless. Bohland's own names for it, verbatim, are
a **"non-symmetric measure of spatial overlap"** (p.15) and, in use, the **"conditional overlap
measure"** (p.4) or **"region-to-region conditional probabilities"** (p.3); the GIS discipline
calls the identical quantity an **allocation factor** (Geocorr) or an **areal weight**. The single
best precedent for a headline number the atlas does *not* yet compute is Bohland's **S-index**.

---

## 1. Brain parcellation atlases — the closest structural match that exists

### 1.1 Bohland, Bokil, Allen & Mitra (2009), "The brain atlas concordance problem: quantitative comparison of anatomical parcellations", PLoS ONE 4(9): e7200

- DOI 10.1371/journal.pone.0007200.
  Landing page fetched: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0007200
  Full printable PDF fetched and **read page-by-page directly** (not summarizer-mediated):
  https://journals.plos.org/plosone/article/file?type=printable&id=10.1371/journal.pone.0007200
  PubMed record: https://pubmed.ncbi.nlm.nih.gov/19787067/ (not fetched — cookie wall)
- **The object**: one brain. Specifically the single-subject ICBM "Colin27" template, 181×217×181
  at 1 mm isotropic voxels, spatially registered (9-parameter global affine) to **MNI-305**
  stereotaxic space. Only the **left hemisphere** grey matter was analysed. *(verbatim, p.14.)*
- **The partitions**: 8 parcellation methods applied to that one brain. Table 1, **read directly
  off the PDF** (an earlier WebFetch summary of this same table returned a completely different
  and wrong set of numbers — do not trust summarizer output for counts):

  | Method | # LH regions | % GM labeled | Reference space |
  |---|---|---|---|
  | AAL   | 62 | 93.2% | Colin27 |
  | CYTO  | 29 | 21.6% | MNI average |
  | H-O (Harvard-Oxford) | 56 | 86.7% | MNI average |
  | ICBM  | 49 | 92.5% | Colin27 |
  | LPBA40 | 29 | 97.0% | MNI average |
  | T&G (Tourville & Guenther / FreeSurfer) | 65 | 81.1% | Colin27 |
  | TALc (Talairach cytoarchitectonic / Brodmann) | 68 | 26.5% | Talairach brain |
  | TALg (Talairach gyral) | 49 | 76.7% | Talairach brain |

- **THE METRIC.** Verbatim, Materials and Methods, p.15:

  > "We define a non-symmetric measure of spatial overlap between a region *i* from parcellation
  > *R* and region *j* from parcellation *R'* as:"
  >
  > P_ij = |r_i ∩ r_j| / |r_j| = P(x ∈ r_i | x ∈ r_j)   **(Equation 3)**
  >
  > "P_ij thus indicates the proportion of region *r_j* that is contained within the bounds of
  > region *r_i*. Its values are limited to the interval [0,1], and thus P_ij has a
  > straightforward interpretation as the conditional probability that a voxel is contained in
  > region *i* given that it is contained in region *j*, averaged across all voxels in *r_j*.
  > For simplicity, we write these conditionals as P(i|j) or simply P_ij, omitting the reference
  > to voxel *x*."

  And the crucial justification for preferring it over Dice/Jaccard, verbatim:

  > "This conditional measure is to be contrasted with more commonly employed symmetric overlap
  > measures, such as the Dice coefficient [51] or the Jaccard similarity index [52], which can
  > only take its maximum value of 1 when the regions are *identically* defined. P_ij is instead
  > 1 when there is a pure subset relationship, even when P_ji < 1."

  Symmetric companion, **Equation 4**:

  > O_ij = |r_i ∩ r_j| / sqrt(|r_i| |r_j|) = sqrt(P_ij · P_ji)
  >
  > "This index, which is equivalent to the *cosine coefficient* for binary vectors as commonly
  > used in information retrieval [53], again takes values on [0,1], but is only equal to 1 when
  > the two regions are identically defined. Here O_ij = O_ji."

  Figure 2 spells out the geometry in a Venn diagram and states the measure is on
  "the areas (volumes in 3-D) of the shaded regions", with worked values
  P(r1|r2) ≈ 0.5, P(r1|r3) = 1.0, etc.

- **The framing sentence** this project should steal, verbatim from the Results, p.3:

  > "Pair-wise relationships can be expressed using simple conditional probabilities, providing
  > answers to straight-forward questions of the form: *what is the probability that a voxel is
  > in Region X according to Method A if it is in Region Y according to Method B?*"

  And from the Abstract / Introduction:

  > "discounting the names of regions and instead comparing their definitions as spatial entities
  > in an effort to provide more precise quantitative mappings between anatomical entities as
  > defined by different atlases"

  And from the Discussion, p.11 — this is the thesis of the beef atlas in one sentence:

  > "The *brain atlas concordance problem* occurs not because of disagreements in terminology
  > (cf. descriptions of the neuroanatomical *nomenclature problem*), but because the underlying
  > reference partitions of brain anatomy (e.g. atlases) are, at times, dissimilar."

- **Global (whole-partition) concordance**: two scalars.
  - **Adjusted Rand Index (ARI)**. Critiqued verbatim, p.12: "The ARI works by comparing the
    fraction of, in this case, voxel pairs that are either assigned the same label in both
    parcellations or different labels in both parcellations relative to the total number of voxel
    pairs. This index does not allow for *refinement* of a single region in one atlas into
    multiple regions in another without penalty."
  - **S-index** — novel to this paper, **Equation 7, read directly off p.16**. Prose from p.12:
    "The S-index was designed to capture global similarity while allowing for region refinement in
    one atlas relative to another. … The S-index computes a sum of 'penalties' for each pair of
    overlapping regions in the two parcellations, weighted by the relative volume of the smaller
    region. No penalty is assigned when one region is a pure subset of another (when
    max(P(i|j),P(j|i)) = 1; see Figure 2 for illustration), and the largest penalty is assigned
    when the maximal overlap is 50% (reflecting maximal ambiguity in mapping between the region
    pair)." It is "similar to the local consistency error measure defined by Martin et al. [28]
    for comparing object segmentations in complex 2D images."

    **The actual formula**, p.16 — and it is small enough to implement in an afternoon:

    > X_ij = max(P_ij, P_ji)
    >
    > U_ij = min(|r_i|, |r_j|) if X_ij > 0, else 0 ;  W_ij = U_ij / Σ U_ij
    >
    > **S = 1 − 4 Σ_ij W_ij X_ij (1 − X_ij)**   (Equation 7)

    The penalty kernel is `4x(1−x)`, which is 0 at x = 1 (pure subset — no penalty) and 0 at
    x = 0 (disjoint), and peaks at 1 when x = 0.5 (maximal ambiguity). S runs on [0,1].
    Weights W_ij are normalised sizes of the *smaller* region of each overlapping pair.
    **This is the single most directly reusable piece of methodology found in this thread**: it
    takes the atlas's existing pairwise overlap numbers and turns them into one defensible number
    per tradition-pair, with a published rationale for why it beats the Adjusted Rand Index on
    exactly the failure mode this data has (French cuts are *refinements* of American ones, and
    ARI penalises refinement).
  - **Chance baseline**: random space-filling partitions of the grey-matter voxels with N matched
    to each atlas; 1000 size-matched random pairs per atlas pair give an empirical null. Only
    3 atlas pairs beat chance on ARI (H-O/ICBM, H-O/LPBA40, ICBM/LPBA40). Figure 8 is the
    8×8 concordance matrix with above-chance entries in green.

- **Two derived quantities this atlas could copy directly**:
  - *Fan-out*: "On average, a single region overlaps more than 4 regions defined in any other
    parcellation, and sometimes 15 or more" (p.12); for ICBM specifically the mean and median
    number of partially overlapping regions in the other 7 parcellations are **4.95 and 4.71**
    (p.4). The beef-atlas equivalent — "the average US cut straddles N Japanese cuts" — is a
    one-number headline finding, and it has precedent.
  - *Bipartite equivalence classes*. Verbatim, p.16: "For any pair of parcellations, we define a
    weighted *bipartite graph* B = (V1+V2, E) where edges E are weighted as:
    **E_ij = max(P(i|j), P(j|i))**, i ∈ V1, j ∈ V2" (Equation 5). Then: "we employed a very simple
    algorithm, which iteratively removes the edge with smallest non-zero weight until a threshold
    for the maximum number of graph components or maximum pruned edge weight is reached. We then
    deduced that, for each resulting connected component, the union of regions represented in V1
    has a spatial correspondence with the union of regions represented in V2". Figure 6 does this
    for Harvard-Oxford vs LPBA40 at a pruning threshold of **0.25**, yielding **9 connected
    components**; caption verbatim: "for each component, the union of regions on the left is
    approximately equivalent to the union of regions on the right."
    This is the principled way to say "this *group* of American cuts equals this *group* of
    Japanese cuts", which is what butchers actually want and what no name-matching table can give.
    Strongly recommended, both as a data product and as a UI.

- **Is the data published?** It *was*. Verbatim, p.4: "The full overlap matrix for any atlas pair
  can also be downloaded from http://obart.info." **That site is dead** — DNS does not resolve
  (`getaddrinfo ENOTFOUND obart.info`, fetch attempted 2026-09-13). web.archive.org is blocked to
  this agent, so whether a snapshot survives is **UNPROVEN**. Lesson for this project: the
  overlap matrix outlived its host by 17 years only as figures in the paper. Publish the matrix
  as a file in the repo, not as a website.

- **Ontology remark, directly on point for §3 below.** Verbatim, p.4:
  > "Such 'overlap' relations [31], which vary asymmetrically, are problematic for terminological
  > ontologies that rely on simple categorical mappings and therefore lose information relative
  > to the pair of conditional probability values we compute here."

  And from the Summary, p.14:
  > "simple ontological efforts based on, for example, synonymy and parent-child relationships,
  > appear to be incapable of capturing the rich landscape of spatial relations observed in this
  > analysis of human brain atlases."

### 1.2 neuroparc (Myers, Arvapalli, et al.) — the living successor to obart.info

- Preprint fetched: https://www.biorxiv.org/content/10.1101/845065v1.full
  ("Standardizing Human Brain Parcellations")
- Repo fetched: https://github.com/neurodata/neuroparc
- **24 adult human brain parcellations** in **MNI152NLin6** space per the preprint; the repo
  landing page advertises a larger collection (34+ atlases including FreeSurfer-surface and
  legacy Talairach entries, region counts from 7 (Yeo-7) up to ~1105 (Talairach)). Organised to
  the **BIDS** specification. Region counts from the repo page are UNVERIFIED against a second
  source — treat the preprint's "24 in MNI152NLin6" as the solid number.
- Metrics used: **Dice coefficient** (per-region spatial overlap, Figure 2 "Dice Score Map")
  and **Adjusted Mutual Information** (whole-parcellation, Figure 3 "adjusted mutual information
  matrix between all atlas pairs"). Verbatim from the preprint: "Adjusted mutual information is
  another measure of the similarity of two labelled sets, quantifying how well a particular point
  can be identified as belonging to a region given another region."
- **License: Apache 2.0** — "All code is provided under the Apache 2.0 License."
- Whether the precomputed Dice/AMI matrices ship as *files* in the repo (rather than only as
  figures) is **UNPROVEN**; the repo landing page fetch did not name such paths.

### 1.3 Arslan et al. (2018), NeuroImage — the metric menu for whole-parcellation comparison

- https://pubmed.ncbi.nlm.nih.gov/28412442/ and
  https://www.sciencedirect.com/science/article/abs/pii/S1053811917303026
- **UNPROVEN / not fetched**: both are behind a cookie wall or paywall. From search-result
  metadata only (so, do not cite this as read): evaluates 10 subject-level and 24 groupwise
  parcellation methods on HCP data using **Dice coefficient**, **adjusted Rand index**,
  **Silhouette coefficient** and parcel homogeneity. Listed here only because it confirms the
  metric vocabulary is standard; the load-bearing citation is Bohland, which *was* read in full.

### 1.4 Tools that answer "this voxel is X in atlas A and Y in atlas B"

- **Coord2Region** (Abdelhedi et al., arXiv:2512.18165). Fetched:
  https://arxiv.org/html/2512.18165v1 — Python package mapping MNI/Talairach coordinates to
  labels in **more than 20 atlases** (AAL, Harvard-Oxford, Destrieux, …) simultaneously via a
  `MultiAtlasMapper` class "returning per-atlas labels for comparison"; bidirectional
  (coordinate ↔ voxel index ↔ region label). It does *not* compute atlas-to-atlas overlap — it is
  a point lookup. Repo fetched: https://github.com/BabaSanfour/Coord2Region — the **code licence
  is BSD-3-Clause**. (A first pass recorded "CC BY 4.0"; that is the arXiv *paper* licence, not
  the software licence. Corrected after fetching the repo.)
  This is precisely the beef atlas's "click a point on the cow, see what every tradition calls it".
- **AtlasReader** (Notter et al. 2019, JOSS 4(34):1257).
  https://joss.theoj.org/papers/10.21105/joss.01257 — repo fetched:
  https://github.com/miykael/atlasreader. Analyses statistical MRI images to identify and label
  brain regions, producing coordinate tables, region labels and figures. The README does **not**
  itemise the default atlas set (there is an `atlas` parameter defaulting to `'default'`), so the
  commonly repeated "ships AAL, Desikan-Killiany and Harvard-Oxford" list is **UNPROVEN** here.
  **Licence, verbatim from the README** — and this is the sentence this project should heed:
  > "AtlasReader is licensed under the BSD-3 license; however, the atlases it uses are separately
  > licensed under more restrictive frameworks. By using AtlasReader, you agree to abide by the
  > license terms of the individual atlases."

  The *code* being open does not make the *partition* open. Whatever licence this atlas ships
  under, the licensing of each tradition's cut list is a separate question from the licensing of
  the viewer.
- **Scalable Brain Atlas** (Bakker, Tiesinga & Kötter 2015, Neuroinformatics 13:353-366).
  Fetched: https://scalablebrainatlas.incf.org/ ; preprint https://arxiv.org/abs/1312.6310 ;
  PubMed https://pubmed.ncbi.nlm.nih.gov/25682754/ (not fetched).
  Web-based slice viewer over **>20 atlas templates in ~6 species** (human, macaque, mouse, rat,
  ferret, marmoset, opossum), with a plugin API and web services (`listregions.php`, coordinate
  transforms, SVG→bitmap, label-volume export, region centres and distance matrices).
  **Site is live but the page's own last-update stamp is 8 Feb 2019.**
  Crucially, its "SBA Lookup" plugin finds "which other atlases have a region with the **same
  name** as the active region" — i.e. it solves the *nomenclature* problem by string matching,
  **not** the concordance problem by spatial overlap. That is exactly the weaker thing Bohland
  argues against, and it is the difference between this project and a synonym table.
- **SumsDB** (Surface Management System Database, http://sumsdb.wustl.edu/sums) is cited by
  Bohland as the prior art for the ability to "overlay" different partitions on one another;
  not fetched, status in 2026 **UNPROVEN**.
- Also named in Bohland but not independently checked here: the **Talairach Daemon** (Lancaster
  et al.) — "an online tool that allows researchers to query for labels at five different
  'levels' at any given point in Talairach space" — and the **Anatomy Toolbox** (Zilles and
  colleagues), the source of the CYTO probabilistic cytoarchitectonic maps.

### 1.5 "Common coordinate framework" — yes, the term is established, and it is exactly `FRAME.md`

- **Rood et al. (2019), "Toward a Common Coordinate Framework for the Human Body", Cell
  179:1455-1467.** https://www.cell.com/cell/fulltext/S0092-8674(19)31275-9 (**403 to this
  agent — not fetched**); https://pubmed.ncbi.nlm.nih.gov/31835027/ (cookie wall, not fetched).
  Definition circulating in search metadata — **treat as UNPROVEN until read**: a CCF is
  "an underlying reference map of organs, tissues, or cells that allows new individual samples to
  be mapped to determine the relative location of structural regions between samples".
- **Allen Mouse Brain Common Coordinate Framework (CCFv3)**, Wang et al. (2020), Cell
  181(4):936-953. Publisher page 403; PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC8152789/
  cookie-walled. Fetched instead, from the Allen Institute's own docs:
  https://alleninstitute.github.io/CCF-MAP/descriptions/mouse_ccf.html and
  https://alleninstitute.github.io/abc_atlas_access/descriptions/Allen-CCF-2020.html
  — "a 3D reference space … an average brain at 10 um voxel resolution", built from serial
  two-photon tomography of **1,675** young adult C57Bl6/J mice, annotated **directly in 3D**,
  every voxel labelled, spanning **43 isocortical areas and their layers, ~314–329 subcortical
  grey-matter structures, 81 fiber tracts, 8 ventricular structures**. (The subcortical count
  differs between the two Allen pages — 314 on CCF-MAP, 329 on the ABC atlas page; flagged, not
  resolved.) Downloads are direct S3 links (`template_10.nii.gz`,
  `annotations_compressed_10.nii.gz`). **License not stated on the page fetched — UNPROVEN.**
  CCF-MAP itself spans mouse, human (two versions), rhesus macaque, cynomolgus macaque and
  marmoset, i.e. it is a *multi-species* CCF primer.
- **HuBMAP Common Coordinate Framework.** Fetched: https://hubmapconsortium.org/ccf/ (via
  https://hubmapconsortium.github.io/ccf/). Components: **ASCT+B tables** (Anatomical
  Structures, Cell Types and Biomarkers), a **CCF Ontology**, a **3D Reference Object Library**
  (with NIAID/NIH), a 2D Reference Functional Tissue Unit library, and the **CCF Registration
  User Interface (RUI)**, which "supports uniform tissue data registration across organs and
  labs". Mesh formats and licence not stated on the page fetched — **UNPROVEN**.
- **Börner et al., "Construction and Usage of a Human Body Common Coordinate Framework Comprising
  Clinical, Semantic, and Spatial Ontologies"**, arXiv:2007.14474 — fetched
  https://arxiv.org/abs/2007.14474. The CCF "provides the essential infrastructure for
  integrating and spatially harmonizing these diverse datasets within a unified three-dimensional
  reference system" and "provides a semantically annotated, 3D reference system for the entire
  body". Three layers: **clinical** ontology (donor/specimen metadata), **semantic** ontology
  (ASCT+B: anatomical structures, cell types, biomarkers), **spatial** ontology (3D coordinates
  of tissue samples). No weighted/percentage vocabulary mapping is described.

**Takeaway for `FRAME.md`:** rename what it describes a **common coordinate framework (CCF)** —
the term is established across at least three independent large consortia (Allen, HuBMAP, HCA)
and means precisely what the file already does: a shared 3D reference into which independently
produced delineations are registered so they can be compared. The Rood et al. definition is the
one to quote once it can actually be read.

---

## 4. Cross-linguistic partition of a continuum — the human-science version

### 4.1 Body-part terminology: *Language Sciences* 28(2-3), 2006 — the colour survey done on a body

This is the startlingly close one: **one body, many languages' partitions of it, elicited on
identical stimuli.**

- **Enfield, N.J. (2006), "Elicitation guide on parts of the body", Language Sciences 28(2-3):
  148-157, doi:10.1016/j.langsci.2005.11.003.** Open PDF fetched and **read page-by-page**:
  https://pure.mpg.de/rest/items/item_60128/component/file_60129/content
  - **The shared frame is literally a figure.** Verbatim, p.153: "this elicitation guide includes
    **six illustrations of the body**, showing front and back views of men and women (including
    two additional 'modest' front views, in case nudity offends in your field site)."
    Figures 1-6 are the male front/back, female front/back, and two modest front views.
  - **The registration procedure.** Verbatim, p.153: "(a) Give a pen to the consultant and ask him
    or her to name the various body parts, **drawing outlines (i.e., not just marking points)** of
    the specified body parts on the illustrations." And (b), p.154: "Tell him or her that 'The
    person has a mole/wart/birthmark/mosquito bite on his ___' … and ask the consultant to draw it
    on the figure."
    Immediately followed by the honest caveat: "These procedures will work for only a selection of
    the full set of body part terms."
  - **The problem statement**, p.152, verbatim, is the beef-atlas problem verbatim: "the
    extensional range of English *shoulder* includes the joint connecting the arm to the torso …
    Lao, on the other hand, has no equivalent word for 'shoulder'. The extension of English
    *shoulder* is covered by **two** Lao expressions: *baa1* … and *ngaw5 khèèn3* … Their
    respective extensional range is delineated at the joint itself."
  - Sections of the guide: 1 Inventory of parts; 2 **Extensional range** of body part terms;
    3 **Intensional content**; 4 **Ambiguity vs. generality** (with the assertion-negation test
    and the "I-saw-two-X's" test); 5 Establishing **'partonomy'**.
  - **No quantitative metric is proposed in the guide.** The comparison across languages in this
    special issue is qualitative/typological. Stated plainly so the project does not overclaim
    this as a statistical precedent.
  - The guide defers the formal version to "van Staden and Majid, this issue".
- **van Staden, M. & Majid, A. (2006), "Body colouring task", Language Sciences 28(2-3):
  158-161.** The companion elicitation instrument: consultants **colour in** body parts on a
  standard body drawing when given a term; each body part is divided into smaller segments and
  colouring behaviour is coded per segment and compared. **UNPROVEN as read** — I could not fetch
  an open full text; the description above comes from search-result metadata and from Enfield's
  cross-reference to it. *The per-segment coding is the interesting bit: it is a discretisation of
  the shared frame into comparison units, i.e. the same move as voxels in Bohland and boxes in
  `FRAME.md`.* Worth a proper library fetch before citing.
- **Enfield, Majid & van Staden (2006), "Cross-linguistic categorisation of the body:
  Introduction", Language Sciences 28(2-3): 137-147.**
  https://pure.york.ac.uk/portal/en/publications/cross-linguistic-categorisation-of-the-body-introduction
  (record page only — full text not fetched, **UNPROVEN**). The special issue runs pp. 137-360.
- **Tjuka, Forkel & List (2024), "Universal and cultural factors shape body part vocabularies",
  Scientific Reports 14, s41598-024-61140-0.** https://www.nature.com/articles/s41598-024-61140-0
  (redirects to an IdP — **not fetched**); PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC11076558/
  (cookie-walled); https://pubmed.ncbi.nlm.nih.gov/38714717/ (cookie-walled).
  **UNPROVEN as read.** From search metadata: the first large-scale comparison of body part
  vocabularies across **1,028 language varieties**, using **colexification** networks (two body
  parts named by one word) rather than spatial overlap; finds adjacent body parts are colexified
  frequently, and that body-part networks vary *less* across language families than emotion or
  colour networks. Note the methodological contrast worth recording: this compares partitions via
  *shared lexical labels*, not via a shared spatial frame — the weaker, name-based approach,
  scaled up. Data is almost certainly CLDF/Zenodo-archived and openly licensed, but that is
  **UNVERIFIED**.

### 4.2 World Color Survey — one Munsell array, 110 languages

- Kay, P. & Regier, T. (2003), "Resolving the question of color naming universals", PNAS
  100(15): 9085-9089, doi:10.1073/pnas.1532837100. Open PDF fetched and **read directly**:
  https://terry-regier.github.io/lclab/papers/kay-regier-PNAS-2003.pdf
- **The object**: **330 Munsell colour chips** — "40 gradations of hue at eight levels of value
  (lightness) and maximal available chroma (saturation), plus 10 neutral (black-gray-white)
  chips at 10 levels of value." Presented one at a time in a fixed random order. This is the
  shared coordinate frame, and it is a *discrete stimulus array*, exactly like the beef atlas's
  box grid.
- **The partitions**: the WCS "collected color naming data *in situ* from **110** unwritten
  languages spoken in small-scale, nonindustrialized societies, from an average of **24** native
  speakers per language (mode: 25 speakers), insofar as possible monolinguals." Table 1 of the
  paper lists all 110 with speaker counts.
- **THE METRIC — and note that it is *not* an overlap metric.** Verbatim:
  > "Because the idea of clustering depends essentially on the concept of distance, we required a
  > color space in which psychologically meaningful distances can be calculated. Consequently we
  > transformed our 330 color stimuli from Munsell space, which lacks such a distance metric, to
  > **CIEL\*a\*b\*** space, which has one."

  Each colour term T in each language L is represented by its **centroid** in CIEL\*a\*b\* — the
  centroid of the chips named T by a speaker, averaged over speakers, then "coerced back to the
  chip most similar to it in the stimulus array". The comparison statistic is a **dispersion**
  measure, Equation 1:
  > D = Σ_{l,l' ∈ WCS} Σ_{c ∈ l} min_{c* ∈ l'} distance(c, c*)
  >
  > "Because *D* is a measure of dispersion, low values of *D* indicate clustering."
- **The null model** is a **Monte Carlo hue-rotation**: each language's term centroids are rotated
  by a random amount in the a\*b\* (hue) plane — the same amount for all terms within a language,
  different amounts across languages — thereby "preserv[ing] within-language structure while
  randomizing cross-language structure". 1,000 randomized datasets. Result: "the WCS data show
  significantly less dispersion, that is, more clustering, than expected by chance, P < 0.001."
- **Structural note for this project**: the WCS solves a *different* comparison problem from
  Bohland's. It compares partitions by **the distance between their category centroids**, not by
  the overlap of their extents. That is the right tool when you want to ask "do different schemes
  put their category *centres* in the same places?" — a question the beef atlas could also ask
  (do US, Japanese and Brazilian butchery put cut-centroids in the same places on the carcass?)
  and which would be a genuinely new statistic for it, complementary to the overlap matrix.
- **Data — live and open, and the archive has moved.** The old ICSI addresses
  (http://www.icsi.berkeley.edu/wcs, http://www1.icsi.berkeley.edu/wcs/data.html) **refuse
  connections** (ECONNREFUSED 192.150.186.60:443, 2026-09-13). The working home is
  **https://linguistics.berkeley.edu/wcs/data.html** (fetched; maintained by Richard Cook,
  Paul Kay and Terry Regier; most recent file update 16 March 2011; NSF-funded). Files:
  | file | contents |
  |---|---|
  | `chip.txt` | the 330 Munsell stimuli with their WCS grid coordinates (rows A–J = value, cols 1–40 = hue) |
  | `term.txt` | for each consultant and each chip, the term they named it with — **the raw partition data** |
  | `foci.txt`, `foci-exp.txt` | each consultant's best example(s) of each term |
  | `lang.txt` | language, country, fieldworker |
  | `spkr.txt` | consultant demographics |
  | `dict.txt` | term abbreviations and renderings (UTF-8) |
  | `cnum-vhcm-lab-new.txt` | **the frame registration table** — WCS chip number ↔ Munsell ↔ CIEL\*a\*b\* coordinates |
  | `BK-term.txt`, `BK-foci.txt`, `BK-dict.txt` | the Berlin & Kay (1969) 20-language data |
  | `WCS-Munsell-chart.txt` / `.png` | the visual reference chart |
  **Licence**: there is no formal open licence — the archive states only "In any published work
  based on these data, please cite these archives." Note that as a licensing precedent this is
  *weaker* than CC-BY, and it has not stopped the dataset becoming the standard benchmark for
  30 years of partition-comparison work.
- **An interactive analogue worth looking at**: https://wcs.ijs.si/ (fetched) — WCS visualisations
  by Mikael Vejdemo-Johansson (KTH) and Susanne Vejdemo (Stockholm), built in d3.js, over 2,618
  speakers / 110 languages / 1,441 unique colour terms. Two views: a **Mapper** (topological data
  analysis) layout of all colour terms, with inter-term distance computed by **Earth Mover's
  Distance** "to reflect perceptual color differences", and a plainer explorer listing all
  languages with speaker counts and all lexemes with response counts, with hover-over-the-chart
  response rates. EMD is a third named metric worth knowing: it compares two *distributions* over
  a shared frame rather than two crisp sets, and would be the right tool if cut boundaries are
  ever treated as fuzzy rather than as hard boxes. No licence or download stated on the page.
- Follow-on work worth chasing (all **unfetched, listed as leads only**): Lindsey & Brown, "World
  Color Survey color naming reveals universal motifs and their within-language diversity", PNAS,
  doi:10.1073/pnas.0910981106 (403 to this agent) — k-means over *whole naming systems* to find
  recurrent "motifs", i.e. clustering the partitions themselves rather than the categories;
  Regier, Kay & Khetarpal, "Color naming reflects optimal partitions of color space",
  PNAS — the "well-formedness" optimality criterion for a partition.

### 4.3 Labov's cups — the caveat this project should record but not over-invest in

- Labov, W. (1973), "The boundaries of words and their meanings". **No primary source fetched —
  every claim here is UNPROVEN**, assembled from search metadata and secondary summaries
  (e.g. https://en.wikipedia.org/wiki/Referential_indeterminacy, not fetched).
  Reported design: subjects are shown drawings of receptacles varying continuously in
  width-to-depth ratio and asked to name them (cup / mug / bowl / vase); the cup→bowl naming
  boundary shifts *gradually* with diameter, and shifts again with imagined contents (hot coffee
  pushes "cup", mashed potatoes pushes "bowl").
- **Why it matters here, and why it is a caveat rather than a precedent**: it is the classic
  demonstration that a category boundary over a continuum can be *graded and context-dependent*
  rather than crisp. `FRAME.md` models every cut as a hard union of axis-aligned boxes, which
  asserts a crisp boundary. That is a defensible simplification — butchery boundaries are cut
  with a knife, so they *are* crisper than "cup vs bowl" — but the project should say so
  explicitly rather than leave it implicit, because a reader from linguistics will ask.
  It does **not** give a metric; there is no overlap matrix in this tradition.

### 4.4 Whole-partition comparison metrics — the canonical names

There is a settled ML/statistics literature on "comparing two clusterings", which is the same
mathematical object as "comparing two partitions of one carcass". Read directly from
Xiang, Mao, Chai, Chieu, Tsang & Zhao (2012), "A Split-Merge Framework for Comparing Clusterings",
ICML 2012 — https://arxiv.org/pdf/1206.6475 (PDF pages 1-3 read as images), which gives a clean
survey. **It sorts every such measure into three families:**

1. **Pair counting.** "Pair counting measures are based on counting the pairs of points for which
   two clusterings agree or disagree." — **Rand index** (Rand 1971): the fraction of point-pairs
   on which the two partitions agree; **Adjusted Rand Index** (Hubert & Arabie 1985), the
   chance-corrected version. Noted weakness, verbatim: "They are sensitive to parameters, such as
   the size of a cluster, the number of clusters, and the number of data points."
2. **Set matching.** "Set matching measures find a maximum matching between two clusterings. They
   make no assumption on how clusterings are generated, but they **ignore those unmatched
   clusters**." Named instances: the **Van Dongen criterion** (Dongen 2000) and **classification
   accuracy**, where "finding the best mapping between two clusterings is equivalent to solving a
   maximum weighted bipartite matching problem (Meilă, 2005)".
3. **Information theoretic.** **Normalized Mutual Information**, NMI(L,C) = I(L,C)/max{H(L),H(C)}
   (Vinh et al. 2010); **Adjusted Mutual Information** (Vinh, Epps & Bailey 2010); and
   **Variation of Information**, verbatim:
   > "The variation of information VI(L, C) = H(C|L) + H(L|C) is the change in the amount of
   > information when transforming L into C (Meilă, 2007). Although VI(L, C) has certain desired
   > properties, it is unnormalized. This can be rectified through dividing by the upper bound
   > log n (Meilă, 2007)."

   Primary source: Meilă, M. (2007), "Comparing clusterings — an information based distance",
   *Journal of Multivariate Analysis* 98(5): 873-895; conference version Meilă (2003),
   "Comparing Clusterings by the Variation of Information", COLT/Kernel 2003, Springer LNCS
   2777, https://link.springer.com/chapter/10.1007/978-3-540-45167-9_14 — **the Meilă papers
   themselves were not fetched**; the claim that VI is a *true metric* (positive, symmetric,
   triangle inequality) comes from search metadata and is **UNPROVEN here**, though it is the
   property VI is famous for. Verify against Meilă directly before putting it in print.

**Convergent evidence worth noting**: this ICML paper independently models the relation between
two clusterings as "a **bipartite graph** which is decomposed into **connected components**" —
the *same* construction Bohland (2009) arrived at for two brain atlases (§1.1). Two unconnected
literatures both land on "bipartite graph, prune, take connected components" as the way to express
*group*-to-*group* equivalence between two partitions. That is a strong signal that it is the
right shape for "these three American cuts together equal these four Japanese ones".

---

## 6. Interactive 3D / multi-scheme viewers worth stealing from

Covered in passing above rather than separately: **Scalable Brain Atlas** (§1.4) is the closest
working example of a web viewer over one template with many parcellations and a plugin
architecture; **Coord2Region** (§1.4) is the closest example of the "one point, every scheme's
name for it" interaction; the **HuBMAP CCF Registration UI** (§1.5) is the closest example of
placing a sub-region into a shared 3D body frame through a browser. Bohland's **Figure 6 bipartite
graph with pruned edges** (§1.1) is the best *visualisation* idea found in this thread and is not,
as far as this search found, used by any food or butchery resource.

---

## 2. BodyParts3D / Anatomography — the direct technical ancestor of the anatomy layer

Researched in parallel by a separate agent; claims below carry the URL that agent fetched, and
counts marked "(raw)" were pulled byte-for-byte with curl rather than through a summarizer.

- **Still online.** Archive: https://dbarchive.biosciencedbc.jp/en/bodyparts3d/desc.html
  (operation start 2007/10, last update 2013/05). Dated release directories at
  https://dbarchive.biosciencedbc.jp/data/bodyparts3d/ (`20080812` … `20130619`, `LATEST`).
  The live **Anatomography** UI at https://lifesciencedb.jp/bp3d/ **loads and renders in a
  browser as of 2026-09-13** — it was fetched *and* driven interactively.
- **The object and its frame.** Meshes segmented from **TARO**, a 2 mm whole-body MRI voxel model
  of one adult Japanese male. The NAR paper (https://academic.oup.com/nar/article/37/suppl_1/D782/1000752)
  states "BodyParts3D introduces a universal coordinate system in human anatomy". The frame is
  documented as *a diagram*, not prose — unit mm, body centreline ≈ z-axis, left x>0, right x<0,
  posterior y>0, anterior y<0, all z>0 superior-greater
  (https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/coordinate_system.png).
  `FRAME.md` does the same job with an ASCII diagram plus landmark tables, and is if anything
  better documented.
- **Counts, from the primary release note**
  (https://dbarchive.biosciencedbc.jp/data/bodyparts3d/LATEST/release_4.0_e.html, cross-checked
  against the raw `isa_parts_list_e.txt` / `partof_parts_list_e.txt`):

  | version | is-a tree (elem/comp) | part-of tree | in both | unique FMA |
  |---|---|---|---|---|
  | V2.0 (2010-04-28) | 843 / 643 | 408 / 326 | 406 | 845 / 969 |
  | V3.0 (2011-06-20) | 912 / 700 | 436 / 353 | 433 | 915 / 1053 |
  | V4.0 (2013-05-16) | 1651 / 1254 | 765 / 603 | 764 | 1652 / 1854 |

  A newer **v4.3** is reachable only from the live server
  (`https://lifesciencedb.jp/bp3d/get-info.cgi?version=4.3&cmd=concept-objfiles-list`): 5614
  concept rows = 3899 `is_a` + 1715 `part_of`, **4528 unique FMA concepts over 3,210 unique
  atomic meshes** (raw). Wikipedia's "1,324 / 1,523" figures
  (https://en.wikipedia.org/wiki/Anatomography) count something else — prefer the release note.
- **THE FINDING: BodyParts3D is itself a two-scheme atlas.** The same mesh set is partitioned two
  ways — by the FMA **`is_a`** tree and by the FMA **`part_of`** tree — and the two do not agree.
  In v4.3, 1086 FMA concepts appear in both trees and **87 of them resolve to a different set of
  meshes** depending on which tree you ask (in v4.0: 841 shared, **77 differing**) (raw,
  computed from `isa_element_parts.txt` / `partof_element_parts.txt`). A compound concept is
  literally a `+`-union of atomic meshes — `FMA10446 is_a FJ3202+FJ3203+…+FJ3224` — which is
  structurally *identical* to "a cut is a union of boxes". So the closest technical ancestor of
  this project's anatomy layer independently arrived at both the union-of-atoms data model and
  the two-competing-partitions problem.
  **But it never quantifies the disagreement.** `partof_inclusion_relation_list.txt` is a flat
  boolean containment table — `parent id / parent name / child id / child name`, 1368 rows. No
  percentages anywhere. That gap is this project's contribution.
- **IDs**: files named by FMA ID, with a minted fallback when FMA has no matching concept —
  verbatim from https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/README_e.html:
  "If a corresponding concept is not found in the FMA, a BodyParts3D's original ID that begins
  with 'BP' is assigned". From v4.0 the mesh files are `FJxxxx` with a separate concept↔file
  table — i.e. **the ID is deliberately not the name**, a discipline worth copying.
- **Format and size**: OBJ. Archive bundles are polygon-reduced to 99%:
  `isa_BP3D_4.0_obj_99.zip` = 142,903,898 bytes, `partof_BP3D_4.0_obj_99.zip` = 64,888,505 bytes
  (raw `Content-Length`). Full resolution only via Anatomography's `download.cgi`.
- **Licence — conflicting, flag it.** The archive licence page
  (https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html) says **CC BY 4.0**, attribution
  "BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0
  International". The live Anatomography footer and both GitHub mirrors still show the older
  **CC BY-SA 2.1 Japan**. Which governs, and when it changed, is **UNPROVEN**. If this project
  ever ingests BP3D meshes, resolve that before shipping — SA would be infectious.
- **UI ideas worth stealing** (observed directly in the running Anatomography):
  - **An IS-A Tree / HAS-PART Tree radio pair with live counts beside each**, swapping the
    partition scheme over identical geometry in one click. This is the best existing answer to
    "7 traditions, one cow" and it is a radio button, not a mode switch.
  - A **Segment × Volume cross-tab used as the navigation control** — body-segment rows against
    volume bins (`<0.1, 0.1–0.35, 0.35–1, 1–10, 10<` cc), each cell a clickable count. An
    overlap-style matrix used to *navigate*, not merely to report.
  - An **Intersection tab** with `ELEMENT / Complete COMPOUND / Incomplete COMPOUND` checkboxes —
    the data model already distinguishes fully- from partially-covered concepts, which is the
    qualitative shadow of this project's percentages.
  - **URL-encoded scenes**: `av, iw, ih, bcl, cf, bv, cx/cy/cz, tx/ty/tz, oid, ocl, osc, osz,
    oop, orp`, colours as hex (`ocl002=0000FF`) — object IDs, per-object colour, opacity and
    camera all in the query string
    (https://wiki.lifesciencedb.jp/mw/BodyParts3D/Anatomography.html). **Steal this wholesale**:
    it makes every view of the atlas a citable link, which is what a reference work needs.
  - A per-part side panel giving representation ID, represented FMA concept, component mesh list,
    an `[Icon URL]` permalink and a per-part `download obj files` button.
- **Derivative worth knowing: Z-Anatomy** — takes the BodyParts3D meshes and **re-partitions them
  under a third scheme, Terminologia Anatomica 2** (https://github.com/Z-Anatomy/The-blend,
  https://github.com/LluisV/Z-Anatomy, https://zenodo.org/records/4953712). So there now exist
  *three* partitions of one mesh set. Licence conflict again: GitHub says CC BY-SA 4.0, the
  Zenodo record says CC BY 4.0. Ships `.blend` (130 MB) and FBX.
- **No animal equivalent exists, open or commercial.** The parallel agent checked Waxholm Space
  rat (CC BY 4.0 but NIfTI label volumes, not meshes), Allen Mouse CCF (per-structure `.obj`
  downloads confirmed working, but a **custom non-commercial** licence — "may not redistribute
  the Content… for commercial purposes without our written permission"), Visible Human (public
  domain, but image slices with no named meshes), the 1999 Visible Animal Project (a dog;
  cryosections, no meshes distributed), IMAIOS vet-Anatomy (commercial, includes bovine, no data
  export), Biosphera (commercial apps, includes a cow), and the OBO registry.
  **There is no named-part 3D mesh set for cattle in a shared frame, under any licence.**
  That is a genuinely open niche and it is precisely what this project's anatomy layer is.

## 3. Anatomy ontologies — can the percentages ever live in one?

**No.** They can be attached *beside* an ontology as a weighted mapping table, and there is a
standard for that table, but no OBO/OWL relation carries a degree. Researched in parallel; the
neuroimaging literature in §1.1 reaches the same verdict independently, which is the strongest
part of this finding — two unrelated communities, same conclusion.

- **UBERON** — "An integrated cross-species anatomy ontology covering animals and bridging
  multiple species-specific ontologies", **CC BY 3.0** (https://obofoundry.org/ontology/uberon.html).
  Size depends on what you count: "over 13000" core / "over 40000" composite
  (https://obophenotype.github.io/uberon/about/); OLS4 API reports 26,624 terms
  (https://www.ebi.ac.uk/ols4/api/ontologies/uberon, almost certainly including imports); counting
  the 2026-06-19 `uberon-base.obo` source directly gives 16,071 UBERON stanzas of which 1,096 are
  obsolete → **14,975 live classes** (raw curl, http://purl.obolibrary.org/obo/uberon/uberon-base.obo).
- **The bridging machinery is all-or-nothing.** Terms carry `xref`s
  (`UBERON:0002107` liver → `FMA:7197, MA:0000358, EMAPA:16846, ZFA:0000123, XAO:0000133, …`,
  https://ontobee.org/ontology/UBERON?iri=http://purl.obolibrary.org/obo/UBERON_0002107), but the
  real logic lives in bridge files: `uberon-bridge-to-ma.owl` holds **6,130 `owl:equivalentClass`
  axioms** of the form `MA:0000001 ≡ UBERON:0001062 and (RO:0002162 'in taxon' some
  NCBITaxon:10090)` (raw curl,
  https://raw.githubusercontent.com/obophenotype/uberon/master/src/ontology/bridge/uberon-bridge-to-ma.owl).
  A term either *is* the Uberon term within a taxon, or it is not. **There is no 62%.**
- **RO has the qualitative relation and nothing more.**
  - **`RO:0002131` "overlaps"** — "x overlaps y if and only if there exists some z such that x has
    part z and z part of y"; symmetric; sub-property of `mereotopologically related to`
    (https://ontobee.org/ontology/RO?iri=http://purl.obolibrary.org/obo/RO_0002131, verified at
    line 1885 of the raw `ro.obo`).
  - **`RO:0002151` "partially overlaps"** (alt label "proper overlaps") — adds "neither x is part
    of y or y is part of x"; `is_a RO:0002131`. Its editor note is the whole story in one line:
    "We would like to include disjointness axioms with part_of and has_part, however this is not
    possible in OWL2 as these are non-simple properties and hence cannot appear in a disjointness
    axiom."
  - Grepping all of RO: the only "quantity" relations are regulatory (`regulates quantity of`).
    **No quantified spatial overlap relation exists.**
  - **Can OWL attach a degree?** Only as an axiom annotation, which is explicitly inert —
    https://www.w3.org/TR/owl2-primer/: "Annotation information is not really part of the logical
    meaning of an ontology" and "under the Direct Semantics annotations have no formal meaning."
- **SSSOM is where the numbers actually go.** (Simple Standard for Sharing Ontological Mappings;
  https://mapping-commons.github.io/sssom/dev/, schema at
  https://raw.githubusercontent.com/mapping-commons/sssom/master/src/sssom_schema/schema/sssom_schema.yaml.)
  `predicate_id` has `slot_uri: owl:annotatedProperty` — SSSOM *is* OWL reification in a TSV — and
  its range is an open `EntityReference`, so **`RO:0002151` is a legal predicate**. Two candidate
  numeric slots, neither a clean fit:
  - `confidence` — wrong: "the creator's confidence or estimated probability that the mapping
    record is correct." That is confidence in the assertion, not extent of overlap.
  - `similarity_score` — closer: "a score between 0 and 1 … where 1 denotes equivalence, and 0
    denotes disjointness", paired with a free-text `similarity_measure`. But it reads as
    **symmetric**, and this atlas's number is **directional**, so it cannot hold the pair.
  - The clean answer is `extension_definitions`, SSSOM's sanctioned typed custom columns, with two
    slots — e.g. `fraction_of_subject` and `fraction_of_object`. `mapping_cardinality`
    (`1:1`, `1:n`, …) captures the *shape* of the relationship but not the fraction.
- **FMA** — OBO Foundry status **inactive**, licence **CUSTOM**
  (https://obofoundry.org/ontology/fma.html). Counted from the 208 MB official release directly
  (raw curl, http://sig.biostr.washington.edu/share/downloads/fma/release/latest/fma.owl):
  **104,721 `owl:Class` declarations, 139 object properties, and zero properties whose name
  contains "overlap"**. Its spatial vocabulary is `adjacent_to`, `bounded_by`/`bounds`,
  `continuous_with`, `surrounds`/`surrounded_by` — all boolean topology, no degree.
- **NAV / Terminologia Anatomica — not machine-readable.** NAV current edition is the **6th, 2017**,
  distributed by WAVA as a ZIP/PDF (https://www.wava-amav.org/wava-documents.html), alongside
  Nomina Histologica Veterinaria (1st ed. 2017) and Nomina Embryologica Veterinaria (2nd rev.
  2017). Terminologia Anatomica 2nd ed. 2019 is **PDF only, CC BY-ND 4.0** with individual terms
  in the public domain (https://libraries.dal.ca/Fipat/ta2.html) — the ND clause means no legally
  derived machine-readable vocabulary.
- **No cattle anatomy ontology exists.** The full OBO Foundry registry (267 ontologies, raw curl
  of https://obofoundry.org/registry/ontologies.jsonld) contains no bovine/cattle anatomy
  ontology, active or inactive. `vbo` is the Vertebrate **Breed** Ontology (breed names,
  CC BY 4.0), not anatomy. UBERON's 74-file bridge directory covers mouse, human, zebrafish, fly,
  Xenopus, worm, spider, tick, NCIT, SNOMED — **no bovine bridge**
  (https://api.github.com/repos/obophenotype/uberon/contents/src/ontology/bridge). Cattle coverage
  in UBERON is species-neutral classes plus `in taxon` constraints.
- **The confirming quote, from the anatomy-ontology community itself.** Travillian et al.,
  "Anatomy ontologies and potential users: bridging the gap", *J Biomed Semantics* 2011, verbatim
  (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3194170/fullTextXML):
  > "a few cases of quantitative annotations, such as 75% kidney, 25% liver were present in the
  > annotations; these will be ruled out of scope in future testing, as very few present
  > ontologies can handle quantitative data. However, their presence does indicate a
  > currently-unmet user need in data annotation."

  Set that beside Bohland (§1.1, p.4): asymmetric overlap relations "are problematic for
  terminological ontologies that rely on simple categorical mappings and therefore lose
  information relative to the pair of conditional probability values we compute here."
  **Two independent communities, fifteen years apart, both report the same gap.** This project
  sits in it.

## 5. GIS — the discipline with the best-named methodology and the deepest precedent

This is the thread that supplies the *name*. Researched in parallel; every claim carries its
fetched URL.

- **Areal interpolation** is the umbrella term: "the process of transforming data from one spatial
  framework to another" — UCGIS GIS&T Body of Knowledge entry AM-02-040,
  https://gistbok-ltb.ucgis.org/current/concept/AM-02-040. The vocabulary, from the same page:
  **source zones** = "The original areas with known values or attributes before areal
  interpolation"; **target zones** = "The new areas, for which values will be estimated".
  Methods split into spatial-only (area-to-point, pycnophylactic, **areal weighted**) and
  ancillary-data (dasymetric, statistical, street-weighted).
- **THE FORMULA, and it is this project's formula.** From the `areal` R package vignette source
  (https://raw.githubusercontent.com/chris-prener/areal/master/vignettes/areal-weighted-interpolation.Rmd,
  corroborated at https://chris-prener.github.io/areal/articles/areal-weighted-interpolation.html):
  - **areal weight**: `W_i = A_i / A_j` — area of the intersected feature over the total area of
    the **source** feature. That is **|A∩B| / |A|**, directional, normalised on the source.
  - **extensive** (counts): `E_i = V_j · W_i`, summed into the target as `G_k = Σ E_ik`.
  - **intensive** (rates/densities): the denominator **flips to the target**, `W_i = A_i / Σ A_ik`.

  Lineage, from the CC-BY JOSS paper (Prener & Revord 2019, JOSS 4(37):1221,
  https://www.theoj.org/joss-papers/joss.01221/10.21105.joss.01221.pdf): estimating values for
  "an overlapping but incongruent set of polygon features is known as the *polygon overlay
  problem* (Goodchild, 1978), with the original data known as the 'source' data and the
  overlapping set of features known as the 'target' data (Markoff & Shapiro, 1973)";
  extensive/intensive is Goodchild & Lam (1980). Core assumption: "individuals are spread out
  evenly within the source features" — the same uniformity assumption this atlas makes when it
  treats a cut rectangle as homogeneous.
- **MAUP — the Modifiable Areal Unit Problem** (https://gistbok-ltb.ucgis.org/current/concept/FC-07-026,
  cite as Mennis, J. (2019), GIS&T BoK, DOI 10.22224/gistbok/2019.1.2): "an issue related to the
  analysis of spatially aggregated data where the results of mapping or statistical analysis may
  differ when using different spatial units of aggregation." Two components, defined there:
  **scale** = "the number, and, relatedly, the size, of spatial units used to partition an area";
  **zoning** = "the shapes and boundaries of the spatial units" — two schemes may have the same
  number of units but differ in configuration. Canonical citation: **Openshaw, S. (1984), *The
  Modifiable Areal Unit Problem*, Concepts and Techniques in Modern Geography No. 38, Geo Books.**
  **This is the discipline's name for the thesis of `docs/differences.md`** — that the answer
  depends on how you cut it — and the scale/zoning split maps exactly onto this atlas's two
  findings: France has *more, smaller* cuts (scale) and Britain places its boundaries one primal
  forward (zoning). Use both words.
- **Dasymetric mapping** (https://gistbok-ltb.ucgis.org/current/concept/CV-04-011): "a thematic
  map that uses ancillary data to determine new more meaningful borders of enumeration units,
  improving the representation of the spatial distribution of the mapped phenomenon." Ancillary
  data is **exclusionary** (where the phenomenon cannot occur) or **inclusionary** (a strong
  positive correlate). The relevance here: the atlas's 115-part anatomy layer is exactly the
  ancillary data that would turn its areal weighting into dasymetric weighting — "how much of
  this cut is *muscle X*" is better evidence than "how much of this rectangle overlaps".
- **The best-named precedent: the allocation factor.** MABLE/Geocorr, Missouri Census Data Center,
  https://mcdc.missouri.edu/help/data-allocation, verbatim:
  > "When associated with more than one target area it is important to have an **allocation
  > factor** to indicate what portion of the source area belongs to the target."

  The Census Bureau's own how-to
  (https://www2.census.gov/data/api-documentation/address-search/using-geocorr-urban-rural-mix.pdf)
  shows the column literally named **`afact`**; the weighting variable is user-chosen —
  Population, **Land area (square miles)**, or Housing units — and an option produces "a second
  allocation factor [AFACT2] showing portion of target geocodes in source geocodes", i.e. the
  *other* direction. Worked output (Cochise County R = 0.3677, U = 0.6323) sums to 1 over targets,
  confirming the **source is the denominator**. **With land-area weighting, `afact` is exactly
  |A∩B|/|A|** — the beef atlas's number, under a settled government-published name, with a
  named convention for publishing the reverse direction too.
- **Census Bureau relationship files** publish the raw intersection.
  https://www2.census.gov/geo/pdfs/maps-data/data/rel2020/tract/explanation_tab20_tract20_tract10.pdf:
  "Each record in the file represents one relationship that is formed when a 2020 TRACT intersects
  a 2010 TRACT." Fields include the full identity block for each side plus **`AREALAND_PART`** and
  **`AREAWATER_PART`** — an explicit overlap-area column, with ratios left for the user.
  Arithmetic verifies in their own Example 3 (6203654 + 2097390 + 3107823 = 11408867 =
  `AREALAND_TRACT_10`).
- **HUD USPS ZIP crosswalks** — huduser.gov returned empty bodies on four URLs and web.archive.org
  is blocked, so **HUD's own wording and terms of use are UNPROVEN**. Secondary but fetched:
  https://etam4260.github.io/hudpy/build/html/usps_crosswalk.html gives `res_ratio` as "The ratio
  of residential addresses in the ZIP – Tract, County, or CBSA part to the total number of
  residential addresses in the entire ZIP", with `bus_ratio`, `oth_ratio`, `tot_ratio` identical
  over business / other / all addresses — denominator is the **ZIP (source)**. Inverse-direction
  files exist but "inverse relationships…are NOT COMPLETELY inverse", which is a useful warning:
  publishing both directions is not the same as publishing one and inverting it.
  https://cran.r-project.org/web/packages/zippeR/vignettes/converting-zips.html confirms the four
  column names and that an API key is required.
- **NHGIS** — nhgis.org returns 403 to WebFetch, so its weight column names, TDW methodology and
  data licence are **UNPROVEN**. Fetched instead: https://tech.popdata.org/nhgisxwalk/ and
  https://raw.githubusercontent.com/ipums/nhgisxwalk/main/README.md — crosswalk rows are **atoms**,
  "the smallest intersecting units", each row carrying a source ID, a target ID and "at least one
  column of weights", the weights being "the interpolated proportions of source attributes that
  are calculated as being within the target units". MPL-2.0 covers the *software* only.
- **Is the full pairwise matrix published as open data? Yes.**
  https://www2.census.gov/geo/docs/maps-data/data/rel2020/tract/ lists
  `tab20_tract20_tract10_natl.txt` (18 MB, 2022-01-25) plus per-state files — the complete
  national pairwise 2010×2020 tract intersection table, plain text, no registration.
  **Solid precedent for shipping the whole overlap matrix as a file.**
- **Ranked candidate names** for this project's number, by strength of primary-source precedent:
  **allocation factor** (Geocorr — defined exactly as portion-of-source-in-target, has a named
  reverse, and a pure-geometry land-area variant) > **areal weight** (the GIS&T/textbook term for
  the same quantity) > **interpolation weight** (NHGIS) > **crosswalk** / **correspondence file**
  (the container, not the number) > "apportionment weight" (no primary source — do not lean on it).
- **3D version**: a voxel-overlap interpolation *between two 3D partitions of one solid* was not
  found. Closest fetched precedent is Biljecki et al. (2016), PLOS ONE, CC-BY
  (https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0156808), which
  disaggregates population weighted by "(i) area of the 2D building footprints (in m2), (ii) area
  of the building floorspace (in m2), and (iii) building volume (in m3)" — dasymetric
  interpolation with a *volumetric ancillary variable*, not 3D-to-3D overlap. Note this matters
  less than it first appears, because (see below) this atlas's published percentages are
  **2D areal**, not volumetric — so the standard 2D method applies directly, unextended.

---

## What this atlas actually computes, and what to call it

Read from the repo (not inferred). `web/app.js` lines 213-229:

```js
function rectArea(r) { return (r.x[1] - r.x[0]) * (r.z[1] - r.z[0]); }

function overlapArea(a, b) {
  const ox = Math.max(0, Math.min(a.x[1], b.x[1]) - Math.max(a.x[0], b.x[0]));
  const oz = Math.max(0, Math.min(a.z[1], b.z[1]) - Math.max(a.z[0], b.z[0]));
  return ox * oz;
}

// What fraction of `a` lies inside `b`.
function overlapFraction(a, b) {
  const area = rectArea(a);
  return area > 0 ? overlapArea(a, b) / area : 0;
}
```

and `docs/differences.md`: "When this piece says the American short loin is '82% the British
sirloin', it means 82% of the American rectangle is covered by the British one."

So the published number is **area(a ∩ b) / area(a)** — **directional**, **two-dimensional** (the
x–z side-view projection; y is discarded), and computed on **a single bounding rectangle per cut**,
not on the box union that `FRAME.md` describes. Three consequences:

1. **It is exactly Bohland's Equation 3** with the denominator cut as *j* and the numerator cut as
   *i*: `overlapFraction(a, b)` = P(b | a) = |r_b ∩ r_a| / |r_a|. Note the index order is the
   reverse of Bohland's reading order — his P_ij is "the proportion of r_j contained within r_i",
   so the atlas's `overlapFraction(a,b)` is his **P_ba**. Whichever notation is adopted, write the
   direction out in words somewhere, because the subscripts fool everyone.
2. **It is exactly the GIS areal weight** `W = A_i / A_j`, with the source zone as the denominator
   — i.e. Geocorr's **allocation factor** under land-area weighting. The measure is *area*, so no
   "volumetric" extension is needed and none should be claimed; the standard 2D method applies
   verbatim.
3. **It is not Dice and not Jaccard**, and that is correct and defensible rather than a shortcut.
   Bohland's own justification, verbatim (p.15): Dice and Jaccard "can only take [their] maximum
   value of 1 when the regions are *identically* defined. P_ij is instead 1 when there is a pure
   subset relationship, even when P_ji < 1." Since French cuts are largely *refinements* of
   American ones, a symmetric index would report near-total disagreement where the truth is clean
   containment.

### Recommendation, in one sentence

**Call it the *conditional overlap* — "what fraction of cut A lies inside cut B" — state in
`differences.md` and in the UI that it is Bohland et al.'s non-symmetric conditional overlap
P(i|j) (PLoS ONE 2009, Eq. 3), identical in form to the GIS *allocation factor*, ship the full
directional matrix as a file in the repo, and always publish or display both directions.**

Concretely, in priority order:

1. **Name and cite it.** One sentence in `docs/differences.md`: *"This is the non-symmetric
   conditional overlap P(i|j) of Bohland et al. (2009), the standard measure for comparing two
   parcellations of one object; geographers call the same quantity an allocation factor."* That
   converts an informal percentage into a cited method at a cost of one line.
2. **Always show both directions.** P(i|j) ≠ P(j|i), and the atlas's most quotable finding — the
   British false friend at "82% in both directions" — is *only* meaningful because both were
   checked. HUD publishes both directions and warns they are "NOT COMPLETELY inverse"; make that
   the house rule, not a special case.
3. **Ship the matrix as a file.** `obart.info`, which held the only published parcellation overlap
   matrix, is gone — the numbers survived 17 years only as figures in a PDF. The Census Bureau
   ships `tab20_tract20_tract10_natl.txt` as plain text with no registration. Do that: a
   `data/overlap.csv` of `culture_a, cut_a, culture_b, cut_b, frac_a_in_b, frac_b_in_a`.
4. **Add one headline scalar per tradition-pair: Bohland's S-index** (Eq. 7, §1.1). It is
   `S = 1 − 4 Σ W_ij X_ij (1 − X_ij)` over the numbers the atlas already has, it does not
   penalise France for being a refinement of America the way the Adjusted Rand Index would, and
   it turns a 153×153 matrix into a 7×7 table — which is the table `differences.md` is reaching
   for when it falls back on mean cut size.
5. **Add the bipartite grouping** (Eq. 5 + edge pruning, §1.1). `E_ij = max(P(i|j), P(j|i))`,
   prune the weakest edges, take connected components: each component says "this group of American
   cuts ≈ this group of Japanese cuts". That is the answer a cook actually wants, and no butchery
   resource found in any of these threads provides it.
6. **Adopt "common coordinate framework" for `FRAME.md`** and "the concordance problem" for what
   `differences.md` describes — both are established terms (§1.5, §1.1). Borrow **MAUP**, with its
   *scale* vs *zoning* split, to frame the France-has-smaller-cuts and Britain-is-shifted-forward
   findings as two named effects rather than two anecdotes.
7. **Two honesty notes the prior art obliges.** (a) The percentages are 2D side-view areas on
   bounding rectangles — `differences.md` already says this well; keep saying it, because
   everything it is being compared to here is volumetric. (b) If the overlaps are ever published
   as data, add a chance baseline: Bohland's random size-matched partitions and Kay & Regier's
   hue-rotation Monte Carlo are both cheap to imitate, and without one, "82%" has no scale.
8. **If the cross-tradition mappings are ever exported for machines**, use **SSSOM** with
   `predicate_id: RO:0002151` (partially overlaps) plus two `extension_definitions` columns for
   the directional fractions (§3). Do not try to put the numbers in an ontology; no OBO/OWL
   relation carries a degree, and the anatomy-ontology community has said so in print.

---

## Method notes / audit trail

- Every equation and every verbatim quote in §1.1 and §4.1-4.2 was read **directly from the PDF**
  via page-image extraction, not through a summarizer. This mattered: a WebFetch summary of
  Bohland's Table 1 returned eight region counts (34/45/45/61/59/48/40) that do **not** appear in
  the paper at all; the real counts are in the table above. Treat WebFetch numeric output as a
  lead, never as a citation.
- Fetches that failed, and how: `obart.info` — DNS ENOTFOUND (site gone). `web.archive.org` —
  blocked to this agent. `cell.com`, `pnas.org/doi/full/…`, `nature.com/articles/…` — HTTP 403 or
  IdP redirect. `pmc.ncbi.nlm.nih.gov`, `pubmed.ncbi.nlm.nih.gov` — cookie wall, content not
  returned. `icsi.berkeley.edu` / `www1.icsi.berkeley.edu` — connection refused.
  Open-access mirrors that *did* work: journals.plos.org (PDF), pure.mpg.de, arxiv.org,
  terry-regier.github.io, biorxiv.org, github.com, alleninstitute.github.io, joss.theoj.org,
  scalablebrainatlas.incf.org.
- Three claims in this file originally came from WebFetch summaries and were **corrected** after
  fetching a primary source: Bohland's Table 1 region counts (summarizer invented eight numbers);
  Coord2Region's licence (paper licence reported as code licence — it is BSD-3-Clause); and
  AtlasReader's default atlas list (not actually stated in the README, now marked UNPROVEN).
  The parallel agents hit the same class of failure independently — one reports WebFetch returning
  "a *different, wrong* definition" for the `RO:0002131` stanza in a raw file it had fetched
  correctly. Treat the summarizer as a search tool, never as a source.
- Measure-theoretic note, so the analogy does not get challenged: brain parcellation counts
  **voxels**, GIS counts **2D area**, the WCS counts **chips**, and this atlas — per `web/app.js`,
  not per `FRAME.md` — counts **2D area of a bounding rectangle in the x–z projection**. All four
  are the same construction: a measure μ on a shared frame, with P(i|j) = μ(r_i ∩ r_j) / μ(r_j).
  The method transfers; only the measure changes. Because this atlas's measure is *areal*, the GIS
  areal-interpolation literature applies to it **literally**, not by analogy — that is the
  strongest single fact in this file after Bohland.
- **Open question left for whoever picks this up.** `FRAME.md` defines a cut as a union of 3D
  boxes, but `web/app.js` computes overlap on one bounding rectangle in 2D. Whether the published
  percentages should move to box-union area (still 2D, but honest about irregular shapes) or to
  box-union volume (3D, and then the y-blindness caveat in `differences.md` disappears) is a real
  decision with real consequences for every number in that document. Nothing in this thread
  settles it; it is flagged, not answered.
