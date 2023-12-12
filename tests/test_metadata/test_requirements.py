"""Testing module for api metadata. This is a test file designed to use pytest
and prepared with some basic assertions as base to add your own tests.

You can add new tests using the following structure:
```py
def test_{description for the test}(metadata):
    # Add your assertions inside the test function
    assert {statement_1 that returns true or false}
    assert {statement_2 that returns true or false}
```
The conftest.py module in the same directory includes the fixture to return
to your tests inside the argument variable `metadata` the value generated by
your function defined at `api.get_metadata`.

If your file grows in complexity, you can split it into multiple files in
the same folder. However, remember to add the prefix `test_` to the file.
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


def test_author(metadata):
    """Tests that metadata provides authors information."""
    assert "author" in metadata
    assert metadata["author"] == ["Borja Esteban"]


def test_email(metadata):
    """Tests that metadata provides authors information."""
    assert "author-email" in metadata
    assert metadata["author-email"] == {
        "Borja Esteban": "boressan@outlook.com"
    }


def test_description(metadata):
    """Tests that metadata provides description information."""
    assert "description" in metadata
    assert metadata["description"] == "DEEPaaS full demo/template."


def test_license(metadata):
    """Tests that metadata provides license information."""
    assert "license" in metadata
    assert metadata["license"] == "MIT License"


def test_version(metadata):
    """Tests that metadata provides version information."""
    assert "version" in metadata
    assert isinstance(metadata["version"], str)
    assert all(v.isnumeric() for v in metadata["version"].split("."))
    assert len(metadata["version"].split(".")) == 3


def test_models(metadata):
    """Tests that metadata provides models information."""
    assert "models" in metadata
    assert metadata["models"] == {"simple_convolution": "Testing model."}


def test_datasets(metadata):
    """Tests that metadata provides datasets information."""
    assert "datasets" in metadata
    assert metadata["datasets"] == ["t100-dataset.npz"]
