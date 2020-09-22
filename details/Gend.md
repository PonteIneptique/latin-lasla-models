## Gend


*[Back to readme](../README.md)*


|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9628   | 0.9088    | 0.9161 | 169822  |
| known-tokens     | 0.9652   | 0.9124    | 0.9211 | 161674  |
| unknown-tokens   | 0.9149   | 0.8547    | 0.8433 | 8148    |
| ambiguous-tokens | 0.86     | 0.8536    | 0.8694 | 34690   |


### Gend Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| Com         | 0.93      | 0.95   | 0.94     | 7130    |
| Fem         | 0.89      | 0.92   | 0.90     | 8964    |
| Masc        | 0.94      | 0.94   | 0.94     | 8561    |
| MascFem     | 0.93      | 0.95   | 0.94     | 3019    |
| MascNeut    | 0.83      | 0.87   | 0.85     | 6657    |
| Neut        | 0.84      | 0.80   | 0.82     | 8113    |
| _           | 0.99      | 0.98   | 0.98     | 127378  |
| avg / total | 0.91      | 0.92   | 0.91     | 169822  |

### Gend Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 2070         | MascNeut    | 605             |
|          |              | Neut        | 430             |
|          |              | Fem         | 342             |
|          |              | Masc        | 306             |
|          |              | Com         | 298             |
|          |              | MascFem     | 89              |
| Neut     | 1586         | Fem         | 660             |
|          |              | MascNeut    | 458             |
|          |              | _           | 412             |
|          |              | Com         | 46              |
|          |              | MascFem     | 6               |
|          |              | Masc        | 4               |
| MascNeut | 854          | _           | 482             |
|          |              | Neut        | 262             |
|          |              | Masc        | 99              |
|          |              | Com         | 10              |
|          |              | Fem         | 1               |
| Fem      | 760          | Neut        | 512             |
|          |              | _           | 235             |
|          |              | MascFem     | 5               |
|          |              | Masc        | 3               |
|          |              | Com         | 3               |
|          |              | MascNeut    | 2               |
| Masc     | 524          | _           | 366             |
|          |              | MascNeut    | 80              |
|          |              | Com         | 47              |
|          |              | MascFem     | 19              |
|          |              | Neut        | 12              |
| Com      | 389          | _           | 219             |
|          |              | MascFem     | 96              |
|          |              | Masc        | 47              |
|          |              | MascNeut    | 19              |
|          |              | Neut        | 5               |
|          |              | Fem         | 3               |
| MascFem  | 141          | Com         | 69              |
|          |              | _           | 56              |
|          |              | Masc        | 12              |
|          |              | Neut        | 3               |
|          |              | MascNeut    | 1               |

