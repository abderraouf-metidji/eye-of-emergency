# <u>Eye of Emergency</u>

___

## 1. Text Mining & Natural Language Processing
### **Text Mining**
_Définition_:  
Le Text Mining est un ensemble de méthodes informatiques et dotées d’intelligence artificielle qui consiste à extraire des connaissances et informations à partir d’ensembles volumineux de données textuelles non structurées ou semi-structurées.  
Il s'agit d'un processus qui va transformer de grandes quantités de contenus exprimés en langage naturel en des éléments exploitables et compréhensibles par une machine pour qu'en suite, la machine transforme ces éléments en informations exploitables par l'humain. Le Text Mining découle directement du Data Mining et se concentre sur l'utilisation de données textuelles de manière à mieux comprendre des tendances pour les prédire et les utiliser de manière stratégique.  


_La data pour le Text Mining_:  
Afin de faire du Text Mining, il faut travailler avec plusieurs formats de données.  

**Les données Non Structurées:**  
Les données non structurées correspondent a des data brutes, stockées dans leur état d’origine et qui n’ont pas été classifiées ni formatées en vue d’un traitement.  

**Les données Structurées:**  
Ce sont des data qui sont présentées dans un format que les machines peuvent comprendre, analyser et stocker. Les données sont donc contrôlées par des référentiels et classifiées selon des champs qui permettent de les interpréter et les traiter.  

**Les données Semi-Structurées:**  
Ces data n'ont pas été organisées selon des référentiels spécifiques mais elles présentent tout de même des éléments permettant de les traiter plus facilement que des données brutes non structurées. Elles ne sont pas compréhensibles par les machines mais elles présentent une certaine forme d'organisation qui va permettre de les examiner et de les utiliser.  

<u>Source</u>: https://www.qualtrics.com/fr/gestion-de-l-experience/client/text-mining/ 

### **Natural Language Processing (NLP)**:  
_Définition_:  
Le Natural Langage Processing (NLP) est un domaine du machine learning qui permet, via des algorithmes linguistiques et statistiques, de comprendre le langage naturel humain.

Concrètement, cette discipline est liée à l’intelligence artificielle et a pour objectif d’extraire le sens d’un écrit ou d’une discussion afin qu’il soit compris par une machine comme le comprendrait un cerveau humain.  

_Pourquoi le NLP ?_:  
Une grande majorité des données clients sont des données textuelles non structurées. Une énorme quantité de ces données sont est générée chaque jour et pour un humain, il est impossible de lire et retranscrire toutes ces données à des fins d'analyse. C'est là qu'intervient le NLP. En automatisant la lecture de texte grâce a des algorithmes qui vont identifier des mots et les grammaire utilisés par les clients pour trouver le sens principal d’un texte ou d’une conversation. C'est pour ces raisons que l'on retrouve aujourd'hui beacuoup de domaines d'pplications pour le NLP.  

_Domaines d'application_:  
- **Sentiment Analysis** -> Identifier l'opinion et le ressenti d'un individu.
- **Ciblage Marketing** -> Identifier les acheteurs potentiels et proposer la meilleure offre et/ou message.  
- **Analyse de marché** -> Dresser un portrait complet du marché existant et de la clientèle.  
- **Chatbots** -> répondre correctement aux questions simples des individus.  

<u>Source</u>: https://www.qualtrics.com/fr/gestion-de-l-experience/client/nlp/


### **Points communs**:  
- **Domaines d'application**: Les deux sont utilisés pour extraire des informations à partir de textes.  
- **Techniques partagées**: Les deux utilisent l'analyse de texte, y compris le nettoyage des données textuelles, la tokenisation, le stemming et la lemmatisation. Mais aussi les techniques d'apprentissage automatique telles que les algorithmes de classification, de clustering et de régression.  
- **Outils et Technologies**: Les deux utilisent des bibliothèques et outils similaires comme NLTK, spaCy, Gensim...  

### **Différences**:  
- **Objectifs**: Le Text Mining se concentre sur l'extraction de connaissances et d'information significatives à partir de texte là où le NLP se concentre sur la compréhension et la génération de langage naturel par les machines.  
- **Approches et Méthodologies**: Le TM utilise souvent des techniques statistiques et des méthodes de Data Mining pour analyser les textes et extraire des informations. Le NLP lui, implique des techniques linguistiques et informatiques plus complèxes pour permettre aux machines de comprendre et générer du langage humain.  
- **Complexité et Problèmes Traitables**: Le TM se concentre souvent sur des tâches moins complèxes comme l'extraction d'informations et l'analyse de sentiment alors que le NLP va être utilisé pour la compréhension contextuelle, l'ambiguïté linguistique et la génération de langage naturel cohérent.  

## 2. Les sous-domaines du NLP  
Le traitement automatique du langage naturel (NLP) englobe un large éventail de sous-domaines et de techniques, chacun ayant des objectifs spécifiques et des applications pratiques. Voici une liste des principaux sous-domaines et techniques du NLP:  
- Analyse de Sentiments (Sentiment Analysis)
- Reconnaissance d'Entités Nommées (Named Entity Recognition - NER)
- Étiquetage des Parties du Discours (Part-of-Speech Tagging - POS Tagging)
- Analyse Syntaxique (Parsing)
- Résolution de la Coréférence (Coreference Resolution)
- Extraction d'Information (Information Extraction)
- Traduction Automatique (Machine Translation)
- Résumé Automatique (Text Summarization)
- Question-Réponse (Question Answering)
- Reconnaissance Vocale (Speech Recognition)
- Génération Automatique de Texte (Text Generation)
- Modèles de Langage (Language Modeling)
- Analyse Sémantique (Semantic Analysis)
- Reconnaissance d'Intention (Intent Recognition)
- Classification de Texte (Text Classification)
- Clustering de Texte (Text Clustering)
- Analyse de Cohérence Textuelle (Textual Coherence Analysis)
- Correction Automatique de Texte (Text Correction)  

Pour cette veille nous allons nous concentrer sur seulement cinq de ces sous-domaines. A savoir, _L'Analyse de Sentiment_, _Le NER_, _le POS Tagging_, _Le Parsing_, _La Traduction Automatique_.  

### **<u>Analyse de sentiment</u>**:  
L'analyse de sentiments vise à déterminer l'attitude ou l'émotion exprimée dans un texte. Cette technique peut identifier des sentiments positifs, négatifs ou neutres dans des textes comme des avis de clients, des tweets, ou des articles de presse.  
_Exemple_: Imaginons un système d'analyse de sentiments appliqué aux avis de produits sur un site de commerce.  
- **Avis**: "J'adore ce produit! La qualité est excellente et le service client est exceptionnel."  
- **Résultat**: Sentiment positif (Score étant un chiffre entre 0 et 1).  
### **<u>Named Entity Recognition (NER)</u>**:  
Le NER consiste à identifier et classifier les entités nommées (personnes, organisations, lieux, dates, etc.) mentionnées dans un texte. Cette technique est cruciale pour extraire des informations spécifiques et structurées à partir de documents textuels.  
_Exemple_: Dans un article de presse, un système NER pourrait identifier et classer les entités suivantes: 
- **Texte**: "Apple a annoncé un nouveau produit lors de la conférence à San Francisco le 25 juin 2023."  
- **Résultat**: {Organisation: "Apple", Événement: "conférence", Lieu: "San Francisco", Date: "25 juin 2023"}
### **<u>POS Tagging</u>**:  
Le POS Tagging consiste à attribuer à chaque mot d'un texte son rôle grammatical, comme nom (noun), verbe (verb), adjectif (adjective), etc. Cette technique est fondamentale pour l'analyse syntaxique et la compréhension du texte.  
_Exemple_: Pour une phrase simple comme "Le chat dort sur le tapis," le POS Tagging produirait le résultat suivant: 
- **Phrase**: "Le chat dort sur le tapis" 
- **Résultat**: [("Le", "DET"), ("chat", "NOUN"), ("dort", "VERB"), ("sur", "PREP"), ("le", "DET"), ("tapis", "NOUN")]
### **<u>Analyse Syntaxique (Parsing)</u>**: 
L'analyse syntaxique consiste à déterminer la structure grammaticale d'une phrase. Cela permet de comprendre les relations entre les mots et les phrases. 
_Exemple_: Pour la phrase "Le chat mange une souris", l'analyse syntaxique pourrait générer un arbre syntaxique indiquant que "le chat" est le sujet, "mange" est le verbe et "une souris" est l'objet.
### **<u>Traduction Automatique</u>**: 
La traduction automatique est la tâche de traduire automatiquement du texte d'une langue à une autre. 
_Exemple_: Traduire "Bonjour, comment allez-vous?" de français en anglais donnerait "Hello, how are you?".  

## 3. Exemples d'application du NLP  
Les domaines d'application du NLP sont très larges, en voici une liste non exhaustive:  
- Assistants Virtuels & Chatbots -> comprendre et répondre aux demandes d'un utilisateur.
- Traduction Automatique -> traduire un texte d'une langue à une autre.
- Analyse de Sentiments pour les réseaux sociaux -> identifier des tendances positives ou négatives concernant un produit après analyse d'un large nombre de publications.
- Systèmes de recommandations -> analyse les commentaires, like et critiques afin de faire des suggestions. 
- Détection de Fraude -> analyse les communications et transactions suspectes.
- Reconnaissance vocale et Transcription -> permet de convertir la parole en texte.
- Résumé Automatique de Documents -> parcourt et condense de longs documents.  

## 4. Les Stop-Words
_Définition_:  
Les stop words sont les tokens très fréquents dans une langue donnée. Ces tokens étant présents dans la plupart des textes, ils ont un pouvoir discriminant assez faible. On a donc tendance à les supprimer pour réduire encore plus la taille du vocabulaire.  

<u>Source</u>: https://blog.octo.com/nettoyage-du-texte-en-nlp-moins-de-vocabulaire-moins-de-bruit  

Il est important de supprimer les Stop-Words pour plusieurs raisons.  
Tout d'abord afin de réduire la taille des données. En les supprimant la quantité de données à traiter est réduite ce qui accélère le traitement et diminue l'utilisation des ressources.  
En suite, supprimer les Stop-Words améliore la précision du modèle. En effet, les Stop-Words peuvent introduire du bruit dans les analyses textuelles, ce qui peut réduire la précision des modèles NLP. En les supprimant, on se concentre sur les mots porteurs de sens et pertinents, ce qui permet de mieux capturer les relations et les significations dans les textes.  
Pour finir cela permet d'améliorer la pertinence des termes utilisés pour ces analyses.  

_Exemple_:  
Considérons un texte simple:

"Le chat dort sur le tapis et il est très confortable."

<u>Texte Avant Suppression des Stop-Words</u>:
"Le chat dort sur le tapis et il est très confortable."

<u>Texte Après Suppression des Stop-Words</u>:
"chat dort tapis confortable"

Dans cet exemple, les mots "Le", "sur", "et", "il", "est", "très" ont été supprimés car ce sont des stop-words. Les mots restants, "chat", "dort", "tapis", et "confortable", portent une signification contextuelle importante et sont essentiels pour les tâches de NLP comme l'analyse de sentiments ou la classification de texte.

#### 5. En plus de la ponctuation, on retrouve souvent des caractères spéciaux au sein de données textuelles. Comment sont traités ces deux types de caractères ?

Généralement en NLP on va etre amené à supprimer les ponctuations et les caractères spéciaux. S'agissant de caractères sans aucune valeur ajouter ils viennent polluer notre donnée et rendent les taches de NLP plus compliquées.

#### 6. Qu’est ce qu’un token ? un N-gram ? Quel processus permet-il de les obtenir ?

<u>Token</u>

La tokenization est une tache primordiale lors du NLP. Il s'agit d'une façon de séparer les mots d'une phrase en leur attribuant un *token*. Ce token peut prendre plusieurs formes différentes en fonction de la méthode choisie mais globalement le but étant que chaque mot possède un id permettant aux différents modèle d'avoir un apprentissage plus optimisé. Les machines ne comprenant pas les mots comme les humains il est primordial d'effectuer cette étape lors du NLP.

Différents types de tokenization:

* Word tokenization; c'est une méthode qui casse un texte en mots
* Character tokenization; ici nous allons segmenté le texte en caractères individuels
* Subword tokenization; cette méthode combine les deux méthodes précédentes et va donc casser un texte en plusieurs chaines de caractères qui sont plus grandes que 1 mais qui ne font pas la taille d'un mot (ex. chatbot devient 'chat' & 'bot')

<u>N-gram</u>

Un N-gram constitue en NLP des séquences de n mots extrait d'un texte pour le processing du langage et son analyse. Cet N-gram peut etre aussi court q'un mot (unigram) et aussi long que plusieurs mots (bigram, trigram, etc.). Ces n-gram permettent de capturer le contexte entre plusieurs mots dans un texte.

Le N-gram est important en NLP car il permet de nuancer la compréhension du texte à l'aide du contexte permettant un processing de langage plus précis. 

Quelques bénéfices du N-gram:

* Modeling de langage; les N-gram aide à la capture de la probabilité de distribution de mots dans un langage donné
* Récupération d'information; ils peuvent aussi etre utilisé afin d'indexer et parcourir un texte dans le but d'obtenir des résultats plus pertinents
* Prédiction de texte; en analysant les N-gram les plus fréquent on pourra prédire le prochain mot dans une séquence de texte

Ces deux taches sont généralement effectuées lors du traitement de la donnée, avant d'utiliser un algorithme. 

On va dans un premier temps utiliser une librairie comme NLTK ou encore spaCy afin de nettoyer notre texte. Par la suite on va utiliser un script qui nous permet de générer les différents tokens.

#### 7. Expliquez les deux notions de Stemming et de Lemmatization. Quelle est la différence entre les deux ? Dans quels cas faut-il utiliser l’un plutôt que l’autre ?

<u>Stemming</u>

Le *Stemming* est une méthode de normalization de texte qui permet de convertir de la donnée brute en format lisible.

Ici on va supprimer les suffixes de nos mots en comparant nos tokens avec un lexique de de suffixes communs. L'algorithme le plus utilisé pour le stemming et *l'algorithme de Stemming de Porter* (Snowball Stemmer).

<u>Lemmatization</u>

La *Lemmatization* a le meme but que le stemming mais avec un fonctionnement différent. 

Contrairement au Stemming ici on va supprimer les affixes et non les suffixes. Le but étant de réduire les variations de mots en la forme principale utilisé dans le dictionnaire.

<u>Stemming vs Lemmatization</u>

Là ou le stemming va simplement supprimer les affixes en se basant sur un lexique prédéfini la Lemmatization va nettoyer chaque mot dans le but de normaliser la forme de chaque mot. 

La Lemmatization demande plus de temps que le Stemming en matière de traitement. Généralement nous allons utiliser le Stemming lors d'une analyse de sentiment par exemple alors que la Lemmatization elle va etre utilisée lors de la construction d'un chatbot par exemple. 

#### 8. En représentant les mots sous forme de vecteurs numériques, vous permettez à un algorithme de Machine Learning de traiter les données textuelles et d'en extraire des informations utiles. Étudiez les deux méthodes Bag of Words et TF-IDF.

<u>Bag of words</u>

Le modèle *Bag of words* et une méthode d'extraction qui permet de récupérer des features à partir d'un texte dans le but de l'utiliser lors d'un modeling en machine learning. 

Il s'agit d'une approche relativement simple et flexible qui peut etre utilisée de plusieurs manières différentes. 

Cette méthode comprends 2 choses:

* un vocabulaire de mots communs
* une mesure de présence de ces mots

Etapes : 

* Récupérer la donnée
* Définir le vocabulaire
* Création de vecteurs

Si le vocabulaire de comprend pas beaucoup de mots on peut utiliser des vecteurs avec une longueur fixe. Cependant, si la taille du vocabulaire augmente la taille des vecteurs augmentera également.

Le but étant donc d'optimiser notre vocabulaire afin de ne pas avoir une liste de mot trop grande qui compliquerai nos vecteurs. Pour ce faire nous pouvons suivre les étapes de traitement de la donnée tels que : 

* ignorer les majuscules
* ignorer la ponctuation
* ignorer les mots fréquents sans conséquence pour la compréhension du texte 
* correction des erreurs d'orthographe
* réduire les mots à leur racine (ex. playing -> play)

Sinon, une autre méthode consiste en la création d'un vocabulaire de mots groupés.

Une fois le vocabulaire défini nous allons attributer un score à nos mots ce qui nous permet d'avoir une idée de la présence des mots dans le texte ainsi que leur récurrence.

En termes de limitation il y en a quelques unes tels que: 

* Vocabulaire; comme nous l'avons vu la notion de vocabulaire peut etre limité s'il n'est pas traité correctement
* Parcimonie;  une représentation parcimonieuse est plus difficile à modéliser
* Sens; lorsqu'on ignore le contexte et l'ordre des mots le texte peut avoir moins de sens

<u>TF-IDF</u>

Il s'agit d'une méthode statistique en NLP qui mesure l'importance d'un terme dans un texte.

Les mots d'un texte sont donc transformés en nombre basé sur leur importance dans le but de vectoriser ce texte. 

Pour ce faire on va calculer *TF* qui correspond au *Term Frequency*. Ce calcul s'effectue en divisant le nombre de fois qu'un mot apparait dans le texte par le nombre total de mots dans le texte.

<img>![alt text](images/image.png)</img>

L'*IDF* quant à lui correspond à *l'inverse document frequency*. L'IDF représente la proportion de documents qui contienne un mot. Ici les mots qui sont le moins présent (par exemple des mots techniques) vont avoir une plus grande importance que les mots communs. 

<img>![alt text](images/image-1.png)</img>

Ensuite on va calculer le *TF-IDF* en multipliant ces deux valeurs.

<img>![alt text](images/image-2.png)</img>

Plus simplement, l'importance d'un mot est plus importante lors qu'il est très présent dans un texte et moins dans les autres. Cela nous permet d'avoir un niveau d'importance global pour un mot dans plusieurs textes. 