"""
This is a boilerplate pipeline 'model_saving'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import save_scaler, save_model, explain_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = save_scaler,
                inputs = 'events_preprocessed',
                outputs = 'scaler',
                name = 'save_scaler_node',
            ),
            node(
                func = save_model,
                inputs = 'train_data',
                outputs = 'best_model',
                name = 'save_model_node',
            ),
            node(
                func = explain_model,
                inputs = ['best_model', 'test_data'],
                outputs = None,
                name = 'explain_model_node',
            )
        ]
    )
