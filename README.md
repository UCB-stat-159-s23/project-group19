[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](< https://ucb-stat-159-s23.github.io/project-group19/>)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-group19.git/HEAD)

## Project Overview
In our project, we explored the Motor Vehicles Collisions dataset which comes from the city of New York. The dataset contains information on motor vehicle crashes that occured from 2012-2013.

Motor crashes are a major public health and safety concern, particularly in urban areas with high traffic volumes such as New York City. In recent years, the city has seen a significant increase in the number of motor crashes, leading to a growing concern about their impact on public safety, transportation infrastructure, and economic productivity. To address these concerns, data analysis can play a crucial role in identifying the factors that contribute to motor crashes and developing effective strategies for prevention and mitigation.

This paper aims to analyze the data on motor crashes in New York City over the past few years, with a focus on identifying the key factors associated with these incidents and proposing actionable solutions to reduce their frequency and severity. We aim to find a relationship between the data included and how severe the crashes are for people. We hope the analysis conducted in the project will lead key desicion makers to improving safety and road rules.

## Dataset
The dataset can be found at this link: https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes.

## Useful Commands
### Creating an environment from an environment.yml file:
```
    conda env create -f environment.yml 
    conda activate final_proj
    conda install ipykernel
    python -m ipykernel install --user --name final_proj --display-name "IPython - final_proj
```
### Running the JupyterBook
```
cd _build/html
python -m http.server
```
and then heading to this URL: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html.

## Repository Structure
The repository is structured as follows: 

- data: Contains the raw and processed datasets we used.
- tool: Contains utils.py, housing the functions used in the Analysis notebook. In this folder as well is a tests folder to run tests on these functions.
- Analysis.ipynb: Contains the code we wrote to analyze the data. We did EDA and modelling.
- Main.ipynb: Contains a summary of the code and analysis of the EDA and modelling from Analysis.ipynb
- environment.yml: Contains all the packages and dependencies needed for the project.
- Makefile: Contains all the information needed to build a JupyterBook for this project.
