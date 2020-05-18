# Pie Latin LASLA Models

[![DOI](https://zenodo.org/badge/244858653.svg)](https://zenodo.org/badge/latestdoi/244858653)

Repository for LASLA Latin models: the models were fine-tuned by Thibault Clérice, data are based on LASLA data but some adaptation might be found.

## Information about the model

*Note:* the model is currently being fine-tuned in the context of my PhD. I'll fill this part when it will be done.

- Enclitics are kept in a single token
	- Enclitic lemma are separated as such `token[Caesarque]` == `lemma[Caesar界que]` 
	- Morphology is the morphology of the first token
- Only numbers 1, 2 and 3 are known. Roman numbers are unknown.
- All punctuation signs are unknown, including the one used in abbr. `token[C]` == `lemma[Gaius]`
- Everything is lowercased at the moment. Including lemma.

## Scores

For more details about the errors, see the [Report](information/Confusion.md).

### lemma

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9752   | 0.8452    | 0.8405 | 169822  |
| unknown-tokens   | 0.8771   | 0.744     | 0.7395 | 6535    |
| ambiguous-tokens | 0.9295   | 0.706     | 0.7087 | 41834   |
| unknown-targets  | 0.6597   | 0.4933    | 0.4914 | 1099    |

### pos

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9667   | 0.8775    | 0.8682 | 169822  |
| unknown-tokens   | 0.9226   | 0.6606    | 0.583  | 6535    |
| ambiguous-tokens | 0.915    | 0.7935    | 0.7774 | 55267   |

### Gend

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.968    | 0.924     | 0.9266 | 169822  |
| unknown-tokens   | 0.9201   | 0.8727    | 0.8506 | 6535    |
| ambiguous-tokens | 0.8772   | 0.8748    | 0.8818 | 35778   |

### Numb

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9751   | 0.9739    | 0.9732 | 169822  |
| unknown-tokens   | 0.9467   | 0.9186    | 0.9254 | 6535    |
| ambiguous-tokens | 0.9171   | 0.9135    | 0.9108 | 41278   |

### Case

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9275   | 0.8887    | 0.8318 | 169822  |
| unknown-tokens   | 0.8799   | 0.6519    | 0.6268 | 6535    |
| ambiguous-tokens | 0.8381   | 0.8317    | 0.7812 | 64764   |

### Deg

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9815   | 0.9728    | 0.9728 | 169822  |
| unknown-tokens   | 0.9388   | 0.9386    | 0.9176 | 6535    |
| ambiguous-tokens | 0.916    | 0.913     | 0.9259 | 28464   |

### Mood_Tense_Voice

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9873   | 0.8608    | 0.8141 | 169822  |
| unknown-tokens   | 0.9301   | 0.762     | 0.744  | 6535    |
| ambiguous-tokens | 0.9366   | 0.7802    | 0.7675 | 19961   |

### Person

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9974   | 0.9867    | 0.9821 | 169822  |
| unknown-tokens   | 0.9827   | 0.9697    | 0.9585 | 6535    |
| ambiguous-tokens | 0.9812   | 0.9356    | 0.9262 | 12679   |

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

For more details about the errors, see the [information](information) folder.
