"""
This is a boilerplate pipeline 'model_experimentation'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_rf_models, train_xgb_models


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = split_data,
                inputs = 'events_preprocessed',
                outputs = ['train_data', 'test_data'],
                name = 'split_data_node',
            ),
            node(
                func = train_rf_models,
                inputs = ['train_data', 'test_data'],
                outputs = None,
                name = 'train_rf_node',
            ),
            node(
                func = train_xgb_models,
                inputs = ['train_data', 'test_data'],
                outputs = None,
                name = 'train_xgb_node',
            )
        ]
    )
