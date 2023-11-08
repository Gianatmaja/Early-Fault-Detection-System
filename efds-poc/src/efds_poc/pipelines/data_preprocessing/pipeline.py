"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import auto_eda, preproc_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = auto_eda,
                inputs = 'events',
                outputs = None,
                name = 'auto_eda_node',
            ),
            node(
                func = preproc_data,
                inputs = 'events',
                outputs = 'events_preprocessed',
                name = 'preprocess_data_node',
            )
        ]
    )