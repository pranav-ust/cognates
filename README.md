# Alignment Analysis of Sequential Segmentation of Lexicons to Improve Automatic Cognate Detection

Github repository for my ACL-SRW paper. My paper looks into the problem of finding a cognate from a search space of a lexicon list. I approached the solution by creating a ranker function consisting of two modules: shingle similarity function and graphical error modelling function. 

![Poster](https://github.com/pranav-ust/cognates/blob/master/utils/poster.jpg)

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

## Citation

If you find this useful, then please cite my work:

```
@InProceedings{P18-3019,
  author = 	"A, Pranav",
  title = 	"Alignment Analysis of Sequential Segmentation of Lexicons to Improve Automatic Cognate Detection",
  booktitle = 	"Proceedings of ACL 2018, Student Research Workshop",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"134--140",
  location = 	"Melbourne, Australia",
  url = 	"http://aclweb.org/anthology/P18-3019"
}

```
