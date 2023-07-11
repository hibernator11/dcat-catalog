# dcat-catalog

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hibernator11/dcat-catalog/HEAD)

Examples of GLAM datasets described using the [Data Catalog Vocabulary](https://www.w3.org/TR/vocab-dcat-3/).


## Collection of datasets

- [British Library - Free dataset downloads](datasets/bl.ttl)
- [Europeana - Downloads](datasets/europeana.ttl)
- [Harvard Art Museums API](datasets/harvard.ttl)
- [Library of Congress - Chronicling America](datasets/lc.ttl)
- [Metropolitan Museum of Art - Collection API](datasets/moma.ttl)
- [National Library of France - Mandragore](datasets/bnf.ttl)
- [National Library of Luxembourg - Historical Newspapers](datasets/bnl.ttl)
- [National Library of Scotland - Moving Image Archive - A Medical History of British India](datasets/data-foundry-nls.ttl)
- [National Library of the Netherlands - Dutch Novels 1800-2000](datasets/kb.ttl)
- [Rijksmuseum - Actors - Thesauri](datasets/rijksmuseum.ttl)
- [South Australian Museum - Minerals Collection](datasets/sam.ttl)
- [Zeri Photo Archive](datasets/zeri.ttl)

  
## Exploring the collection of datasets using Jupyter Notebooks

- [dcat-SPARQL](https://nbviewer.org/github/hibernator11/dcat-catalog/blob/main/notebooks/dcat-SPARQL.ipynb)

## Visualisations

- The organisations used in this work can be retrieved using their Wikidata identifiers in order to create a map as a [visualisation example](https://w.wiki/6$oU).

<img src="images/map-dcat.png" width="80%">

<iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#%23defaultView%3AMap%0APREFIX%20wd%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E%0ASELECT%20%3Fr%20%3FrLabel%20%28SAMPLE%28%3Fimage%29%20as%20%3Fimg%29%20%28SAMPLE%28%3Flocation%29%20as%20%3Fl%29%0AWHERE%20%7B%20%20%20%0A%20%20VALUES%20%3Fr%20%7Bwd%3AQ1670994%20wd%3AQ3783572%20wd%3AQ234110%20wd%3AQ856651%20wd%3AQ188740%20wd%3AQ1526131%20wd%3AQ190804%20wd%3AQ131454%20wd%3AQ193563%20wd%3AQ23687322%20wd%3AQ23308%20wd%3AQ2546445%7D.%0A%20%20%20%20%20%20%20OPTIONAL%20%7B%3Fr%20wdt%3AP625%20%3Flocation.%7D%20%23%20coordinates%0A%20%20%20%20%20%20%20OPTIONAL%20%7B%3Fr%20wdt%3AP159%20%3Fheadquarters%20.%20%3Fheadquarters%20wdt%3AP625%20%3Flocation.%7D%20%23%20headquarters%0A%20%20%20%20%20%20%20OPTIONAL%20%7B%3Fr%20wdt%3AP18%20%3Fimage%7D.%0A%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22%20%7D%0A%7D%20GROUP%20BY%20%3Fr%20%3FrLabel%20%3Fimg" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups" ></iframe>

## References

- Gustavo Candela, Nele Gabriëls, Sally Chambers, Thuy-An Pham, Sarah Ames, Neil Fitzgerald, Katrine Hofmann, Victor Harbo, Abigail Potter, Meghan Ferriter, Eileen Manchester, Alba Irollo, Ellen Van Keer, Mahendra Mahey, Olga Holownia, Milena Dobreva: A Checklist to Publish Collections as Data in GLAM Institutions. CoRR abs/2304.02603 (2023)
- Candela, G. (2023). Towards a semantic approach in GLAM Labs: The case of the Data Foundry at the National Library of Scotland. Journal of Information Science, 0(0). https://doi.org/10.1177/01655515231174386
- Chambers, Sally, Walsh, Melanie, Caswell, Michelle, Harder, Geoff, Okumura, Mercedes, Corrin, Julia, Baeza Ventura, Gabriela, Antonijevic, Smiljana, Knazook, Beth, Narlock, Mikala, Bailey, Jefferson, Neudecker, Clemens, Downie, J. Stephen, Layne-Worthey, Glen, van Strien, Daniel, Irollo, Alba, Whitmire, Amanda, Lee, James, Berry, Dorothy, … Ridge, Mia. (2023). Position Statements -> Collections as Data: State of the field and future directions (Version 1). Zenodo. https://doi.org/10.5281/zenodo.7897735
- Padilla, Thomas, Allen, Laurie, Frost, Hannah, Potvin, Sarah, Russey Roke, Elizabeth, & Varner, Stewart. (2019). Final Report --- Always Already Computational: Collections as Data (Version 1). Zenodo. https://doi.org/10.5281/zenodo.3152935
- Mahey, M., Al-Abdulla, A., Ames, S., Bray, P., Candela, G., Chambers, S., Derven, C., Dobreva-McPherson, M., Gasser, K., Karner, S., Kokegei, K., Laursen, D., Potter, A., Straube, A., Wagner, S-C. and Wilms, L. with forewords by: Al-Emadi, T. A., Broady-Preston, J., Landry, P. and Papaioannou, G. (2019) Open a GLAM Lab. Digital Cultural Heritage Innovation Labs, Book Sprint, Doha, Qatar, 23-27 September 2019.
- Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna M. Wallach, Hal Daumé III, Kate Crawford:
Datasheets for datasets. Commun. ACM 64(12): 86-92 (2021)
