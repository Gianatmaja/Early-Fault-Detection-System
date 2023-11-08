# Early Fault Detection System
A proof-of-concept for the implementation of an early fault detection system in oil wells, designed to enhance operational efficiency and reduce costs.

## Introduction
The current global economic uncertainty, regulatory pressure for green technologies, as well as constant exploration for new oil fields all contribute to constantly increasing production costs for the oil & gas sector. Thus, costs reduction has become a priority for oil & gas companies. 

With unplanned downtime being a leading contributor of high costs for them, it makes sense to mitigate its risk and impact.

## Proposed Solution
An early fault detection system to identify faulty transient state (the state between normal and permament faulty) in oil wells is recommended. By identifying faulty transient states, maintenance can be done quickly and as needed, thus reducing unplanned downtime and the costs associated with it.

## Business Impact
The value driver tree below illustrate the business impact of the proposed early fault detection system.

## Proof-of-Concept (PoC)
This GitHub repository serves as the PoC and will demonstrate the feasibility of the proposed early fault detection system.

### Running the PoC

### Dataset
The dataset used for the PoC is a sample obtained from the [3W Dataset GitHub Repository](https://github.com/ricardovvargas/3w_dataset). The sampling is performed using the `data_sampling.py` script.

### Tech Stack
The highlighted tools and libraries used to develop this PoC are:
- [Kedro](https://docs.kedro.org/en/stable/): Used for code management and to promote reusability and readability.
- [D-Tale](https://pypi.org/project/dtale/): Used for automating the EDA process.
- [Scikit-Learn](https://scikit-learn.org/stable/): Used for ML model training.
- [Weights & Biases](https://docs.wandb.ai/): Used for experiment tracking and ML model management.
- [Explainer-Dashboard](https://explainerdashboard.readthedocs.io/en/latest/): Used for model explainabillity.

