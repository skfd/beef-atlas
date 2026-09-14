# Prior art, shape thread 1 — cuts as geometry in a real coordinate frame

Raw research notes. Research date **2026-09-13**. Every claim below is tagged with the URL it came
from and whether that URL was actually fetched. `[VERIFIED]` = I fetched it and read the text.
`[SNIPPET]` = search-engine summary only, not fetched. `[UNPROVEN]` = fetch blocked, claim not
testable either way.

---

## Summary

**The industrial/scientific cousin of this atlas exists, and it is the Auckland Bioengineering
Institute lineage — but it stops one step short of what this repo does, in the same place every
time: one tradition.** Ho, Yu, Gangsei & Kongsro built a CT-derived *pig atlas* of 84 muscles and
121 bones as a parametric cubic-Hermite mesh and named "virtual meat cuts" as its application
(Meat Science 2019); Ritchie & Ho then put a *lamb carcass musculoskeletal model (or atlas)*
into Unity3D and drove a virtual knife through it "as per standard meat cut specifications of New
Zealand", getting per-cut volume and weight out (NZ J Ag Res 2025 — the atlas is reported elsewhere
as CT-derived with 38 muscles, but that detail is unverified; see below). That is features 1, 3 and 4 of
this atlas, in one animal frame, for one national cutting standard each — and neither publishes the
cut geometry, only the anatomy that the cuts were applied to, and neither is open. The robotics
side is closer to real cut *surfaces*: de Medeiros Esper et al. (Smart Agricultural Technology 2024,
the EU RoBUTCHER project) build a CT 3D model, register it to a live point cloud with Bayesian
Coherent Point Drift, and generate cutting trajectories from "a custom 3D model of the cutting
surface" — an actual published description of a cut as a surface in a scanned animal's frame, again
for one cutting scheme (pig, Meat Factory Cell). Everything else in the CT/DXA/X-ray carcass
literature — Teagasc, SRUC, MLA/CSIRO, Norwegian, Danish — publishes **yields and prediction
equations, never cut geometry**. There is no bovine "Visible Human"; the Visible Animal Project is a
dog. And I found **no empirical trial that cut matched carcasses two different national ways and
reported the overlap**; the nearest thing is a Colorado State study that fabricated US carcasses
21,504 different ways *within* the US tradition. On the specific question this atlas answers —
how much of a French *entrecôte* is an American ribeye — nobody has measured it geometrically, and
the only prior quantification of partial cut equivalence at all is Swatland's binary name-overlap
score (already known to this repo).

---

## TOP 3 HITS

### 1. Ho, Yu, Gangsei & Kongsro (2019) — CT-image based **pig atlas model** [VERIFIED]

- DOI `10.1016/j.meatsci.2018.09.011`, *Meat Science* 148 (2019) 1–4. PMID 30292698.
- Authors and affiliations **[VERIFIED]** — printed from Europe PMC `authorAffiliationDetailsList`:
  - **H. Ho** — *Auckland Bioengineering Institute, The University of Auckland, New Zealand*
    (`harvey.ho@auckland.ac.nz`)
  - **H.B. Yu** — *Auckland Bioengineering Institute, The University of Auckland, New Zealand*
  - **L.E. Gangsei** — *Animalia, Norwegian Meat and Poultry Research Centre, Norway; Norwegian
    University of Life Sciences, Norway*
  - **J. Kongsro** — *Norsvin SA, Oslo, Norway*
- Abstract fetched verbatim from Europe PMC REST
  (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"A CT-image based pig atlas model"&format=json&resultType=core`):

  > "In this communication we present a novel pig atlas model which is represented by a parametric
  > linear Lagrange or cubic Hermite mesh. The model is developed from data points digitized from a
  > 3D pig CT image. In total 84 muscles and 121 bones are included in the atlas, representing the
  > tissue structures most relevant to the industry. We discuss its potential applications in
  > virtual meat cuts and statistical shape analysis for pig breeding and genetics companies."

- **Coordinate frame**: yes — a single CT specimen's frame, all 84 muscles and 121 bones digitised
  into one parametric mesh. This is the same architectural idea as `data/FRAME.md`, but built from a
  real scan rather than authored boxes, and for pig not cattle.
- **Cut geometry published?** No. "Virtual meat cuts" is named as a *potential application* in the
  abstract; the abstract does not claim cut boundaries were defined or published. Full text is
  paywalled (Europe PMC `isOpenAccess: N`, no PMCID) — **internals UNPROVEN**, do not assume the
  paper contains cut definitions.
- **Traditions**: none stated in the abstract. Zero cross-tradition content.
- **Open access**: No.
- Same group's adjacent work, all [VERIFIED] via Europe PMC `AUTH:"Gangsei LE"`:
  - Kvam, Gangsei, Kongsro, Schistad Solberg (2018), *Translational Animal Science*,
    DOI `10.1093/tas/txy060`, PMC7200429, **OA** — deep-learning automatic segmentation of the pig
    skeleton from CT volumes.
  - Nordbø, Hassan, Gangsei, Grindflek, Olstad (2026), *J. Animal Science*,
    DOI `10.1093/jas/skaf449`, PMC12923158, **OA** — anatomic segmentation model over whole-body pig
    CT, "29 classes of different tissues, like individual bones, muscles, and organs", joint centre
    detection validated at 29 mm mean error. Topigs Norsvin breeding programme.
  - So: an industrial pipeline that routinely turns pig CT into per-bone, per-muscle 3D labels
    exists and is partly open. It is aimed at breeding and osteochondrosis, not at cuts.

### 2. Ritchie & Ho (2025) — **VR meat cut planning on a lamb carcass atlas** [VERIFIED]

- DOI `10.1080/00288233.2024.2305825`, *New Zealand Journal of Agricultural Research* **68**(5),
  1125–1131 (issued 2025-10; online 2024).
- Authors and affiliations from Crossref (`https://api.crossref.org/works/10.1080/00288233.2024.2305825`)
  [VERIFIED]: **Aaron Ritchie** and **Harvey Ho**, both *Auckland Bioengineering Institute, The
  University of Auckland*. (Same Harvey Ho as the pig atlas — this is one research lineage, not two.)
- Crossref-deposited abstract, verbatim [VERIFIED]:

  > "Consumer-level Virtual Reality (VR) hardware/software has undergone rapid developments in recent
  > years. Its potential use in the meat industry for meat cut planning has yet to be reported. In
  > this communication, we introduce a VR system based on a VR goggle (Oculus Rift) and a hand motion
  > sensor. A lamb carcass's musculoskeletal model (or atlas) is imported into an immersive virtual
  > environment, created by a 3D VR engine (Unity3D). Virtual resection is performed by using a
  > virtual knife operating on the virtual atlas as per standard meat cut specifications of New
  > Zealand. The procedure yields instant volume and weight information of each primary and retail
  > meat cut. We suggest that the VR system can potentially be used in a high-volume slaughterhouse
  > for meat-cut planning and marketing decisions."

- Crossref licence field lists `http://creativecommons.org/licenses/by-nc-nd/4.0/`, but
  `tandfonline.com` returned **403** to both WebFetch and curl, and `web.archive.org` replay of the
  same URL also returned 403. **Full text not read.**
- **[SNIPPET — UNVERIFIED]** A WebSearch summary of the full article states the atlas "was built from
  CT images of a lamb carcass weighing 20.1 kg and comprised an ovine skeleton and 38 muscles
  represented by parametric cubic Hermite mesh" and "was developed previously at the University of
  Auckland". Consistent with the pig atlas method and the shared author, but **I did not fetch the
  sentence** — treat the 20.1 kg / 38-muscle / Hermite details as unconfirmed.
- **Coordinate frame**: one lamb carcass atlas, cuts applied inside it (the abstract says
  "musculoskeletal model (or atlas)" and nothing about how it was built). Closest published thing to
  this repo's shape.
- **Cut geometry published?** No indication. The output described is volume and weight per cut, not
  the cut surfaces. No data availability statement seen.
- **Traditions**: exactly one — New Zealand. Explicitly "as per standard meat cut specifications of
  New Zealand".
- **Open access**: effectively no (403 everywhere I tried).

### 3. de Medeiros Esper, Gangsei, Cordova-Lopez, Romanov, Bjørnstad, Alvseike, From & Mason (2024) — **3D model based adaptive cutting system for the meat factory cell** [VERIFIED via DOAJ]

- DOI `10.1016/j.atech.2023.100388`, *Smart Agricultural Technology* (2024). EU **RoBUTCHER** project.
- Affiliations **[VERIFIED]** from the paper's own title page (salvaged PDF, see below): all authors
  are **a** *Norwegian University of Life Sciences, Faculty of Science and Technology,
  Universitetstunet 3, Ås, 1433, Norway* and/or **b** *Animalia AS, Oslo, 0585, Norway*.
  (Gangsei and Mason carry both.) Corresponding: `mason@nmbu.no`.
- OpenAlex (`https://api.openalex.org/works/doi:10.1016/j.atech.2023.100388`) [VERIFIED]:
  `is_oa: true`, `oa_status: gold`, licence `cc-by-nc-nd`.
- Abstract verbatim from DOAJ API
  (`https://doaj.org/api/v2/articles/55450b94fdb54c8590e1773f7fd1dd16`) [VERIFIED]:

  > "This article presents a comprehensive framework for executing primal cuts on pigs within a Meat
  > Factory Cell (MFC) context, with potential applications for small and medium-sized producers. The
  > framework begins by creating a 3D model from CT-scans, which is then aligned with a 3D point cloud
  > acquired from an Intel© Realsense™ camera using an initial coarse estimate, and refined through
  > Bayesian Coherent Point Drift. **Cutting trajectories are generated based on a custom 3D model of
  > the cutting surface, designed with consideration of the pig's skeletal structure and the cutting
  > properties of the knife tool attached to the robot.** A qualitative evaluation of the cuts
  > performed by a professional butcher reveals promising results, while also identifying areas for
  > improvement. The article underscores the potential of integrating CT-scans, 3D point clouds, and
  > cutting models to automate primal cuts in the meat industry, addressing the inherent anatomical
  > variability among animals."

- **This is the only paper I found that states, in a fetched sentence, that a cut is represented as a
  3D surface model in a scanned animal's frame.** Registration is CT template → per-animal point
  cloud (Bayesian CPD), i.e. a canonical frame deformed onto each individual — the industrial
  analogue of `FRAME.md` normalisation.
- **Partially recovered full text [VERIFIED].** `robutcher.eu` itself returns
  **ECONNREFUSED 82.165.235.55:443** (site down, not blocking), and `sciencedirect.com` 403s — but the
  Wayback CDX API lists two captures of the robutcher.eu PDF mirror
  (`20240523082329`, `20241111140924`, ~985 KB stored each) and the `…id_/` replay served a PDF.
  **The download is capped at exactly 1,048,576 bytes**, so the file is truncated and pypdf refuses
  it; I salvaged ~36 kB of text by decompressing the intact FlateDecode content streams directly.
  That covers the title page and Introduction, **not** the Methods. Two sentences worth having,
  verbatim from the paper's own Introduction:

  > "In this work, a novel framework for an adaptive cutting system is investigated and proposed in
  > the context of the MFC. It uses an **anatomical atlas, based on computer tomography (CT) data of
  > pig carcasses, to adapt the cutting trajectories for each pig being processed** to overcome the
  > natural variability."

  Keywords printed on the title page: "Meat factory cell (MFC); Pork primal cuts; **CT-scan generated
  model**; 3D point clouds; Bayesian coherent point drift; **Cutting trajectories**; Meat processing
  industry."

  One nuance the salvaged text does settle: the knife geometry is expressed in the **robot's** frame,
  not the animal's — "three virtual knife tools are defined in the robot's controller, these tools are
  defined in relation to the reference frame at the end-effector… The TCP translation, i.e., the tip
  of the knife, is the same for all knives and set to the values 9.12786, 20.2347, 446.024". The
  animal-frame part is the CT atlas that the trajectories are adapted *to*.
- **Cut geometry published?** The cutting-surface model is *described*; whether its parameters are
  given remains **UNPROVEN** — the Methods section is in the truncated half of the PDF. The salvaged
  text contains no occurrence of "spline", "mesh", "NURBS", "Bézier", "landmark" or "data
  availability", but that is over ~36 kB of a ~2.6 MB paper and proves nothing either way.
- **Traditions**: one — the MFC pig primal scheme (limbs first, then dorsal muscles with column and
  rind in one cut; see Alvseike 2020 below). Notably this is itself a *novel* partition, not a
  national one.
- **Open access**: gold OA, CC BY-NC-ND — but not reachable from here today.

---

## The rest of the RoBUTCHER / Meat Factory Cell cluster [all VERIFIED via Europe PMC REST]

- **Alvseike, Prieto, Bjørnstad, Mason (2020)**, "Intact gastro-intestinal tract removal from pig
  carcasses in a novel Meat Factory Cell approach", *Acta Veterinaria Scandinavica*,
  DOI `10.1186/s13028-020-00546-y`, PMC7457347, **OA**. Affiliations [VERIFIED via Europe PMC]:
  Alvseike, Bjørnstad and Mason at *Animalia — Norwegian Meat and Poultry Research Center, Oslo*
  (Mason also NMBU Ås); Prieto at *University of León, Spain*. Describes the MFC partition in words:
  > "In MFC, the limbs are removed first. Then the dorsal muscles along the spinal axis from tail to
  > head are removed with the column and rind in one meat cut, followed by removal of the viscera.
  > Finally, the cut ribs and belly are removed."
  A deliberately *new* eighth partition of the animal, invented for robots rather than inherited from
  a butchery tradition. Interesting as a case that a partition can be designed, not just recorded.
- **de Medeiros Esper, Cordova-Lopez, Romanov, Alvseike, From, Mason (2022)**, "Pigs: A stepwise
  RGB-D novel pig carcass cutting dataset", *Data in Brief*, DOI `10.1016/j.dib.2022.107945`,
  PMC8866887, **OA**. Affiliations [VERIFIED via Europe PMC]: *Norwegian University of Life Sciences,
  Faculty of Science and Technology, Ås* and *Animalia AS, Oslo*.
  Six Intel RealSense D415 cameras on a bespoke frame plus a robot-arm-mounted
  camera; bag files with RGB-D and intrinsics, **plus ten JSON files of per-camera transformation
  matrices relative to the left/front camera**. This is the **only openly published carcass geometry
  data I found in the entire robotics cluster** — but it is camera extrinsics and depth frames, not
  cut surfaces, and the frame origin is a camera rig, not the animal.
- **Takács et al. (2024)**, "Sensor-Enhanced Smart Gripper Development for Automated Meat
  Processing", *Sensors*, DOI `10.3390/s24144631`, PMC11281046, OA. Gripper mechatronics; no cut
  geometry.
- **de Medeiros Esper, From, Mason (2021)**, "Robotisation and intelligent systems in abattoirs",
  *Trends in Food Science & Technology*, DOI `10.1016/j.tifs.2020.11.005`, not OA. Abstract names the
  commercial systems reviewed: **Frontmatec AiRA** robots for pork slaughterlines, **Mayekawa
  Hamdas-RX** for deboning pork ham, **SCOTT Automated Boning Room** for lamb slaughterlines, and
  SRDViand. Useful as a citable index of who builds these machines. Internals UNPROVEN (paywalled).
- **Kim, Kwon, Kim, Seol, Cho (2023)**, "Robot Technology for Pork and Beef Meat Slaughtering
  Process: A Review", *Animals*, DOI `10.3390/ani13040651`, PMC9951719, **OA**.
- **Xu et al. (2024)**, "Robotization and intelligent digital systems in the meat cutting industry",
  *Trends in Food Science & Technology*, not OA.

## Commercial machine vendors — what they say about the cutting plane

- **Scott Automation** — `https://scottautomation.com/en-us/products/meat` [VERIFIED, fetched].
  Verbatim from the page:
  > "Our X-Ray Primal System creates a 3D map of the bones within a carcass, providing the correct
  > height and angle measurements for each cut."
  So the *representation* is a per-carcass 3D bone map plus, per cut, a **height and an angle** — i.e.
  a plane, parameterised in the carcass's own frame. Nothing published beyond that sentence. Product
  list on the page: BladeStop, Lamb Processing Solutions, Beef Processing Solutions, Poultry Trussing,
  Grading & Objective Carcass Measurement, Back-end Automation.
- **Frontmatec, Marel, DMRI** — no fetched primary source describing their cut representation.
  [SNIPPET, UNVERIFIED] search summaries say Frontmatec uses X-ray including a pubic bone detector for
  carcass measurement, and Marel and E+V use vision to register carcass position and determine a
  cutting trajectory. **Not verified — do not cite.**
- **DMRI / Danish Technological Institute** — searched for "virtual slaughterhouse" and "digital
  twin"; **no such project name found**. [SNIPPET] summaries describe DMRI 3D loin trimming (an exact
  3D computer image of each pork loin, fat/meat boundary found, eight knives, four seconds, with
  Frontmatec/Tican/Danish Crown) but I did not fetch a DMRI page saying it. The DMRI brochure at
  `https://www.dti.dk/_root/media/37612_FINAL_DMRI_brochure_M65_260609_small.pdf` was located but not
  fetched. **Whole DMRI line is UNVERIFIED.**

---

## CT / DXA / X-ray carcass composition — yields, never geometry

Consistent finding across the whole field: these programmes scan carcasses or primals, then regress
**tissue weights** against the scan. The cut boundaries are made with a knife by a human before or
after scanning; they are never the output.

- **Kongsro, Røe, Aastveit, Kvaal, Egelandsdal (2008)**, "Virtual dissection of lamb carcasses using
  computer tomography (CT) and its correlation to manual dissection", *Journal of Food Engineering*
  **88**, 86–93, DOI `10.1016/j.jfoodeng.2008.01.021` [VERIFIED bibliographic record via Crossref;
  **no abstract deposited**, ScienceDirect 403 → contents UNPROVEN]. Norwegian group — *institutional
  affiliations inferred from the author names, not fetched.*
  The phrase "virtual dissection" in this literature means *classifying voxels into muscle/fat/bone*,
  not *partitioning the animal into named cuts* — worth being precise about, because the phrase looks
  like it means the latter.
- **Navajas, Glasbey, Fisher, Ross, Hyslop, Richardson, Simm, Roehe (2010)**, "Assessing beef carcass
  tissue weights using computed tomography spirals of primal cuts", *Meat Science* **84**, 30–38,
  DOI `10.1016/j.meatsci.2009.08.006` [VERIFIED bibliographic; abstract not deposited; contents
  UNPROVEN]. *Affiliations inferred from the author names (SAC/SRUC, Bristol, BioSS) — not fetched.*
  Note the method: **the carcass is cut into primals first, by
  hand, then each primal is scanned** — beef carcasses do not fit a CT gantry. So the geometry is
  destroyed before the scan, which is structurally why nobody in this field ends up with cut surfaces
  in a whole-animal frame.
- **Navajas et al. (2010)**, "Predicting beef carcass composition using tissue weights of a primal cut
  assessed by computed tomography", *Animal* **4**, 1810–1817, DOI `10.1017/s1751731110001096`
  [VERIFIED bibliographic only].
- **Nisbet, Lambe, Miller, Doeschl-Wilson, Barclay, Wheaton, Duthie (2025)**, "Meat yields and primal
  cut weights from beef carcasses can be predicted with similar accuracies using in-abattoir 3D
  measurements or EUROP classification grade", *Meat Science* **222**, 109738,
  DOI `10.1016/j.meatsci.2024.109738`, Crossref licence **CC BY** [VERIFIED bibliographic; abstract
  not deposited; ScienceDirect 403]. *SRUC affiliation inferred from the author names, not fetched.*
  3D imaging of carcasses in-abattoir → predicted primal cut
  *weights*. Geometry in, numbers out.
  Companion: Nisbet et al. (2024), *Meat Science* **209**, 109391, DOI `10.1016/j.meatsci.2023.109391`,
  CC BY.
- **MLA "Objective carcase measurement" factsheet** (May 2015), Meat & Livestock Australia,
  `https://www.mla.com.au/globalassets/mla-corporate/generic/research-and-development/objective-carcase-measurement.pdf`
  — **[VERIFIED]**, fetched as PDF and text-extracted with pypdf (WebFetch alone returned binary
  noise). Relevant verbatim passages:
  > "Objective carcase measurement refers to the processes and technologies that have the potential to
  > be used to better measure carcase attributes to predict eating quality, disease or contamination,
  > **precise boning cutting lines**, and lean meat yield."

  > "Processors are already installing technologies which use skeletal measurements to guide manual
  > and robotic cutting."

  > "**Single source x-ray** (right): Two dimensional images are produced using single source x-ray
  > radiation (SEXA). By creating images of the skeletal components this technology can deliver
  > precise automated cutting of carcase primals."

  > "For example, at JBS Australia's plant at Bordertown, South Australia, dual-emission x-ray analysis
  > is being used to provide two and three dimensional views of each carcase that passes through the
  > plant's LEAP automated cutting system... This combines lean meat yield predictions with optimum
  > cutting lines for a high degree of accuracy and increasing value."

  So MLA confirms the industry computes cutting lines from skeletal scans. It publishes **no
  geometry**, and the factsheet is explicitly "Reproduction in whole or part of this publication is
  prohibited without prior consent" — not open.
- **MLA DEXA project pages** (located, not fetched): P.PSH.1344 (2023) and P.PSH.1201 (2022),
  "NUCTECH DEXA carcase analysis for lean meat yield measurement",
  `https://www.mla.com.au/research-and-development/reports/2023/p.psh.1344---nuctech-dexa-carcase-analysis-for-lean-meat-yield-measurement/`.
  [SNIPPET] DEXA is accredited for lamb **lean meat yield**; MLA states a need to "fast-track primal
  yield measurement with DEXA to get to primal yield" — i.e. per-primal yield is a stated *gap*, not
  a solved thing, as of those reports. UNVERIFIED.
- **Teagasc-adjacent DXA work**: searched; the papers that surfaced are not Teagasc-authored in the
  results I saw. Located but **not fetched**: "Rapid and non-destructive determination of lean fat and
  bone content in beef using dual energy X-ray absorptiometry", DOI via
  `https://pubmed.ncbi.nlm.nih.gov/30145410/`; "Carcass and Primal Composition Predictions Using
  Camera Vision Systems (CVS) and Dual-Energy X-ray Absorptiometry (DXA) Technologies on Mature Cows",
  PMC8158109 (OA). [SNIPPET] the latter: "Left carcass sides (n = 316) were broken down into primal
  cuts, scanned using DXA and then dissected to fat, lean and bone" — again, **cut first, scan
  second**. Teagasc as an institution: **not verified either way.**
- **Mishra, Ferragina, Hegarty, Hamill (2026)**, "Instance segmentation of beef carcass features with
  deep learning", *Applied Food Research* **6**, 102070, DOI `10.1016/j.afres.2026.102070`, Crossref
  licence **CC BY** [VERIFIED bibliographic only; abstract not deposited]. Teagasc authorship is
  likely (Hamill, Ferragina are Teagasc Ashtown) but **not verified from a fetched page**.

---

## "Visible Cow" / volumetric anatomical datasets — explicit negatives

- **The Visible Animal Project is a dog, not a cow.** [VERIFIED] — Böttcher, Maierl, Schiemann,
  Glaser, Weller, Hoehne, Reiser, Liebich (1999), *Veterinary Radiology & Ultrasound*,
  DOI `10.1111/j.1740-8261.1999.tb00887.x`, PMID 10608688. Abstract fetched verbatim via Europe PMC:
  > "The 'Visible Animal Project' (VAP) is comprised of axial anatomic cryosections and corresponding
  > CT and MR images of a mature dog... For the first time a complete high-resolution
  > three-dimensional database of a dog is available... similar to the 'Visible Human Project' (VHP)."
- **No "Visible Cow" or bovine equivalent found** in three distinct WebSearch queries
  (`"Visible Cow" OR "Visible Animal Project" bovine sectional anatomy CT atlas 3D dataset`, plus two
  follow-ups the search tool ran on "Visible Animal" and "Visible Cow" separately). This is a **null
  search, not a proven absence.**
- **`anatomy3d.ovgu.de` does not resolve** — `getaddrinfo ENOTFOUND anatomy3d.ovgu.de` [VERIFIED
  failure]. Either dead or never existed at that host. A WebSearch for it returned nothing matching.
- Bovine sectional-anatomy CT papers do exist, but they are head/limb/sinus scale, not whole-carcass,
  and none is a distributable volume. Located, not fetched: Zebu cattle head sectional anatomy + 3D CT
  (PMC11250968); CT/cross-sectional anatomy of paranasal sinuses in the Holstein cow
  (`10.1111/vru.13166`); 3T MRI and CT of the bovine carpus (PMC9214995). None of these touches cuts.
- **IMAIOS vet-Anatomy** bovine atlas (`https://www.imaios.com/en/vet-anatomy/bovine/bovine-general-anatomy`)
  — located, not fetched. Commercial, subscription, 2D slice-based. Not cut-aware.
- **Virginia Tech Veterinary Anatomy Viewer** `https://virtualanimalproject.vetmed.vt.edu/` — located,
  not fetched. Teaching anatomy, not cuts.

## Cuts scanned as physical objects — the near-miss worth knowing about

**Hadžiomerović, Čaklovica, Dučić, Gjoni Gündemir, Vejzović, Fazlović, Avdić, Čaklovica & Tandir
(2025)**, "Anatomy of meat cuts: integrating 3D scanning and virtual reality in veterinary education
and training", *Frontiers in Veterinary Science*, DOI `10.3389/fvets.2025.1680785`, PMC12590504,
**CC BY**. Full text [VERIFIED] via
`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12590504/fullTextXML`. University of Sarajevo
Veterinary Faculty.

- Method, verbatim: an **EinScan Pro 2X (Shining 3D)** handheld scanner, scanning in a working meat
  plant; "the specimens were positioned as standard commercial meat portions and scanned from multiple
  angles and orientations"; post-processed in EXModel; "all files were recorded as **OBJ** files."
- Twelve models uploaded to Sketchfab as the **"3DMeat Project"** collection under
  `https://sketchfab.com/UNSA-VF`, "each accompanied by descriptive metadata including the name of the
  meat cut, the constituent muscles and the corresponding meat category, along with a diagram of its
  anatomical location."
- VR layer: Open Brush on HTC Vive Pro 2, two stations of six cuts each, info panel above each model.
  Education study with 25 students; 3D-model group scored highest immediately, VR group retained best
  at two weeks.
- **I checked the Sketchfab profile directly** via `https://api.sketchfab.com/v3/search?type=models&user=UNSA-VF&count=24`
  [VERIFIED]. The profile is real and mixes veterinary specimens with meat cuts — meat-cut models
  present in the first page of 24 include **"Ramstek cijeli"**, **"Cijeli But"**, **"Medaljon lažni
  biftek"** (Bosnian cut names). **All 24 models returned by that first API page have
  `isDownloadable: false` and `license: null`** — viewable in the Sketchfab player only, no reuse, no
  licence declared. (I paged once; the profile has more models, and the "3DMeat Project" collection
  itself was not enumerated separately.)
- Against the four questions: **frame** — none; each cut is scanned as a loose object in its own
  arbitrary scanner frame, so two cuts cannot be compared or overlapped. **Geometry published** — yes
  as renderable meshes, no as downloadable data. **Traditions** — one (Bosnian/local), 12 cuts.
  **Open** — CC BY paper, but the models themselves are not.
- This is the clearest demonstration of why the shared frame is the hard part: somebody has already
  done "cuts as real 3D geometry with muscle metadata", and without a common frame it is a photo
  album, not an atlas.

## Parametric / statistical shape models of cattle (not games)

- Live-animal body-measurement work only, not carcass or cut work. Located, **not fetched**:
  "Construction of statistical shape model of real cattle and its application to body measurement",
  IEEE `https://ieeexplore.ieee.org/document/9964568/`; "Automated measurement of livestock body based
  on pose normalisation using statistical shape model",
  `https://www.sciencedirect.com/science/article/abs/pii/S1537511023000211`.
- **No open-source parametric bovine model found** comparable to SMPL/SMAL for this purpose.
  [SNIPPET] the search summary states the results "do not indicate whether these models are available
  as open source". Null search — not a proven absence.
- The one parametric animal mesh that *is* documented in this domain is the Auckland pig/lamb atlas
  above (cubic Hermite), and it is not distributed.

---

## Comparative cutting trials — did anyone ever cut the same carcass two ways?

**Answer: not across national traditions, as far as four searches reach.**

Queries run, all returning nothing on point:
1. `comparative cutting trial same carcasses American versus European cutting style yield "cutting test" beef boning method comparison`
2. `"cutting style" OR "cutting method" comparison yield same carcass "German" OR "Danish" versus "American" primal breakdown study meat science`
3. `"US-style" OR "American style" boning lamb carcass yield comparison "New Zealand" OR "Australian" cutting specification trial same carcasses`
4. `Hanwoo Korean beef cutting yield comparison USDA primal cut "same carcass" different fabrication standard study`
5. `"cutting test" beef carcass "different cutting systems" yield comparison national specifications IMPS versus EUROP primal harmonisation trial`

These are **null searches**, which is weaker evidence than a blocked fetch. It is entirely possible
such a trial exists in a processor's internal report, an MLA/AHDB project report, or pre-1990 grey
literature that is not indexed.

**The nearest published thing, and it is within one tradition:**

- **Beef Carcass Value Optimization** — T.D. Carpenter, J.L. Meisinger, J.D. Tatum, G.C. Smith,
  K.E. Belk, **Colorado State University**, completed 2008. Project summary at
  `https://www.beefresearch.org/resources/product-quality/project-summaries/2006-2010/beef-carcass-value-optimization`
  [VERIFIED, fetched]. Verbatim:
  > "There were a total of three cutting styles for fabricating the brisket, seven styles for
  > fabricating the chuck, eight styles for fabricating the rib and plate, eight styles for
  > fabricating the loin, and 16 styles for fabricating the round."

  generating **"21,504 different carcass styles for which yields were measured"**, valued against
  USDA-reported prices for Nov 2007 and May–Jun 2008.
- This is a genuine combinatorial measurement of *how a different partition of the same animal changes
  what you get* — the empirical cousin of this atlas's overlap percentages. But all 21,504 styles are
  **US styles**; there is no French, Korean or Russian arm. And the summary does not state the carcass
  count or link a full report; whether individual carcasses were physically fabricated multiple ways
  (as opposed to yields being combinatorially recomposed from subprimal data) is **not stated on the
  page** — do not assume physical re-cutting.
- Also relevant, already in this repo's survey: **Swatland (2012)**, "History and Language of
  International Meat Cutting", AMSA 65th Reciprocal Meat Conference,
  `https://meatscience.org/docs/default-source/publications-resources/rmc/2012/26_swatland_r2.pdf`
  [VERIFIED — fetched and text-extracted with pypdf]. His concordance method, verbatim:
  > "if a us cut overlapped with a British cut of the same name, it scored 1, with 0 for a mismatch by
  > location. in table 1, the cut match shows the degree of concordance; rib and brisket are perfectly
  > conserved names, with flank not far behind. there is no concordance for shank..."

  So Swatland's score is **binary name-location agreement**, judged from printed cutting charts — not
  a measured or geometric overlap. That sharpens what this repo adds: Swatland asks "is the US rib the
  same cut as the British rib, yes or no"; this atlas asks "what fraction of one occupies the other".
  Nobody in between.

---

## Fetch failures and blocks encountered (so nobody re-runs them)

| URL / host | Result |
|---|---|
| `tandfonline.com` (article and PDF, direct + curl + Wayback replay) | **403** every route |
| `sciencedirect.com` (all articles) | **403** |
| `robutcher.eu` (PDF mirror of the atech paper) | **ECONNREFUSED 82.165.235.55:443**, WebFetch and curl |
| `pmc.ncbi.nlm.nih.gov` / `pubmed.ncbi.nlm.nih.gov` via WebFetch | cookie-consent wall, no content |
| `europepmc.org` article pages via WebFetch | navigation chrome only |
| `web.archive.org` via WebFetch | "Claude Code is unable to fetch from web.archive.org" |
| `archive.org/wayback/available` API | **429** rate limited (the `cdx` API worked fine) |
| Wayback `…id_/` PDF replay, via curl | serves, but **truncates at exactly 1,048,576 bytes** |
| `api.semanticscholar.org` for the atech OA PDF | 200, but `openAccessPdf.url` just points back at the DOI |
| `api.core.ac.uk/v3/search/works` for the atech DOI | 200, 1 hit, but the only data provider is DOAJ — no repository PDF |
| `sketchfab.com` HTML via WebFetch | empty |
| `anatomy3d.ovgu.de` | **DNS ENOTFOUND** |
| MLA and AMSA PDFs via WebFetch | binary noise |

**What worked, and is worth reusing on the other threads:**

- **Europe PMC REST via curl/python** — `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=…&format=json&resultType=core`
  gives title, authors, affiliations, journal, DOI, PMCID, OA flag and **full abstract** with no
  cookie wall; `…/rest/PMC<id>/fullTextXML` gives the **entire open-access full text**.
- **Crossref REST** — `https://api.crossref.org/works/<doi>` and `?query.bibliographic=…` gives
  author affiliations and, for some publishers (Taylor & Francis, Wiley), the deposited abstract. This
  is how the paywalled T&F lamb paper was read.
- **DOAJ API** — `https://doaj.org/api/v2/articles/<id>` returned the full abstract of an Elsevier
  gold-OA paper that ScienceDirect refused.
- **OpenAlex** — `https://api.openalex.org/works/doi:<doi>` for OA status and mirror locations.
- **pypdf on the file WebFetch already saved** — WebFetch writes the raw PDF to
  `C:\Users\kk\.claude\projects\…\tool-results\webfetch-*.pdf` even when it reports binary noise.
  Extract from that file rather than re-fetching. This rescued both the MLA factsheet and Swatland.

---

## Answers to the brief's four questions, per hit

| Work | Coordinate frame? | Cut geometry published? | Traditions | Open? |
|---|---|---|---|---|
| Ho et al. 2019 pig atlas | Yes — one CT specimen, 84 muscles + 121 bones, cubic Hermite | No (virtual cuts named as future application only) | 0 explicit | No |
| Ritchie & Ho 2025 lamb VR | Yes — one CT lamb atlas | No — outputs volume/weight per cut | 1 (NZ) | No (403) |
| de Medeiros Esper et al. 2024 MFC | Yes — CT template registered to per-carcass point cloud (Bayesian CPD) | **Described** as "a custom 3D model of the cutting surface"; parameters UNPROVEN | 1 (MFC pig scheme) | Gold OA, CC BY-NC-ND, host unreachable |
| Pigs RGB-D dataset 2022 | Camera-rig frame, not animal frame | Depth frames + camera transform JSONs — **published** | n/a | Yes, OA |
| Sarajevo 3DMeat 2025 | **No** — each cut scanned loose | Meshes viewable, `isDownloadable: false`, no licence | 1 (Bosnian), 12 cuts | Paper CC BY; models no |
| Scott X-Ray Primal | Per-carcass bone map; cut = height + angle | No | 1 per customer spec | No |
| MLA OCM / DEXA | Per-carcass scan | No — yields and cutting-line guidance only | 1 (AUS-MEAT) | No, reproduction prohibited |
| SRUC / Navajas / Kongsro CT | Primal cut **before** scanning | No | 1 | No |
| CSU Value Optimization 2008 | n/a (no geometry) | Yields for 21,504 fabrication styles | 1 (US), many styles within it | Summary page only |
| Swatland 2012 | n/a | Binary name-location concordance table | 2 (US vs British/Scottish) | Yes, free PDF |

## What is still unbuilt after all of this

1. Nobody has put **more than one** tradition's cuts into **one** animal frame.
2. Nobody has published the **cut surfaces themselves** as reusable geometry — the closest, the
   RoBUTCHER cutting-surface model, is described but its host is down.
3. Nobody has **measured the overlap** between two traditions' cuts, geometrically or empirically.
   Swatland scored name agreement 1/0; CSU measured yields across US-only style permutations; the
   cross-tradition number this atlas computes has, on this evidence, never been reported.
4. There is **no bovine Visible Human**. The whole-animal volumetric dataset that would let someone
   else redo this from scans does not exist in the open.
