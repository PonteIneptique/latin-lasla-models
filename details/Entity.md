## Entity


*[Back to readme](../README.md)*


|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.995    | 0.9504    | 0.7087 | 169822  |
| known-tokens     | 0.9967   | 0.966     | 0.7296 | 161674  |
| unknown-tokens   | 0.9596   | 0.6141    | 0.6009 | 8148    |
| ambiguous-tokens | 0.8891   | 0.9142    | 0.6881 | 2578    |


### Entity Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| _           | 1.00      | 1.00   | 1.00     | 162106  |
| a           | 0.87      | 0.74   | 0.80     | 1025    |
| n           | 0.93      | 0.95   | 0.94     | 6677    |
| o           | 1.00      | 0.14   | 0.25     | 14      |
| avg / total | 0.95      | 0.71   | 0.75     | 169822  |

### Entity Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| n        | 328          | _           | 243             |
|          |              | a           | 85              |
| a        | 264          | n           | 226             |
|          |              | _           | 38              |
| _        | 252          | n           | 224             |
|          |              | a           | 28              |
| o        | 12           | n           | 10              |
|          |              | _           | 2               |

