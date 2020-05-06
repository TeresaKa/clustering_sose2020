# clustering_sose2020
Repository für Clusteringkurs SoSe 2020

Timo: Kuchendiagramme, UMAP farblich markieren, Literatur

Teresa: NGramm, Part of Speech Tags,

Julia: Datensatz verkleinern --> Nach einer bestimmten Anzahl von Bands und Liedern. 

Mittwoch, 06.05.2020: Zoom-Meeting um 10 --> Kurze PPP mit Grafiken zusammenstellen. 


Präsentation:
- erst unbalanciert: 643 Bands, 57.650 Songs, alle mit weniger als 60 Songs raus unterschiedlich viele Songs pro Band 

- Metadaten: Bandname, Songname, Genre (selber gescraped - Multilabel), Erscheinungsjahr von Songs???

- Text bearbeiten: Chorus, Linetags, Satzzeichen;

- Part-of-Speech Tagging: Substantive und Adjektive 

- PCA, UMAP, TSNE, 3 Graphiken nebeneinander --> nicht viel zu erkennen

--> Bands mit weniger als 100 Songs raus; 25 Songs pro Band, 272 Bands, 6800 Songs

- Folie "Datensatz anpassen":  Songlänge pro Band Fragen: Songlänge anpassen/ abschneiden?

- Songlänge pro Genre

- Genres Verteilung: Genre1 (am häufigsten der Band zugeordnet), Genre2 (am zweithäufigsten zugeordnet) 


- PCA, TSNE, UMAP für Lyrics: keine gute Verteilung für PCA, ein paar Cluster aber nicht nach Gerne (Wonach?! --> Ziel herauszufinden) bei TSNE (perplexity=50); ...

- PCA, TSNE, UMAP für POS: PCA verwirrend/ konnten Ergebnis nicht so gut interpretieren;

- 50 Most Frequent Words: nach Genres --> ist ein Unterschied zu erkennen?

nach Genre balancieren? Songlängen anpassen?
