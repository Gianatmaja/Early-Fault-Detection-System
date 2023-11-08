"""
This is a boilerplate pipeline 'model_inference'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import predict_new_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = predict_new_data,
                inputs = ['extra_data1', 'events_preprocessed', 'best_model', 'scaler'],
                outputs = 'new_predictions',
                name = 'predict_new_node',
            )
        ]
    )
