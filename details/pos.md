## pos


*[Back to readme](../README.md)*


|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9649   | 0.8747    | 0.8626 | 169822  |
| known-tokens     | 0.967    | 0.8798    | 0.8672 | 161674  |
| unknown-tokens   | 0.9245   | 0.6683    | 0.6129 | 8148    |
| ambiguous-tokens | 0.9087   | 0.8215    | 0.7913 | 52129   |


### pos Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
|             | 0.00      | 0.00   | 0.00     | 3       |
| ADJadv.mul  | 1.00      | 0.99   | 0.99     | 84      |
| ADJadv.ord  | 0.81      | 0.96   | 0.88     | 157     |
| ADJcar      | 0.97      | 0.99   | 0.98     | 878     |
| ADJdis      | 0.98      | 0.85   | 0.91     | 105     |
| ADJmul      | 0.90      | 0.76   | 0.83     | 25      |
| ADJord      | 0.95      | 0.83   | 0.89     | 392     |
| ADJqua      | 0.92      | 0.91   | 0.92     | 14958   |
| ADV         | 0.95      | 0.95   | 0.95     | 10570   |
| ADVint      | 0.83      | 0.77   | 0.80     | 847     |
| ADVint.neg  | 0.91      | 0.98   | 0.95     | 44      |
| ADVneg      | 0.99      | 0.98   | 0.99     | 2586    |
| ADVrel      | 0.82      | 0.76   | 0.79     | 1650    |
| CONcoo      | 0.98      | 0.99   | 0.98     | 10389   |
| CONsub      | 0.91      | 0.91   | 0.91     | 5314    |
| INJ         | 0.98      | 0.92   | 0.95     | 306     |
| NOM         | 0.98      | 0.97   | 0.98     | 48840   |
| PRE         | 0.98      | 0.99   | 0.99     | 9448    |
| PROdem      | 0.99      | 0.99   | 0.99     | 7188    |
| PROind      | 0.98      | 0.98   | 0.98     | 4269    |
| PROint      | 0.88      | 0.79   | 0.83     | 1349    |
| PROper      | 0.99      | 0.99   | 0.99     | 3353    |
| PROpos      | 0.98      | 0.98   | 0.98     | 1523    |
| PROpos.ref  | 0.97      | 0.99   | 0.98     | 753     |
| PROref      | 0.99      | 0.99   | 0.99     | 1008    |
| PROrel      | 0.88      | 0.94   | 0.91     | 4384    |
| VER         | 0.98      | 0.98   | 0.98     | 39398   |
| VERaux      | 0.00      | 0.00   | 0.00     | 1       |
| avg / total | 0.87      | 0.86   | 0.87     | 169822  |

### pos Confusion Matrix

| Expected   | Total Errors | Predictions | Predicted times |
|------------|--------------|-------------|-----------------|
| NOM        | 1283         | ADJqua      | 831             |
|            |              | VER         | 279             |
|            |              | ADV         | 79              |
|            |              | PROind      | 25              |
|            |              | PROpos.ref  | 17              |
|            |              | ADJcar      | 10              |
|            |              | PRE         | 9               |
|            |              | PROpos      | 9               |
|            |              | CONcoo      | 8               |
|            |              | ADJord      | 5               |
|            |              | ADJmul      | 2               |
|            |              | ADJdis      | 2               |
|            |              | PROper      | 2               |
|            |              | PROref      | 2               |
|            |              | PROint      | 1               |
|            |              | ADVint.neg  | 1               |
|            |              | PROrel      | 1               |
| ADJqua     | 1281         | NOM         | 763             |
|            |              | VER         | 328             |
|            |              | ADV         | 171             |
|            |              | PRE         | 9               |
|            |              | ADJord      | 5               |
|            |              | CONcoo      | 3               |
|            |              | PROref      | 1               |
|            |              | PROind      | 1               |
| VER        | 641          | NOM         | 310             |
|            |              | ADJqua      | 280             |
|            |              | ADV         | 18              |
|            |              | CONsub      | 13              |
|            |              | PRE         | 8               |
|            |              | PROdem      | 4               |
|            |              | INJ         | 4               |
|            |              | PROper      | 3               |
|            |              | ADJcar      | 1               |
| ADV        | 549          | CONcoo      | 181             |
|            |              | PROdem      | 83              |
|            |              | PRE         | 74              |
|            |              | ADJqua      | 70              |
|            |              | CONsub      | 47              |
|            |              | NOM         | 36              |
|            |              | VER         | 16              |
|            |              | PROind      | 15              |
|            |              | ADJcar      | 9               |
|            |              | ADVrel      | 6               |
|            |              | ADVint      | 3               |
|            |              | ADVneg      | 3               |
|            |              | ADVint.neg  | 2               |
|            |              | PROrel      | 2               |
|            |              | INJ         | 1               |
|            |              | PROint      | 1               |
| CONsub     | 463          | PROrel      | 144             |
|            |              | ADVrel      | 143             |
|            |              | PRE         | 68              |
|            |              | CONcoo      | 26              |
|            |              | ADVneg      | 24              |
|            |              | ADV         | 21              |
|            |              | VER         | 20              |
|            |              | ADVint      | 11              |
|            |              | PROint      | 2               |
|            |              | PROind      | 2               |
|            |              | PROref      | 1               |
|            |              | NOM         | 1               |
| ADVrel     | 400          | CONsub      | 197             |
|            |              | PROrel      | 94              |
|            |              | ADVint      | 85              |
|            |              | PROint      | 11              |
|            |              | ADV         | 6               |
|            |              | VER         | 5               |
|            |              | INJ         | 1               |
|            |              | PROind      | 1               |
| PROint     | 287          | PROrel      | 245             |
|            |              | ADVint      | 22              |
|            |              | PROind      | 7               |
|            |              | CONsub      | 7               |
|            |              | ADVrel      | 3               |
|            |              | ADV         | 1               |
|            |              | NOM         | 1               |
|            |              | PROdem      | 1               |
| PROrel     | 267          | PROint      | 96              |
|            |              | CONsub      | 93              |
|            |              | ADVrel      | 38              |
|            |              | ADVint      | 16              |
|            |              | CONcoo      | 13              |
|            |              | PROind      | 11              |
| ADVint     | 191          | ADVrel      | 90              |
|            |              | CONsub      | 39              |
|            |              | PROrel      | 38              |
|            |              | PROint      | 18              |
|            |              | ADV         | 3               |
|            |              | PROind      | 2               |
|            |              | NOM         | 1               |
| CONcoo     | 110          | ADV         | 58              |
|            |              | CONsub      | 42              |
|            |              | PROrel      | 4               |
|            |              | NOM         | 3               |
|            |              | ADJqua      | 3               |
| PROdem     | 91           | ADV         | 88              |
|            |              | ADJqua      | 2               |
|            |              | PROind      | 1               |
| PROind     | 72           | PROrel      | 33              |
|            |              | PROint      | 18              |
|            |              | ADV         | 12              |
|            |              | NOM         | 5               |
|            |              | ADVrel      | 2               |
|            |              | VER         | 1               |
|            |              | ADVint.neg  | 1               |
| PRE        | 70           | ADV         | 45              |
|            |              | CONsub      | 16              |
|            |              | CONcoo      | 5               |
|            |              | VER         | 2               |
|            |              | NOM         | 1               |
|            |              | ADJqua      | 1               |
| ADJord     | 68           | ADJadv.ord  | 36              |
|            |              | ADJqua      | 23              |
|            |              | NOM         | 3               |
|            |              | ADJcar      | 3               |
|            |              | PRE         | 3               |
| ADVneg     | 50           | CONsub      | 45              |
|            |              | CONcoo      | 5               |
| PROpos     | 24           | PROper      | 23              |
|            |              | NOM         | 1               |
| INJ        | 23           | NOM         | 8               |
|            |              | PRE         | 6               |
|            |              | ADV         | 5               |
|            |              | VER         | 2               |
|            |              | CONcoo      | 1               |
|            |              | PROpos      | 1               |
| PROper     | 18           | PROpos      | 17              |
|            |              | VER         | 1               |
| ADJdis     | 16           | NOM         | 9               |
|            |              | ADJcar      | 5               |
|            |              | ADJqua      | 2               |
| ADJcar     | 12           | NOM         | 7               |
|            |              | ADV         | 5               |
| PROpos.ref | 10           | PROref      | 9               |
|            |              | NOM         | 1               |
| PROref     | 9            | PROpos.ref  | 9               |
| ADJadv.ord | 6            | ADJord      | 6               |
| ADJmul     | 6            | ADJqua      | 5               |
|            |              | ADV         | 1               |
|            | 3            | VER         | 2               |
|            |              | NOM         | 1               |
| VERaux     | 1            | VER         | 1               |
| ADJadv.mul | 1            | ADJcar      | 1               |
| ADVint.neg | 1            | ADV         | 1               |

