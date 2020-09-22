## Numb


*[Back to readme](../README.md)*


|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9702   | 0.9679    | 0.9685 | 169822  |
| known-tokens     | 0.9718   | 0.9695    | 0.9696 | 161674  |
| unknown-tokens   | 0.9385   | 0.9108    | 0.9217 | 8148    |
| ambiguous-tokens | 0.8998   | 0.8952    | 0.8946 | 38122   |


### Numb Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| Plur        | 0.95      | 0.95   | 0.95     | 35391   |
| Sing        | 0.97      | 0.97   | 0.97     | 86253   |
| _           | 0.98      | 0.98   | 0.98     | 48178   |
| avg / total | 0.97      | 0.97   | 0.97     | 169822  |

### Numb Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Sing     | 2583         | Plur        | 1748            |
|          |              | _           | 835             |
| Plur     | 1745         | Sing        | 1697            |
|          |              | _           | 48              |
| _        | 736          | Sing        | 710             |
|          |              | Plur        | 26              |

