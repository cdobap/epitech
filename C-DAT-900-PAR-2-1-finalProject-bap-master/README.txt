SENTIMENT ANALYSIS FOR FINANCIAL MARKET

---------------------------------------
PROOF OF CONCEPT
---------------------------------------

Le projet a pour objectif
de récupérer les news qui font l’actualité économique
d’utiliser l’intelligence artificielle afin de les classifier
de tester des modèles pour prédire les futures tendances des actifs financiers

---------------------------------------
API: twitter
Web scrapping:  beautiful soup
Manipulation de dataset:  pandas
Machine learning:  sklearn
---------------------------------------

Le dossier leg contient les notebooks utilisés pour tester les datasets et le scrapping

Le dossier csv contient les datasets

Le dossier roadmap contient les éléments de présentation

---------------------------------------

Les notebooks get_* récupèrent les données

Les notebooks transform_* et merge_* créent les datasets

Les notebooks sentiment_ classifient les données

Les notebooks ratio_* tentent de prédire la tendance du lendemain

---------------------------------------
---------------------------------------

POUR LA SUITE

relancer get_tweets pour scrapper régulièrement twitter et fournir le dataset

créer dataset qui inclut les données du matin (nuit aux usa)

ajouter de nouvelles features

tester tensorflow

évaluer les gains et pertes 