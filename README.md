Machine Learning for evolving graph data
==============================
Research is mostly restricted to static graphs, although most graphs change considerably over time. We need to compute embeddings that encode the temporal information - but representation learning for temporal graphs is largely unexplored. A machine could learn a temporal graph effectively only when it considers both the spatial topological structure of the nodes in a graph and change of network over time (temporal aspects). The nodes in the graph with certain relation in the past could not be ignored in the later stages of time. Temporal graph convolutional network (T-GCN) is a deep learning model which uses graph convolutional network (GCN) and gated recurrent unit (GRU) to capture spatial and temporal dependencies respectively. In this paper, TGCN is applied to OpenSky dataset and the results are compared against the baseline models. 

Motivation:
------------
In the field of representation learning for graphs, research is mostly restricted to static graphs. This leaves out valuable information as most graphs change considerably over time. To solve this problem, we need to compute embeddings that encode the temporal information. Temporal Graph Convolutional Networks (T-GCN) is one such deep learning technique to learn the spatio-temporal aspects of the dynamic graphs.

Dataset:
------------
The connectivity of flights all over the world can be viewed as a dynamic graph. Due to COVID-19, there where huge changes in the amount of flights in the past year. One dataset which captures this trend is the OpenSky dataset available for the time period from January 2019 till today.

Tasks:
------------
The research project consists of preparing the data and then analyzing plus visualizing it. First, several baseline time-series prediction approaches are evaluated before introducing graph-based techniques. The use case is to predict the number of flights between airports given their history (spatio-temporal analysis). This will be further enriched by additional data such as the COVID-19 cases per country.


Video:
------------
Visualization of node-link representation of airports and connecting flights for the dataset of flights connectivity from 1st January 2019 till 31st October 2020
https://youtu.be/GgUkT-8h_UA



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- Adjacency matrix and flight count datasets.
    │   └── raw            <- Download the dataset from OpenSky (https://zenodo.org/record/4419079#.YBcxqOj0lnI)
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries. Also baseline models like ARIMA, VAR.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling (Code included in models -- > Baseline section)
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   └── train_model.py <- Run this first for tgcn
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
