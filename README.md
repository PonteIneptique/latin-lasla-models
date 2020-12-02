# Pie Latin LASLA Models

[![DOI](https://zenodo.org/badge/244858653.svg)](https://zenodo.org/badge/latestdoi/244858653)

Repository for LASLA Latin models: the models were fine-tuned by Thibault Clérice, data are based on LASLA data but some adaptation might be found. 

## Download models

[Check latest release, under assets](https://github.com/PonteIneptique/latin-lasla-models/releases/latest)

## Information about the model

*Note:* the model is currently being fine-tuned in the context of my PhD. I'll fill this part when it will be done.

The training set is roughly **1.5M tokens**, dev test roughly 10k and test 169822. This is not counting punctuation, as LASLA data are lacking punctuation.

- Enclitics are kept in a single token
	- Enclitic lemma are separated as such `token[Caesarque]` == `lemma[Caesar界que]` 
	- Morphology is the morphology of the first token
- Only numbers 1, 2 and 3 are known. Roman numbers are unknown.
- All punctuation signs are unknown, including the one used in abbr. `token[C]` == `lemma[Gaius]`
- Lemma and tokens now accept lower and uppercasing. Noise was introduced in the dataset for better results.

### Model LASLA+ (model-plus.tar)

The model LASLA+ is trained on additionnal data, creating some noise in the original dataset and resulting in apparently worse results on classical data (approxim. -0.3%). It's results are 
detailed in [LASLA-plus.md](LASLA-plus.md).

## Scores

### Table of Content

- [lemma](#lemma)
- [pos](#pos)
- [Gend](#Gend)
- [Numb](#Numb)
- [Case](#Case)
- [Deg](#Deg)
- [Mood_Tense_Voice](#Mood_Tense_Voice)
- [Person](#Person)
- [Entity](#Entity)
- [Dis](#Dis)


### lemma

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9741   | 0.8372    | 0.8327 | 169822  |
| known-tokens     | 0.9786   | 0.9077    | 0.907  | 161674  |
| unknown-tokens   | 0.8845   | 0.7462    | 0.7422 | 8148    |
| ambiguous-tokens | 0.9292   | 0.7067    | 0.7121 | 41561   |
| unknown-targets  | 0.6004   | 0.4306    | 0.4297 | 1131    |


- *[More details](details/lemma.md)*
- *[Back to TOC](#table-of-content)*

### pos

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9649   | 0.8747    | 0.8626 | 169822  |
| known-tokens     | 0.967    | 0.8798    | 0.8672 | 161674  |
| unknown-tokens   | 0.9245   | 0.6683    | 0.6129 | 8148    |
| ambiguous-tokens | 0.9087   | 0.8215    | 0.7913 | 52129   |


- *[More details](details/pos.md)*
- *[Back to TOC](#table-of-content)*

### Gend

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9628   | 0.9088    | 0.9161 | 169822  |
| known-tokens     | 0.9652   | 0.9124    | 0.9211 | 161674  |
| unknown-tokens   | 0.9149   | 0.8547    | 0.8433 | 8148    |
| ambiguous-tokens | 0.86     | 0.8536    | 0.8694 | 34690   |


- *[More details](details/Gend.md)*
- *[Back to TOC](#table-of-content)*

### Numb

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9702   | 0.9679    | 0.9685 | 169822  |
| known-tokens     | 0.9718   | 0.9695    | 0.9696 | 161674  |
| unknown-tokens   | 0.9385   | 0.9108    | 0.9217 | 8148    |
| ambiguous-tokens | 0.8998   | 0.8952    | 0.8946 | 38122   |


- *[More details](details/Numb.md)*
- *[Back to TOC](#table-of-content)*

### Case

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9234   | 0.8882    | 0.8244 | 169822  |
| known-tokens     | 0.9259   | 0.8933    | 0.8314 | 161674  |
| unknown-tokens   | 0.8737   | 0.6745    | 0.692  | 8148    |
| ambiguous-tokens | 0.8319   | 0.8278    | 0.7788 | 63352   |


- *[More details](details/Case.md)*
- *[Back to TOC](#table-of-content)*

### Deg

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9807   | 0.9681    | 0.9721 | 169822  |
| known-tokens     | 0.9828   | 0.9701    | 0.9762 | 161674  |
| unknown-tokens   | 0.9396   | 0.928     | 0.9121 | 8148    |
| ambiguous-tokens | 0.9155   | 0.9051    | 0.9277 | 27870   |


- *[More details](details/Deg.md)*
- *[Back to TOC](#table-of-content)*

### Mood_Tense_Voice

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9835   | 0.8304    | 0.738  | 169822  |
| known-tokens     | 0.9873   | 0.8475    | 0.7589 | 161674  |
| unknown-tokens   | 0.908    | 0.7013    | 0.6715 | 8148    |
| ambiguous-tokens | 0.9258   | 0.7358    | 0.7026 | 16963   |


- *[More details](details/Mood_Tense_Voice.md)*
- *[Back to TOC](#table-of-content)*

### Person

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9971   | 0.9901    | 0.9748 | 169822  |
| known-tokens     | 0.9979   | 0.9918    | 0.9802 | 161674  |
| unknown-tokens   | 0.9815   | 0.9761    | 0.9447 | 8148    |
| ambiguous-tokens | 0.9776   | 0.9517    | 0.9038 | 10040   |


- *[More details](details/Person.md)*
- *[Back to TOC](#table-of-content)*

### Entity

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.995    | 0.9504    | 0.7087 | 169822  |
| known-tokens     | 0.9967   | 0.966     | 0.7296 | 161674  |
| unknown-tokens   | 0.9596   | 0.6141    | 0.6009 | 8148    |
| ambiguous-tokens | 0.8891   | 0.9142    | 0.6881 | 2578    |


- *[More details](details/Entity.md)*
- *[Back to TOC](#table-of-content)*

### Dis

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9725   | 0.8685    | 0.9254 | 169822  |
| known-tokens     | 0.9739   | 0.8699    | 0.9285 | 161674  |
| unknown-tokens   | 0.9451   | 0.6468    | 0.5544 | 8148    |
| ambiguous-tokens | 0.9131   | 0.85      | 0.9119 | 41821   |


- *[More details](details/Dis.md)*
- *[Back to TOC](#table-of-content)*



### Credits

*   D. Longrée, C. Philippart de Foy & G. Purnelle. « Structures phrastiques et analyse automatique des données morphosyntaxiques : le projet LatSynt », in S. Bolasco, I. Chiari & L. Giuliano (eds), Statistical Analysis of Textual Data, Proceedings of 10th International Conference Journées d'Analyse statistique des Données Textuelles, 9-11 June 2010, Sapienza University of Rome, Rome, LED, pp. 433-442.
*   D. Longrée & C. Poudat, « New Ways of Lemmatizing and Tagging Classical and post-Classical Latin: the LATLEM project of the LASLA », in P. Anreiter & M. Kienpointner (éd.), Proceedings of the 15th International Colloquium on Latin Linguistics, (Innsbrucker Beiträge zur Sprachwissenschaft), Innsbruck, 2010, pp. 683-694.
*   D. Longrée & C. Philippart de Foy & G. Purnelle, « Subordinate clause boundaries and word order in Latin: the contribution of the L.A.S.L.A. syntactic parser project LatSynt », in P. Anreiter & M. Kienpointner, éd.), Proceedings of the 15th International Colloquium on Latin Linguistics, (Innsbrucker Beiträge zur Sprachwissenschaft), Innsbruck, 2010, pp. 673-681.
*   D. Longrée & Poudat C., « Variations langagières et annotation morphosyntaxique du latin classique », TAL, 50 – n° 2/2009, Special issue on "Natural Language Processing and Ancient Languages", pp. 129-148.
*   E. Manjavacas & ﻿Á. Kádár & M. Kestemont, « Improving Lemmatization of Non-Standard Languages with Joint Learning », Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), Special issue on "Natural Language Processing and Ancient Languages", 2019, pp. 493--1503.
*   Enrique Manjavacas & Mike Kestemont. (2019, January 17). emanjavacas/pie v0.1.3 (Version v0.1.3). Zenodo. http://doi.org/10.5281/zenodo.2542537 _Check the latest version here :_[Zenodo DOI](https://doi.org/10.5281/zenodo.1637877)
*   Thibault Clérice. (2020, April 28). PonteIneptique/latin-lasla-models: 0.0.0 (Version 0.0.0). Zenodo. http://doi.org/10.5281/zenodo.3773328

The web application and its maintenance is done by Thibault Clérice ( @ponteineptique ). To learn how to cite this repository, go check [our releases](https://github.com/PonteIneptique/latin-lasla-models/releases).

## Information about the model

[![LASLA Logo](statics/LogoLASLA2019.png)](http://web.philo.ulg.ac.be/lasla/textes-latins-traites/)

The model is based on the LASLA data.
