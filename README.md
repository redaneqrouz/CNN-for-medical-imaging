# Classification d'images medical avec Keras et deep learning

utilisation de CNN réseau de neurones conventionnels profonds pour la détection et la prédiction des tumeurs malignes et bénignes à partir des images médicales  
Application sur "INVASIVE DUCTAL CARCINOMA (IDC)"

## Introduction 
Au cours de la dernière décennie, la capacité des programmes informatiques d'extraire l'information des images s'est considérablement accrue. cette progression est du  aux réseaux neuronaux convolutionnels (CNNs), un type de réseau neuronal spécialisé dans le traitement des image. Depuis 2012, année où AlexNet a remporté le concours de reconnaissance visuelle à grande échelle ImageNet, les CNN ont constamment surpassé les techniques classiques d'apprentissage machine (p. ex. machines à vecteurs support, forêt aléatoire, k-voisins les plus proches). L'essentiel du travail de conception d'un algorithme ML classique consiste à choisir les caractéristiques appropriées. En revanche, un réseau neuronal profond prend des données brutes (éventuellement après quelques prétraitements) et apprend automatiquement les caractéristiques. 
dans la suite de cet article nous allons vous proposer une architecture de CNN efficace pour la classification des images médicales 

le reste de l'article est diviser en trois parties 
* Envirenement de travail 
* Entrainement et apprentissage de CNN 
* Test et validation 
* Echantillonage 


## Envirenement de travail
pour l'envirenement de travail j'ai utulisé ANACONDA et GOOGLE COLAB.
ANACONDA est  un envirenement intégré de l'apprentissage machine disponible sur Linux, Windows et Mac OS X.
GOOGLE COLAB  est un environnement de notebook Jupyter gratuit qui ne nécessite aucune configuration et qui s'exécute entièrement dans le cloud [Pour en savoir plus](http://www.ac-grenoble.fr/ugine/m/?p=271).
pour installer ANACONDA voir ce [tutoriel](http://www.ac-grenoble.fr/ugine/m/?p=271)

pour lancer ANACONDA sur linux: 
```
source activate base
```
maintenant faut installer tous les dépendences, librairies et framework qu'on va utiliser 
installer keras sous anaconda envirenement 

```
pip install keras
```
keras utilise TenserFlow en background qui est déja installer sous anaconda 

installation de openCV 
```
conda install -c conda-forge opencv
```

installation de la librairies imutils

```
pip install imutils
```

## Entrainement et apprentissage de CNN 
### Datasets et pre-traitement 
pour l'apprentissage d'un réseaux de neurones il faut une base de données massive des images, les images médicales utilisés dans ce travail peuvent avoir des dimensions dépassent  80k*80k pour utiliser des telles images comme entrée d'un réseaux de neurones faut avoir des super machine avec des processeurs graphique comme Nvidia Titan X 
d'ou la nécissité d'utiliser de découper ces images en imagettes de taille 28*28,32*32,64*64

le CNN qu'on va construire prend en entrée un patch de taille 28*28 
pour découper les grandes images en patchs: 
```
python split_oneTomany.py DOSSIER_SOURCE DOSSIER_DESTINATION
```
### CNN
L'architecture De CNN se compose de deux ensembles de couches convolutionnelles, d'activation et de mise en groupe(pooling), suivis d'une couche entièrement connectée, d'une autre entièrement connectée et enfin d'un classificateur softmax.

<figure>
    <img src="images/architecture.png" align="center"/>
</figure>
					figure 1: architecture CNN lenet
		
nous allons implémenter cette architecture avec keras et TenserFlow

cette architecture est Conçu à l'origine pour la classification des chiffres manuscrits, nous pouvons facilement l'étendre à d'autres types d'images également.
l'archietecture de CNN qu'on va utiliser est dans lenet.py 
*code exlication 

Les premieres lignes  gèrent l'importation de nos paquets Python requis:
La classe Conv2D réalise l'operation de convolution. 
```
class LeNet:
	@staticmethod
	def build(width, height, depth, classes):
```
la classe Lenet contient la méthode static de construction, a chaque fois j'appelle la classe il sera appelé automatiquement.
la méthode build a 4 paramétres
* width : La largeur de nos images d'entrée
* height : La hauteur des images d'entrée
* depth : Le nombre de canaux dans nos images d'entrée 
* classes : Le nombre total de classes que nous voulons reconnaître (dans notre cas, deux: malign, benign)
```
# les 3 trois premiers couches CONV => RELU => POOL
model.add(Conv2D(20, (5, 5), padding="same",
	input_shape=inputShape))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# les 3 trois douxieme couches CONV => RELU => POOL
model.add(Conv2D(50, (5, 5), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# utilisation de fontion d'activation softmax 
model.add(Flatten())
model.add(Dense(500))
model.add(Activation("relu"))
model.add(Dense(classes))
model.add(Activation("softmax"))
return model
```

## Entrainement et apprentissage de CNN

pour l'entrainement on va faire appel au model.py 
au top de fichier on importe les paquets requis qui nous permettent:
* Charger les imagesà partir de mémoire
* Pré-traitement des images
* Instantier le réseau neuronal convolutif
* entrainer le model

Par la suite, nous procéderons à une certaine augmentation des données, ce qui nous permettra de générer des données de  "supplémentaires" en transformant aléatoirement les images d'entrée par rotation, zomm etc..

```
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")
```

pour lancer le script de l'apprentissage 
```
python model --DOSSIER_IMAGES
```

le resultat d'éxecution est donnée dans la figure suivante
<figure>
    <img src="images/training.png" align="center"/>
</figure>
figure 2 : plot de traning de model

les ANN généralement ont besoin d'un processeur graphique, notamment pour les architectures profondes 
l'apprentissage a fait un temps d'exécution de 2H09 sur mon PC de configuration :
- 4 processeurs en CPU GenuineIntel
- Intel(R) Core(TM) i5-5300U CPU @ 2.30GHz

A l'aide de matplotlib, nous construisons la courbe d'avancement d'entrainement, validation 
<figure>
    <img src="images/plot2.png" align="center"/>
</figure>
figure 3 : plot de perte et de précision de l'entraînement sur malign/benign

## Test et validation

pour tester notre model sur une imagette de taille 28*28 pour vérifeir s'il classifie bien les images 
lancer le code suivant sur une imagette n'appartient pas a l'ensemble des imagettes utilisé lors de l'apprentissage
```
python test_model.py --model YOUR_MODEL --image PATH_IMAGE
```
sinon vous trouvez un modele pres compilé parmi les fichier 'model'

<figure>
        <img src="images/pos.png" align="left" width="200px height="200px" "/>
</figure>

<figure>
        <img src="images/output.png" align="rignt" width="200px height="200px"/>
</figure>
									      
figure 4 : resultat de réseaux sur une imagette 28*28 pixels

## Echantillonage
dans cette partie je vais vous montrer la méthode d'échantillonnage régulier décrit dans l'article [HASHI](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0196828)
la méthode consiste a parcourir l'image WSI patch par patch par un itérateur ou window-sliding 
pour lancer le script 
```
python prob_map.py MODEL IMAGE
```
le script prend en entrée deux paramétre le model compilé de réseaux et l'image médical a classifier 
voici les résultats

###les taches en jaunes signifié les regions invasive par les tumeurs 
<figure>
        <img src="images/img-neg.png" align="left" width="400px height="400px""/>
</figure>

<figure>
        <img src="images/output-img-neg.png" align="rignt" width="400px height="400px" "/>
</figure>
figure 5: image negative et le résultat de model


<figure>
        <img src="images/img2.png" align="left" width="400px height="400px""/>
</figure>

<figure>
        <img src="images/output-img2.png" align="rignt" width="400px height="400px""/>
</figure>

figure 6: image positive et le résultat de model


<figure>
        <img src="images/img_n2.png" align="left" width="400px height="400px""/>
</figure>

<figure>
        <img src="images/img_n2_out.png" align="rignt" width="400px height="400px""/>
</figure>

figure 7: image negative et le résultat de model
