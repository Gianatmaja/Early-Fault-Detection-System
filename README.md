# Early Fault Detection System
A proof-of-concept for the implementation of an early fault detection system in oil wells, designed to enhance operational efficiency and reduce costs.

## Introduction
The current global economic uncertainty, regulatory pressure for green technologies, as well as constant exploration for new oil fields all contribute to constantly increasing production costs for the oil & gas sector. Thus, costs reduction has become a priority for oil & gas companies. 

With unplanned downtime being a leading contributor of high costs for them, it makes sense to mitigate its risk and impact.

## Proposed Solution
An early fault detection system to identify faulty transient state (the state between normal and permament faulty) in oil wells is recommended. By identifying faulty transient states, maintenance can be done quickly and as needed, thus reducing unplanned downtime and the costs associated with it.

## Business Impact
The value driver tree below illustrate the business impact of the proposed early fault detection system. On the left, the business impact - cost reduction - is defined. Moving to the right of the tree are the drivers. This provides an illustration of how reductions in costs can be achieved through reduction of unplanned downtime and identification of transient faulty states, further driven by the performance of ML models, as well as reporting and response time following the detection of faulty transient states.

## Proof-of-Concept (PoC)
This GitHub repository serves as the PoC and will demonstrate the feasibility of the proposed early fault detection system.

### Running the PoC
The main codes for the PoC follows the Kedro project structure. To execute the entire project, go to the efds-poc directory and run the following command.

```bash
kedro run
```

To run a specific pipeline, run the following command.

```bash
kedro run --pipeline=<replace with pipeline name>
```

To run a specific node, run the following command.

```bash
kedro run --node=<replace with node name>
```

For more information on the Kedro project structure, refer to the [Kedro documentation](https://docs.kedro.org/en/stable/).

### Dataset
The dataset used for the PoC is a sample obtained from the [3W Dataset GitHub Repository](https://github.com/ricardovvargas/3w_dataset). The sampling is performed using the `data_sampling.py` script.

### Tech Stack
The highlighted tools and libraries used to develop this PoC are:
- [Kedro](https://docs.kedro.org/en/stable/): Used for code management and to promote reusability and readability.
- [D-Tale](https://pypi.org/project/dtale/): Used for automating the EDA process.
- [Scikit-Learn](https://scikit-learn.org/stable/): Used for ML model training.
- [Weights & Biases](https://docs.wandb.ai/): Used for experiment tracking and ML model management.
- [Explainer-Dashboard](https://explainerdashboard.readthedocs.io/en/latest/): Used for model explainabillity.

### Project Structure
The structure of this repository is as follows:

    .
    ├── efds-poc/                          # Main code
    │  ├── conf/                           # Configurations                              
    │  ├── data/                           # Data & Model Files
    │  ├── docs/
    │  ├── notebooks/
    │  ├── src/                            # Main pipeline codes   
    │  │  ├── requirements.txt
    │  │  ├── efds_poc                     # Pipeline & Nodes Scripts
    │  ├── wandb/                          # Wandb Runs Files                           
    │  ├── pyproject.toml
    │  ├── images/
    ├── data_sampling.py                   # data sampling script         
    └── README.md

The main codes for the project are in `src` directory inside the `efds-poc` folder. There are 4 pipelines that make up the project, namely:
- data_preprocessing
- model_experimentation
- model_saving
- model_inference

### Visualizing the Workflow
The pipeline can also be visualized using the `Kedro-Viz` library, by running to following command:

```bash
kedro viz
```

The result can be seen below.

## References
[1] Casey, J. (2020, November 30). The Oil and Gas Energy Transition: Is Cutting Costs Enough? Offshore Technology. https://www.offshore-technology.com/features/the-oil-and-gas-energy-transition-is-cutting-costs-enough/

[2] The Real Cost of Downtime in Process Manufacturing (2022, January 5). Precognize, A Samson Company. https://www.precog.co/blog/downtime-cost-process-manufacturing/

[3] Vargas, Ricardo; Munaro, Celso; Ciarelli, Patrick; Medeiros, André; Amaral, Bruno; Barrionuevo, Daniel; Araújo, Jean; Ribeiro, Jorge; Magalhães, Lucas (2019), “Data for: A Realistic and Public Dataset with Rare Undesirable Real Events in Oil Wells”, Mendeley Data, v1. http://dx.doi.org/10.17632/r7774rwc7v.1
