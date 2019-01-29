# Classification d'images medical avec Keras et deep learning
utilisation de CNN réseau de neurones conventionnels profonds pour la détection et la prédiction des tumeurs malignes et bénignes à partir des images médicales  

## introduction 
Au cours de la dernière décennie, la capacité des programmes informatiques d'extraire l'information des images s'est considérablement accrue. cette progression est du  aux réseaux neuronaux convolutionnels (CNNs), un type de réseau neuronal spécialisé dans le traitement des image. Depuis 2012, année où AlexNet a remporté le concours de reconnaissance visuelle à grande échelle ImageNet, les CNN ont constamment surpassé les techniques classiques d'apprentissage machine (p. ex. machines à vecteurs support, forêt aléatoire, k-voisins les plus proches). L'essentiel du travail de conception d'un algorithme ML classique consiste à choisir les caractéristiques appropriées. En revanche, un réseau neuronal profond prend des données brutes (éventuellement après quelques prétraitements) et apprend automatiquement les caractéristiques. 
dans la suite de cet article nous allons vous proposer une architecture de CNN efficace pour la classification des images médicales 

le reste de l'article est diviser en trois parties 
* envirenement de travail 
* entrainement et apprentissage de CNN 
* test et validation 
* échantillonage 


## envirenement de travail
pour l'envirenement de travail j'ai utulisé ANACONDA et GOOGLE COLAB.
ANACONDA est  un envirenement intégré de l'apprentissage machine disponible sur Linux, Windows et Mac OS X.
GOOGLE COLAB  est un environnement de notebook Jupyter gratuit qui ne nécessite aucune configuration et qui s'exécute entièrement dans le cloud. [Pour en savoir plus](http://www.ac-grenoble.fr/ugine/m/?p=271)
pour installer ANACONDA voir ce [tutoriel](http://www.ac-grenoble.fr/ugine/m/?p=271)
pour lancer ANACONDA sur linux: 
```
source activate base
```
