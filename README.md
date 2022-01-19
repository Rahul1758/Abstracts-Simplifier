# Abstracts-Simplifier

## Table of Content
  * [Demo](#demo)
  * [Objective](#objective)
  * [Motivation](#motivation)
  * [Data](#data)
  * [Approach](#approach)
  * [Packages/Libraries](#packageslibraries)
  * [Installation](#installation)
  * [To Do](#to-do)
  * [Contact](#contact)

## Demo
Link: [https://share.streamlit.io/rahul1758/social-media-classifier/app.py](https://share.streamlit.io/rahul1758/social-media-classifier/app.py)
### Unstructured Abstract
![](https://github.com/Rahul1758/Abstracts-Simplifier/blob/master/gifs%20%26%20imgs/unstructured_abstract.jpgg)
### Structured Abstract
![](https://github.com/Rahul1758/Abstracts-Simplifier/blob/master/gifs%20%26%20imgs/structured_abstract.jpg)
### Working
![](https://github.com/Rahul1758/Abstracts-Simplifier/blob/master/gifs%20%26%20imgs/Abstract_simplifier.gif)


## Objective
The objective of this project is to help researchers in their research. Each researcher has to skim through a lot of research papers trying to find the relevant ones for the topic in their mind. And in doing so they have to read the abstracts of papers to filter the relevant ones. But sometimes it becomes time-consuming if the abstract don't have proper structure. This Webapp uses the concept of **Sequential Sentence classification** to provide appropriate structure to the Abstracts, **making reading easier, quicker & efficient**.

## Motivation
I've always been terrified of reading long articles with huge paragraphs. Plus if the content lacks structure it adds to the anxiety of reading through the entire paragraph. I wanted to make reading easier & quicker, when I came across this Research paper which does the same but for Medical domain abstract. I've implemented the paper using State-of-the-art **BERT** Transformer architecture. 

## Data 
The dataset I am using was prepared by the authors of the Research paper. You can download it from his Github link: https://github.com/Franck-Dernoncourt/pubmed-rct
There are 2 version of the dataset:
1. Larger: **PubMed_200k_RCT** which contains 200k labelled sentences of abstracts in total. There is also a version of this dataset where the numbers mentioned in the abstract is replaced by @ symbol.
2. Smaller: **PubMed_20K_RCT** which contains 20k labelled sentences of abstracts in total. There is also a version of this dataset where the numbers mentioned in the abstract is replaced by @ symbol.

I've used the Smaller version (PubMed_20K_RCT) for this project.

## Approach
Each abstract in the dataset is represent in following format:
```
'###24293578\n' -> id denoting start of abstract of a research paper
(Label)\t(Sentence) -> Label along with each sentence in the abstract
(Label)\t(Sentence)
.
.
'\n' -> denoting the end of abstract of research paper
```
Following is my approach in solving this problem:
  * Preprocess the data (Converting the raw data into Sentence-Label format)
  * Feature Engineering (Added 2 custom features namely Line_number & Total_lines. The sentences in the abstract are correlated and derive context from each other.The order of the sentences matter a lot and these 2 features will help the model understand the sequence/order of the input sentences.)
  * Model Training (I've used BERT model that was trained on MEDLINE/PubMed from scratch from [**TensorFlow Hub**](https://tfhub.dev/google/experts/bert/pubmed/2). Training was done on Google Colab.)
  * Evaluate the model

The Model architecture I've used can be found in this [Colab Notebook](https://github.com/Rahul1758/Abstracts-Simplifier/blob/master/Training%20Notebook/Abstracts_Simplifier.ipynb)

## Packages/Libraries
* Spacy
* Streamlit
* TensorFlow
* TensorFlow-Text

## Installation
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
Then run the following command which runs the Webapp locally:
```
streamlit run app.py
```
That's it!!

## To Do
* Try and improve F1-score using different architectures. One of the way is used in this Research paper: [**Pretrained Language Models for Sequential Sentence Classification**](https://arxiv.org/pdf/1909.04054.pdf)

## References
* [**PubMed 200k RCT: a Dataset for Sequential Sentence Classification in Medical Abstracts**](https://arxiv.org/pdf/1710.06071.pdf)
* [**Neural Networks for Joint Sentence Classification in Medical Paper Abstracts**](https://arxiv.org/pdf/1612.05251.pdf)

## Contact
If you have suggestions for improvement or any other query, you can reach me at following platform:
  * [Linkedin](https://www.linkedin.com/in/rahul-menon-515702a7/)
