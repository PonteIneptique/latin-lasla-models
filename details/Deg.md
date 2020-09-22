## Deg


*[Back to readme](../README.md)*


|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9807   | 0.9681    | 0.9721 | 169822  |
| known-tokens     | 0.9828   | 0.9701    | 0.9762 | 161674  |
| unknown-tokens   | 0.9396   | 0.928     | 0.9121 | 8148    |
| ambiguous-tokens | 0.9155   | 0.9051    | 0.9277 | 27870   |


### Deg Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| Comp        | 0.98      | 0.99   | 0.99     | 1785    |
| Pos         | 0.93      | 0.93   | 0.93     | 22581   |
| Sup         | 0.97      | 0.99   | 0.98     | 1731    |
| _           | 0.99      | 0.99   | 0.99     | 143725  |
| avg / total | 0.97      | 0.97   | 0.97     | 169822  |

### Deg Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Pos      | 1683         | _           | 1669            |
|          |              | Comp        | 8               |
|          |              | Sup         | 6               |
| _        | 1549         | Pos         | 1478            |
|          |              | Sup         | 50              |
|          |              | Comp        | 21              |
| Sup      | 23           | _           | 14              |
|          |              | Pos         | 8               |
|          |              | Comp        | 1               |
| Comp     | 23           | _           | 13              |
|          |              | Pos         | 9               |
|          |              | Sup         | 1               |

