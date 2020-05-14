# clustering_sose2020
Repository für Clusteringkurs SoSe 2020
-------------------------------------------------------------------------------------------------------------------------------
Präsentation:
- erst unbalanciert: 643 Bands, 57.650 Songs, alle mit weniger als 60 Songs raus unterschiedlich viele Songs pro Band 

- Metadaten: Bandname, Songname, URL, Songtext, Genre (selber gescraped - Multilabel), Erscheinungsjahr von Songs???

- Text bearbeiten: Chorus, Linetags, Satzzeichen;

- Part-of-Speech Tagging: Substantive und Adjektive 

- PCA, UMAP, TSNE, 3 Graphiken nebeneinander --> nicht viel zu erkennen

--> Bands mit weniger als 100 Songs raus; 25 Songs pro Band, 272 Bands, 6800 Songs

- Folie "Datensatz anpassen":  Songlänge pro Band Fragen: Songlänge anpassen/ abschneiden?

- Songlänge pro Genre

- Genres Verteilung: Genre1 (am häufigsten der Band zugeordnet), Genre2 (am zweithäufigsten zugeordnet) 


- PCA, TSNE, UMAP für Lyrics: keine gute Verteilung für PCA, ein paar Cluster aber nicht nach Gerne (Wonach?! --> Ziel herauszufinden) bei TSNE (perplexity=50); UMAP (metric= "cosine")...

- PCA, TSNE, UMAP für POS: PCA verwirrend/ konnten Ergebnis nicht so gut interpretieren;

- 30 Most Frequent Words: nach Genres --> ist ein Unterschied zu erkennen? evtl Pop/ Rock raus? aber dann verfälscht/ zu viel eingegriffen?

- Wordclouds: diese Genres sind eindeutiger?

nach Genre balancieren? Songlängen anpassen?

- KMeans: PCA mit eigener und Scikit Implementierung, 10 Cluster

- K-Means Lyrics: mit K-Means von scikit learn berechnet; PCA, t-SNE, UMAP --> t-SNE am besten, aber nicht eindeutig

- K-Means POS: PCA, t-SNE, UMAP --> t-SNE am vielversprechendsten
es sieht so aus, als wären es mehr als 10 Cluster

- Anzahl der Cluster: range 1 bis 20 getestet, Ellenbogenmethode, Silhouette sagen 15 ...  Silhouetten-Koeffizient um null, nicht optimal zugeordnete Cluster, aber auch nicht ganz schlecht (also bei -1)

- t-SNE mit k=15: Text und POS, eher schlecht

- MiniBatch: ausprobiert TSNE, bestes Ergebnis mit POS; unterschiedliche cluster teilweise, z.B. oben Mitte; aber auch ähnlich teilweise; kmeans++ besser

- t-SNE mit Scikit-Learn und Genres: hier wieder mit 15 Clustern, eindeutiger

- Features in Cluster: häufigste Features per Cluster

nach Genre balancieren wäre wahrscheinlich sinnvoll, aber das wissen wir ja eigentlich gar nicht?!

-------------------------------------------------------------------------------------------------------------------------------
Aufgabenverteilung:

KMeans:

- Visualisierung für je PCA, t-SNE, Umap (Teresa) für text und POS

- Clusteranzahl erstmal k=10; dann nach Ellenbogen/ Silhouette (Viktoria)

- häufigste Features/ Wörter (Julia)

- Gif über KMeans-Iterationen hinweg (Teresa)

- Attribute von KMeans austesten --> Visualisierungsmöglichkeiten? (Timo)

- kurze Beschreibung in Notebook oben

Zoom-Meeting: Donnerstag 9 Uhr

TODO: häufigste Features, sklearn+Genre mit neuer Clusterzahl, t-SNE mit k=??

tfidf für text und POS abspeichern
