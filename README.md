# Alignment Analysis of Sequential Segmentation of Lexicons to Improve Automatic Cognate Detection

Github repository for my ACL-SRW paper. Currently adding code and notebooks to this repository.

## Requirements

You need Python 3 and Numpy for this.

## Datasets

Currently this takes cognates from four languages:
* Spanish
* Portuguese
* French
* Italian

You can find training, testing and lexicons in the `data` folder.

## Code explanations with notebooks

You will need Python 3 to run the notebooks.

1. [This notebook](https://github.com/pranav-ust/cognates/blob/master/Notebook%201%2C%20Shingling.ipynb) refers to the shingling concepts which refers to section 2 of the paper.
2. [This notebook](https://github.com/pranav-ust/cognates/blob/master/Notebook%202%2C%20Graphical%20Error%20Modelling.ipynb) refers to the construction of graphical error model, which refers to section 3 of the paper.
3. [This notebook](https://github.com/pranav-ust/cognates/blob/master/Notebook%203%2C%20Similarity%20Functions.ipynb) refers to the string similarity concepts, which refers to section 4.1 of the paper.
4. [This notebook](https://github.com/pranav-ust/cognates/blob/master/Notebook%204%2C%20Error%20Modelling%20Function.ipynb) refers to the string dis-similarity concepts, which refers to section 4.2 of the paper.
5. [This notebook](https://github.com/pranav-ust/cognates/blob/master/Notebook%205%2C%20Final%20Scoring%20Function.ipynb) refers to the scoring concepts which refers to section 4.3 of the paper.

## Demo

Simply run `python3 demo.py` to demonstrate results from portuguese cognates.
