"""Module for defining custom web fields to use on the API interface.
"""
from webargs import fields, validate
import marshmallow

from . import parsers


class PredArgsSchema(marshmallow.Schema):
    """Prediction arguments schema for api.predict function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    input_file = fields.Field(
        metadata={
            "description": "Custom file to generate predictions.",
            "type": "file",
            "location": "form",
        },
        required=True,
    )

    argument_1 = fields.Integer(
        metadata={
            "description": "Custom required argument for predictions.",
        },
        required=True,
    )

    option_1 = fields.Integer(
        metadata={
            "description": "Custom optional argument for predictions.",
        },
        required=False,
    )

    option_2 = fields.Integer(
        metadata={
            "description": "Custom optional argument for predictions.",
        },
        required=False,
    )

    accept = fields.String(
        metadata={
            "description": "Return format for method response.",
            "location": "headers",
        },
        required=True,
        validate=validate.OneOf(parsers.content_types),
    )


class TrainArgsSchema(marshmallow.Schema):
    """Training arguments schema for api.train function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    input_file = fields.Field(
        metadata={
            "description": "Custom file to use for model training.",
            "type": "file",
            "location": "form",
        },
        required=True,
    )

    target_file = fields.Field(
        metadata={
            "description": "Custom file to use for model training.",
            "type": "file",
            "location": "form",
        },
        required=True,
    )

    epochs = fields.Integer(
        metadata={
            "description": "Number of epochs to train the model.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )

    initial_epoch = fields.Integer(
        metadata={
            "description": "Epoch at which to start training.",
        },
        required=False,
        load_default=0,
        validate=validate.Range(min=0),
    )

    steps_per_epoch = fields.Integer(
        metadata={
            "description": "Steps before declaring an epoch finished.",
        },
        required=False,
        validate=validate.Range(min=0),
    )

    shuffle = fields.Boolean(
        metadata={
            "description": "Shuffle the training data before each epoch.",
        },
        required=False,
        load_default=True,
    )

    validation_split = fields.Float(
        metadata={
            "description": "Fraction of the data to be used as validation.",
        },
        required=False,
        load_default=0.0,
        validate=validate.Range(min=0.0, max=1.0),
    )

    validation_steps = fields.Integer(
        metadata={
            "description": "Steps to draw before stopping on validation.",
        },
        required=False,
        validate=validate.Range(min=0),
    )

    validation_batch_size = fields.Integer(
        metadata={
            "description": "Number of samples per validation batch.",
        },
        required=False,
        validate=validate.Range(min=0),
    )

    validation_freq = fields.Integer(
        metadata={
            "description": "Training epochs to run before validation.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )

    accept = fields.String(
        metadata={
            "description": "Return format for method response.",
            "location": "headers",
        },
        required=True,
        validate=validate.OneOf(parsers.content_types),
    )
