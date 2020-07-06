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

- neuer Datensatz: Jahreszahlen gescraped, deutlich verkleinert, POS mit Adjektiven, Verben und Substantiven; nur noch 40.000 Songs

- SVM: Confusionmatrix mit POS; Pop sehr schlecht zugeordnet, Pop und Reggae anscheinend sehr ähnlich, Funk sehr gut zuzuordnen, HipHop sehr schlecht, obwohl es beim Clustering besser ist

- KMeans mit kleineren Teildatensätzen, z.B. alle Genres außer Pop und Rock: HipHop gut abgrenzbar

-------------------------------------------------------------------------------------------------------------------------------
Aufgabenverteilung:

- Grafik, Tokenanzahl pro Song, dann Verteilung visualisieren.(Teresa)
- längere Texte, dann in SVM (Timo)
- hierarchisches Clustering (Timo+Viktoria)
- häufiste Wörter pro Genre, nur Country + HipHop nehmen --> Hierarchisches CLustering (Julia)
- Untergenre z.B. von Pop ausgeben lassen (Julia)
- Alternativ: Word-Embeddings 

--------------------------------------------------------------------------------------------------------------------------------
Präsentation Donnerstag, 4.6.2020

25: neuer Datensatz -> Bandnamen geändert und angepasst, Jahreszahlen für jeden Song gescraped -> neues Ergebnis
    Spotify neue Genre ausgeben lassen -> wird feiner, detaillierter unterteilt, vor allem Pop und Rock
    
26: Kreisdiagramme: Rock alternativ, Album-Rock / Pop Dance-pop usw -> neu anpassen -> größten Subgenre nehmen?

27: SVM: Datensatz: überdurchschnittlich lange Texte -> leider keine Diagonale 
    Klassik werden noch viele andere Songs zugeteilt, aus Country und Latin 
    
28 u. 29: ähneln sich HipHop fällt raus und die anderen ähneln sich 

30: pop und rock weg 

31-33: länger als Durschnitt 

34: type-token: überdurchschnittliche Texte

35: HC -> Eminem und Abba -> viele Cluster 

36: HC ausprobiert und Grafiken einfach mal zeigen :D

37: - " - 

25-26: Julia

27-29: Timo

30-34: Teresa

35-38: Julia 

38-42  : Viktoria 

43-44: Julia -> Code HC - Vergleich und Überlegungen 

--------------------------------------------------------------------------------------------------------------------------------
Präsentation für Donnerstag 18.6.2020:

- Datensatz verändert: alle Songs einer Band pro Jahrzehnt zusammgenfasst -> 1000-2000 tokens 

- Folie 45: Verteilung der Bands in Dekaden/ Länge der "Songtexte"

- Folie 46: SVM: Genre1 als Label und Feautures: decades und text hat am besten funktioniert ... verschiedene Feautures, f1-scores bei den 3 Genres HipHop, Jazz und Country am besten -> report 

- Folie 47: 3 Genre + Electronic -> HC 2000 ---> 5 Cluster 
--------------------------------------------------------------------------------------------------------------------------------

Teresa: GMM

Timo: DBSCAN

Julia: 4 Genre aus allen Dekaden und mit allen Genren -> HC & GMM, BIC & AIC

Viktoria: HC -> Bands, die Beziehungen haben ... Vanilla in Electronic .. evtl Beziehungen zwischen den Künstlern, evtl Beats 

Wörter von 2000-2010 anschauen, Verhältnis types und tokens für jede Dekade -> für die Präsentation 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

- HC nach genre1 & decdades (Viktoria) 

- evtl. ein weiteres Verfahren 

- topic modelling / LDA -> Mallet & Gensim https://radimrehurek.com/gensim/models/wrappers/ldamallet.html (Mallet: Julia & Viktoria) ( Gensim: Teresa & Timo)

- gif nach Dekaden -> Komplexität der Texte (Teresa) 

- K-Means mit neuem Datensatz/ 4 Genre (Julia) & t-SNE mit den 4 Genre (Julia)

- UMAP 

- autoencoder (Timo) 

- Ordner aufräumen/ Notebooks kommentieren 


----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Präsentation:

- GMM, HC und evtl topic modelling gut, da ....

- die Verfahren, die nicht so gut waren nur kurz
