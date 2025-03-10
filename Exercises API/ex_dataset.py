#pip install datasets

import pandas as pd
from datasets import load_dataset

# Print all the available datasets
from huggingface_hub import list_datasets
print([dataset.id for dataset in list_datasets()].head())

dataset =  load_dataset('winogrande', 'winogrande_debiased')


# We inspect dataset and create df for each list
#print(dataset)
train_df = dataset['train'].to_pandas()
test_df = dataset['test'].to_pandas()

validation_df = dataset['validation'].to_pandas()


#print(train_df.head())