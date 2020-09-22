## Mood_Tense_Voice


*[Back to readme](../README.md)*


|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9835   | 0.8304    | 0.738  | 169822  |
| known-tokens     | 0.9873   | 0.8475    | 0.7589 | 161674  |
| unknown-tokens   | 0.908    | 0.7013    | 0.6715 | 8148    |
| ambiguous-tokens | 0.9258   | 0.7358    | 0.7026 | 16963   |


### Mood_Tense_Voice Classification report

| target          | precision | recall | f1-score | support |
|-----------------|-----------|--------|----------|---------|
| Adj|_|Dep       | 0.71      | 0.48   | 0.57     | 61      |
| Adj|_|Pass      | 0.93      | 0.92   | 0.93     | 736     |
| Adj|_|SemDep    | 0.00      | 0.00   | 0.00     | 3       |
| Ger|_|Act       | 0.72      | 0.92   | 0.81     | 273     |
| Ger|_|Dep       | 0.89      | 0.25   | 0.40     | 67      |
| Ger|_|SemDep    | 0.00      | 0.00   | 0.00     | 1       |
| Imp|Fut|Act     | 0.95      | 0.96   | 0.95     | 142     |
| Imp|Fut|Dep     | 0.00      | 0.00   | 0.00     | 4       |
| Imp|Pres|Act    | 0.96      | 0.94   | 0.95     | 805     |
| Imp|Pres|Dep    | 0.78      | 0.78   | 0.78     | 54      |
| Imp|Pres|Pass   | 0.00      | 0.00   | 0.00     | 1       |
| Imp|Pres|SemDep | 1.00      | 1.00   | 1.00     | 5       |
| Ind|FutAnt|Act  | 0.80      | 0.58   | 0.67     | 242     |
| Ind|Fut|Act     | 0.92      | 0.93   | 0.93     | 1339    |
| Ind|Fut|Dep     | 0.78      | 0.69   | 0.73     | 105     |
| Ind|Fut|Pass    | 0.82      | 0.74   | 0.78     | 118     |
| Ind|Fut|SemDep  | 1.00      | 0.80   | 0.89     | 5       |
| Ind|Impa|Act    | 0.99      | 1.00   | 1.00     | 1336    |
| Ind|Impa|Dep    | 0.93      | 0.88   | 0.90     | 113     |
| Ind|Impa|Pass   | 0.95      | 0.96   | 0.95     | 235     |
| Ind|Impa|SemDep | 1.00      | 0.95   | 0.97     | 40      |
| Ind|Perf|Act    | 0.97      | 0.96   | 0.96     | 4056    |
| Ind|Pqp|Act     | 1.00      | 0.99   | 0.99     | 639     |
| Ind|Pres|Act    | 0.97      | 0.97   | 0.97     | 8387    |
| Ind|Pres|Dep    | 0.93      | 0.92   | 0.93     | 689     |
| Ind|Pres|Pass   | 0.93      | 0.95   | 0.94     | 963     |
| Ind|Pres|SemDep | 1.00      | 0.98   | 0.99     | 108     |
| Inf|Perf|Act    | 1.00      | 1.00   | 1.00     | 586     |
| Inf|Pres|Act    | 0.98      | 1.00   | 0.99     | 3720    |
| Inf|Pres|Dep    | 0.93      | 0.89   | 0.91     | 428     |
| Inf|Pres|Pass   | 0.92      | 0.96   | 0.94     | 854     |
| Inf|Pres|SemDep | 1.00      | 1.00   | 1.00     | 16      |
| Par|Fut|Act     | 0.95      | 0.97   | 0.96     | 445     |
| Par|Fut|Dep     | 0.92      | 0.68   | 0.78     | 34      |
| Par|Fut|Pass    | 0.00      | 0.00   | 0.00     | 39      |
| Par|Fut|SemDep  | 1.00      | 0.33   | 0.50     | 3       |
| Par|Perf|Act    | 0.00      | 0.00   | 0.00     | 1       |
| Par|Perf|Dep    | 0.90      | 0.80   | 0.85     | 653     |
| Par|Perf|Pass   | 0.88      | 0.92   | 0.90     | 4391    |
| Par|Perf|SemDep | 0.93      | 0.91   | 0.92     | 58      |
| Par|Pres|Act    | 0.90      | 0.95   | 0.93     | 1210    |
| Par|Pres|Dep    | 0.88      | 0.63   | 0.73     | 188     |
| Par|Pres|SemDep | 1.00      | 0.20   | 0.33     | 5       |
| Sub|Impa|Act    | 0.99      | 1.00   | 0.99     | 1541    |
| Sub|Impa|Dep    | 0.95      | 0.90   | 0.92     | 136     |
| Sub|Impa|Pass   | 0.96      | 0.97   | 0.96     | 308     |
| Sub|Impa|SemDep | 1.00      | 1.00   | 1.00     | 17      |
| Sub|Perf|Act    | 0.80      | 0.91   | 0.85     | 459     |
| Sub|Pqp|Act     | 1.00      | 1.00   | 1.00     | 569     |
| Sub|Pres|Act    | 0.96      | 0.93   | 0.95     | 2617    |
| Sub|Pres|Dep    | 0.81      | 0.74   | 0.77     | 197     |
| Sub|Pres|Pass   | 0.86      | 0.85   | 0.85     | 332     |
| Sub|Pres|SemDep | 0.96      | 0.92   | 0.94     | 25      |
| SupUm|_|Act     | 0.91      | 0.59   | 0.71     | 17      |
| SupU|_|Act      | 1.00      | 0.33   | 0.50     | 15      |
| SupU|_|Dep      | 1.00      | 0.14   | 0.25     | 7       |
| _               | 0.99      | 1.00   | 1.00     | 130424  |
| avg / total     | 0.83      | 0.74   | 0.76     | 169822  |

### Mood_Tense_Voice Confusion Matrix

| Expected        | Total Errors | Predictions     | Predicted times |
|-----------------|--------------|-----------------|-----------------|
| _               | 613          | Par|Perf|Pass   | 377             |
|                 |              | Par|Pres|Act    | 61              |
|                 |              | Par|Perf|Dep    | 40              |
|                 |              | Ind|Pres|Act    | 32              |
|                 |              | Inf|Pres|Pass   | 18              |
|                 |              | Imp|Pres|Act    | 15              |
|                 |              | Par|Fut|Act     | 14              |
|                 |              | Ind|Perf|Act    | 10              |
|                 |              | Sub|Pres|Act    | 9               |
|                 |              | Ind|Fut|Act     | 8               |
|                 |              | Inf|Pres|Act    | 8               |
|                 |              | Par|Pres|Dep    | 6               |
|                 |              | Inf|Pres|Dep    | 5               |
|                 |              | Par|Perf|SemDep | 4               |
|                 |              | Adj|_|Dep       | 2               |
|                 |              | Sub|Pres|SemDep | 1               |
|                 |              | Ind|Pres|Pass   | 1               |
|                 |              | Adj|_|Pass      | 1               |
|                 |              | SupUm|_|Act     | 1               |
| Par|Perf|Pass   | 347          | _               | 312             |
|                 |              | Par|Perf|Dep    | 16              |
|                 |              | Ind|Pres|Act    | 10              |
|                 |              | Ind|Perf|Act    | 3               |
|                 |              | Imp|Pres|Act    | 2               |
|                 |              | Imp|Fut|Act     | 2               |
|                 |              | Sub|Pres|Act    | 1               |
|                 |              | Inf|Pres|Act    | 1               |
| Ind|Pres|Act    | 255          | Ind|Perf|Act    | 102             |
|                 |              | _               | 88              |
|                 |              | Sub|Pres|Act    | 24              |
|                 |              | Par|Perf|Pass   | 19              |
|                 |              | Ind|Fut|Act     | 8               |
|                 |              | Imp|Pres|Act    | 7               |
|                 |              | Imp|Fut|Act     | 4               |
|                 |              | Par|Perf|Dep    | 1               |
|                 |              | Ind|Pqp|Act     | 1               |
|                 |              | Sub|Perf|Act    | 1               |
| Sub|Pres|Act    | 189          | Ind|Fut|Act     | 87              |
|                 |              | Ind|Pres|Act    | 62              |
|                 |              | _               | 30              |
|                 |              | Sub|Impa|Act    | 4               |
|                 |              | Ind|Impa|Act    | 2               |
|                 |              | Par|Pres|Act    | 1               |
|                 |              | Sub|Pres|Pass   | 1               |
|                 |              | Ind|Perf|Act    | 1               |
|                 |              | Par|Perf|Pass   | 1               |
| Ind|Perf|Act    | 147          | Ind|Pres|Act    | 71              |
|                 |              | Inf|Pres|Act    | 28              |
|                 |              | Inf|Pres|Pass   | 24              |
|                 |              | _               | 10              |
|                 |              | Par|Perf|Pass   | 6               |
|                 |              | Imp|Pres|Act    | 4               |
|                 |              | Par|Perf|Dep    | 1               |
|                 |              | Sub|Impa|Dep    | 1               |
|                 |              | Sub|Pres|Act    | 1               |
|                 |              | Inf|Pres|Dep    | 1               |
| Par|Perf|Dep    | 128          | Par|Perf|Pass   | 82              |
|                 |              | _               | 45              |
|                 |              | Ind|Pres|Act    | 1               |
| Ind|FutAnt|Act  | 101          | Sub|Perf|Act    | 93              |
|                 |              | Ind|Pres|Pass   | 3               |
|                 |              | Ind|Pres|Act    | 2               |
|                 |              | _               | 2               |
|                 |              | Ind|Pres|Dep    | 1               |
| Ind|Fut|Act     | 90           | Sub|Pres|Act    | 51              |
|                 |              | Ind|Pres|Act    | 27              |
|                 |              | _               | 6               |
|                 |              | Sub|Impa|Act    | 2               |
|                 |              | Ind|FutAnt|Act  | 2               |
|                 |              | Ind|Perf|Act    | 1               |
|                 |              | Par|Perf|Pass   | 1               |
| Par|Pres|Dep    | 70           | Par|Pres|Act    | 61              |
|                 |              | _               | 9               |
| Ind|Pres|Dep    | 57           | Ind|Pres|Pass   | 31              |
|                 |              | Sub|Pres|Dep    | 7               |
|                 |              | Imp|Pres|Dep    | 6               |
|                 |              | Inf|Pres|Act    | 3               |
|                 |              | Sub|Perf|Act    | 2               |
|                 |              | Ind|Fut|Dep     | 2               |
|                 |              | Sub|Pres|Pass   | 2               |
|                 |              | _               | 2               |
|                 |              | Ind|FutAnt|Act  | 1               |
|                 |              | Sub|Impa|Dep    | 1               |
| Par|Pres|Act    | 56           | _               | 46              |
|                 |              | Par|Pres|Dep    | 10              |
| Adj|_|Pass      | 56           | Ger|_|Act       | 50              |
|                 |              | Adj|_|Dep       | 5               |
|                 |              | _               | 1               |
| Sub|Pres|Dep    | 52           | Sub|Pres|Pass   | 16              |
|                 |              | Ind|Pres|Dep    | 13              |
|                 |              | Ind|Fut|Dep     | 9               |
|                 |              | Inf|Pres|Act    | 4               |
|                 |              | Ind|Fut|Pass    | 3               |
|                 |              | Ind|Pres|Pass   | 3               |
|                 |              | Imp|Pres|Dep    | 2               |
|                 |              | Sub|Perf|Act    | 2               |
| Sub|Pres|Pass   | 51           | Ind|Pres|Pass   | 16              |
|                 |              | Ind|Fut|Pass    | 10              |
|                 |              | Sub|Pres|Dep    | 9               |
|                 |              | Inf|Pres|Act    | 6               |
|                 |              | Ind|Pres|Dep    | 3               |
|                 |              | _               | 2               |
|                 |              | Ind|Pres|Act    | 1               |
|                 |              | Ind|Perf|Act    | 1               |
|                 |              | Sub|Impa|Pass   | 1               |
|                 |              | Sub|Perf|Act    | 1               |
|                 |              | Sub|Pres|Act    | 1               |
| Imp|Pres|Act    | 50           | _               | 37              |
|                 |              | Ind|Perf|Act    | 5               |
|                 |              | Par|Perf|Pass   | 3               |
|                 |              | Ind|Pres|Act    | 2               |
|                 |              | Imp|Fut|Act     | 1               |
|                 |              | Inf|Pres|Pass   | 1               |
|                 |              | Adj|_|Pass      | 1               |
| Ger|_|Dep       | 50           | Ger|_|Act       | 42              |
|                 |              | Adj|_|Dep       | 4               |
|                 |              | Adj|_|Pass      | 3               |
|                 |              | _               | 1               |
| Inf|Pres|Dep    | 45           | Inf|Pres|Pass   | 27              |
|                 |              | _               | 17              |
|                 |              | Par|Perf|Pass   | 1               |
| Ind|Pres|Pass   | 45           | Ind|Pres|Dep    | 18              |
|                 |              | Sub|Pres|Pass   | 11              |
|                 |              | Sub|Perf|Act    | 5               |
|                 |              | _               | 5               |
|                 |              | Ind|Fut|Pass    | 1               |
|                 |              | Ind|Fut|Act     | 1               |
|                 |              | Ind|Perf|Act    | 1               |
|                 |              | Inf|Pres|Pass   | 1               |
|                 |              | Ind|Pres|Act    | 1               |
|                 |              | Ind|Fut|Dep     | 1               |
| Sub|Perf|Act    | 42           | Ind|FutAnt|Act  | 31              |
|                 |              | _               | 3               |
|                 |              | Ind|Pres|Act    | 2               |
|                 |              | Sub|Pres|Pass   | 2               |
|                 |              | Ind|Pres|Pass   | 2               |
|                 |              | Sub|Pqp|Act     | 1               |
|                 |              | Ind|Perf|Act    | 1               |
| Par|Fut|Pass    | 39           | Par|Perf|Pass   | 36              |
|                 |              | _               | 2               |
|                 |              | Ind|FutAnt|Act  | 1               |
| Inf|Pres|Pass   | 37           | Inf|Pres|Dep    | 20              |
|                 |              | _               | 12              |
|                 |              | Ind|Perf|Act    | 4               |
|                 |              | Ind|Fut|Pass    | 1               |
| Ind|Fut|Dep     | 33           | Sub|Pres|Dep    | 14              |
|                 |              | Ind|Pres|Dep    | 7               |
|                 |              | Ind|Fut|Pass    | 4               |
|                 |              | Imp|Pres|Dep    | 3               |
|                 |              | Sub|Pres|Pass   | 1               |
|                 |              | Ind|Impa|Dep    | 1               |
|                 |              | Ind|Perf|Act    | 1               |
|                 |              | Inf|Pres|Act    | 1               |
|                 |              | Ind|Pres|Pass   | 1               |
| Adj|_|Dep       | 32           | Adj|_|Pass      | 28              |
|                 |              | Ger|_|Act       | 3               |
|                 |              | _               | 1               |
| Ind|Fut|Pass    | 31           | Sub|Pres|Pass   | 13              |
|                 |              | Ind|Fut|Dep     | 6               |
|                 |              | Ind|Pres|Pass   | 6               |
|                 |              | Inf|Pres|Act    | 3               |
|                 |              | Ind|Fut|Act     | 1               |
|                 |              | Ind|FutAnt|Act  | 1               |
|                 |              | Ind|Perf|Act    | 1               |
| Ger|_|Act       | 21           | Adj|_|Pass      | 18              |
|                 |              | Ger|_|Dep       | 2               |
|                 |              | Adj|_|Dep       | 1               |
| Inf|Pres|Act    | 16           | _               | 8               |
|                 |              | Ind|Perf|Act    | 5               |
|                 |              | Imp|Pres|Act    | 1               |
|                 |              | Inf|Pres|Dep    | 1               |
|                 |              | Sub|Impa|Act    | 1               |
| Ind|Impa|Dep    | 14           | Ind|Impa|Pass   | 12              |
|                 |              | Ind|Fut|Dep     | 1               |
|                 |              | Imp|Pres|Dep    | 1               |
| Par|Fut|Act     | 13           | _               | 8               |
|                 |              | Inf|Pres|Act    | 2               |
|                 |              | Par|Fut|Dep     | 2               |
|                 |              | Par|Perf|Pass   | 1               |
| Sub|Impa|Dep    | 13           | Sub|Impa|Pass   | 11              |
|                 |              | Sub|Pres|Dep    | 1               |
|                 |              | Ind|Pres|Dep    | 1               |
| Imp|Pres|Dep    | 12           | Inf|Pres|Act    | 8               |
|                 |              | Sub|Pres|Dep    | 2               |
|                 |              | Ind|Fut|Dep     | 1               |
|                 |              | _               | 1               |
| Par|Fut|Dep     | 11           | Par|Fut|Act     | 7               |
|                 |              | Par|Perf|Dep    | 2               |
|                 |              | Ind|Pres|Pass   | 1               |
|                 |              | _               | 1               |
| Ind|Impa|Pass   | 10           | Ind|Impa|Dep    | 7               |
|                 |              | Ind|Impa|Act    | 3               |
| SupU|_|Act      | 10           | Par|Perf|Pass   | 8               |
|                 |              | _               | 2               |
| Sub|Impa|Pass   | 9            | Sub|Impa|Dep    | 5               |
|                 |              | Sub|Impa|Act    | 3               |
|                 |              | Sub|Pres|Pass   | 1               |
| SupUm|_|Act     | 7            | _               | 7               |
| SupU|_|Dep      | 6            | Par|Perf|Pass   | 4               |
|                 |              | _               | 2               |
| Ind|Pqp|Act     | 6            | Ind|Pres|Act    | 5               |
|                 |              | Ind|Impa|Act    | 1               |
| Imp|Fut|Act     | 6            | Par|Perf|Pass   | 5               |
|                 |              | _               | 1               |
| Sub|Impa|Act    | 5            | Sub|Pres|Act    | 3               |
|                 |              | _               | 1               |
|                 |              | Sub|Impa|Pass   | 1               |
| Par|Perf|SemDep | 5            | Par|Perf|Pass   | 3               |
|                 |              | _               | 2               |
| Par|Pres|SemDep | 4            | Par|Pres|Act    | 4               |
| Imp|Fut|Dep     | 4            | Ind|Pres|Dep    | 2               |
|                 |              | Par|Perf|Pass   | 1               |
|                 |              | _               | 1               |
| Adj|_|SemDep    | 3            | Adj|_|Pass      | 3               |
| Ind|Impa|SemDep | 2            | Ind|Impa|Act    | 2               |
| Ind|Pres|SemDep | 2            | Ind|Pres|Act    | 1               |
|                 |              | Ind|Perf|Act    | 1               |
| Sub|Pres|SemDep | 2            | Sub|Pres|Act    | 2               |
| Par|Fut|SemDep  | 2            | Par|Perf|Pass   | 1               |
|                 |              | Par|Fut|Act     | 1               |
| Ind|Fut|SemDep  | 1            | Ind|Fut|Act     | 1               |
| Imp|Pres|Pass   | 1            | Inf|Pres|Act    | 1               |
| Ger|_|SemDep    | 1            | Ger|_|Act       | 1               |
| Par|Perf|Act    | 1            | Par|Perf|Pass   | 1               |
| Inf|Perf|Act    | 1            | Par|Perf|Pass   | 1               |
| Ind|Impa|Act    | 1            | Sub|Impa|Act    | 1               |

