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

## Scores

### Model LASLA

<!-- Start Scores LASLA -->


More details:
- [lemma](reports/lasla-plus.md#lemma)
- [pos](reports/lasla-plus.md#pos)
- [Gend](reports/lasla-plus.md#Gend)
- [Numb](reports/lasla-plus.md#Numb)
- [Case](reports/lasla-plus.md#Case)
- [Deg](reports/lasla-plus.md#Deg)
- [Mood_Tense_Voice](reports/lasla-plus.md#Mood_Tense_Voice)
- [Person](reports/lasla-plus.md#Person)
- [Dis](reports/lasla-plus.md#Dis)




#### lemma

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9734   | 0.8216    | 0.8196 | 169822  |
| known-tokens     | 0.9785   | 0.907     | 0.907  | 161674  |
| unknown-tokens   | 0.8716   | 0.7172    | 0.7153 | 8148    |
| ambiguous-tokens | 0.9292   | 0.7114    | 0.7171 | 41561   |
| unknown-targets  | 0.4775   | 0.3136    | 0.3115 | 1131    |


#### pos

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9651   | 0.8794    | 0.8669 | 169822  |
| known-tokens     | 0.9672   | 0.8808    | 0.8703 | 161674  |
| unknown-tokens   | 0.9232   | 0.6979    | 0.6511 | 8148    |
| ambiguous-tokens | 0.91     | 0.8234    | 0.784  | 52129   |


#### Gend

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.965    | 0.9166    | 0.9203 | 169822  |
| known-tokens     | 0.9673   | 0.9198    | 0.9248 | 161674  |
| unknown-tokens   | 0.9201   | 0.8673    | 0.8543 | 8148    |
| ambiguous-tokens | 0.868    | 0.8652    | 0.8747 | 34690   |


#### Numb

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9719   | 0.9705    | 0.9697 | 169822  |
| known-tokens     | 0.9731   | 0.9716    | 0.9705 | 161674  |
| unknown-tokens   | 0.9482   | 0.9224    | 0.9358 | 8148    |
| ambiguous-tokens | 0.9042   | 0.9013    | 0.8979 | 38122   |


#### Case

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9219   | 0.8811    | 0.8177 | 169822  |
| known-tokens     | 0.9244   | 0.8865    | 0.8237 | 161674  |
| unknown-tokens   | 0.8719   | 0.6896    | 0.6738 | 8148    |
| ambiguous-tokens | 0.8296   | 0.8196    | 0.7667 | 63352   |


#### Deg

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9813   | 0.9694    | 0.971  | 169822  |
| known-tokens     | 0.9832   | 0.9711    | 0.9746 | 161674  |
| unknown-tokens   | 0.9434   | 0.9345    | 0.9149 | 8148    |
| ambiguous-tokens | 0.9186   | 0.906     | 0.9258 | 27870   |


#### Mood_Tense_Voice

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9831   | 0.7845    | 0.7355 | 169822  |
| known-tokens     | 0.9868   | 0.8039    | 0.7632 | 161674  |
| unknown-tokens   | 0.91     | 0.6172    | 0.5863 | 8148    |
| ambiguous-tokens | 0.924    | 0.6879    | 0.675  | 16963   |


#### Person

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9971   | 0.9875    | 0.9772 | 169822  |
| known-tokens     | 0.9978   | 0.989     | 0.9814 | 161674  |
| unknown-tokens   | 0.9834   | 0.9762    | 0.9536 | 8148    |
| ambiguous-tokens | 0.9768   | 0.9391    | 0.9068 | 10040   |


#### Dis

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9727   | 0.879     | 0.8797 | 169822  |
| known-tokens     | 0.9738   | 0.8803    | 0.8823 | 161674  |
| unknown-tokens   | 0.9519   | 0.6651    | 0.5761 | 8148    |
| ambiguous-tokens | 0.912    | 0.8603    | 0.8649 | 41821   |


#### Score on other corpora

##### Glaise, Part 2

*Definition to come*. POS has no NOMcom vs. NOMpro (needs to be fixed in a later training.)

| Task             |   Accuracy |   Accuracy on V != _ |
|------------------|------------|----------------------|
| lemma            |      94.73 |                94.73 |
| Deg              |      97.64 |                93.46 |
| Numb             |      96.84 |                96.28 |
| Person           |      99.85 |                99.75 |
| Mood_Tense_Voice |      98.18 |                93.77 |
| Case             |      93.05 |                88.96 |
| Gend             |      96.29 |                89.93 |
| pos              |      65.11 |                65.11 |

<!-- End Scores LASLA -->

### Model LASLA Plus

The model LASLA+ is trained on additionnal data, creating some noise in the original dataset and resulting in apparently worse results on classical data (approxim. -0.3%). It's results are detailed in [LASLA-plus.md](reports/lasla-plus.md).

<!-- Start Scores LASLA+ -->


More details:
- [lemma](reports/lasla-plus.md#lemma)
- [pos](reports/lasla-plus.md#pos)
- [Gend](reports/lasla-plus.md#Gend)
- [Numb](reports/lasla-plus.md#Numb)
- [Case](reports/lasla-plus.md#Case)
- [Deg](reports/lasla-plus.md#Deg)
- [Mood_Tense_Voice](reports/lasla-plus.md#Mood_Tense_Voice)
- [Person](reports/lasla-plus.md#Person)
- [Dis](reports/lasla-plus.md#Dis)




#### lemma

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.972    | 0.82      | 0.8138 | 169822  |
| known-tokens     | 0.9768   | 0.8903    | 0.8881 | 161674  |
| unknown-tokens   | 0.8759   | 0.7321    | 0.7272 | 8148    |
| ambiguous-tokens | 0.925    | 0.688     | 0.6951 | 41561   |
| unknown-targets  | 0.6304   | 0.464     | 0.4619 | 1104    |


#### pos

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.6838   | 0.7809    | 0.7707 | 169822  |
| known-tokens     | 0.6837   | 0.7873    | 0.7739 | 161674  |
| unknown-tokens   | 0.6852   | 0.6137    | 0.5761 | 8148    |
| ambiguous-tokens | 0.7938   | 0.7281    | 0.696  | 52129   |


#### Gend

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9631   | 0.9107    | 0.9138 | 169822  |
| known-tokens     | 0.9656   | 0.9146    | 0.9192 | 161674  |
| unknown-tokens   | 0.9132   | 0.8508    | 0.836  | 8148    |
| ambiguous-tokens | 0.8628   | 0.8598    | 0.8672 | 34690   |


#### Numb

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9718   | 0.9702    | 0.9698 | 169822  |
| known-tokens     | 0.9734   | 0.9717    | 0.9711 | 161674  |
| unknown-tokens   | 0.9405   | 0.9105    | 0.9205 | 8148    |
| ambiguous-tokens | 0.9052   | 0.9024    | 0.899  | 38122   |


#### Case

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9219   | 0.8863    | 0.8198 | 169822  |
| known-tokens     | 0.9243   | 0.8919    | 0.8262 | 161674  |
| unknown-tokens   | 0.8738   | 0.6555    | 0.6453 | 8148    |
| ambiguous-tokens | 0.8298   | 0.8315    | 0.7715 | 63352   |


#### Deg

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9799   | 0.968     | 0.9703 | 169822  |
| known-tokens     | 0.9822   | 0.9702    | 0.9751 | 161674  |
| unknown-tokens   | 0.9341   | 0.9251    | 0.8998 | 8148    |
| ambiguous-tokens | 0.9147   | 0.906     | 0.9283 | 27870   |


#### Mood_Tense_Voice

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9822   | 0.7717    | 0.6944 | 169822  |
| known-tokens     | 0.9857   | 0.783     | 0.7148 | 161674  |
| unknown-tokens   | 0.9113   | 0.6121    | 0.5833 | 8148    |
| ambiguous-tokens | 0.9209   | 0.6557    | 0.6384 | 16963   |


#### Person

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9971   | 0.9878    | 0.9768 | 169822  |
| known-tokens     | 0.9979   | 0.9893    | 0.9823 | 161674  |
| unknown-tokens   | 0.9821   | 0.976     | 0.9464 | 8148    |
| ambiguous-tokens | 0.9788   | 0.9418    | 0.9231 | 10040   |


#### Dis

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9716   | 0.8677    | 0.8749 | 169822  |
| known-tokens     | 0.973    | 0.8693    | 0.8784 | 161674  |
| unknown-tokens   | 0.944    | 0.6344    | 0.5121 | 8148    |
| ambiguous-tokens | 0.9102   | 0.8497    | 0.8606 | 41821   |


#### Score on other corpora

##### Glaise, Part 2

*Definition to come*

| Task             |   Accuracy |   Accuracy on V != _ |
|------------------|------------|----------------------|
| lemma            |      95.59 |                95.59 |
| Deg              |      97.79 |                93.35 |
| Numb             |      96.68 |                95.88 |
| Person           |      99.9  |                99.62 |
| Mood_Tense_Voice |      98.39 |                94.72 |
| Case             |      92.89 |                88.42 |
| Gend             |      95.83 |                89.15 |
| pos              |      93.75 |                93.75 |


<!-- End Scores LASLA+ -->


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
