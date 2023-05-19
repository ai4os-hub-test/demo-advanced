import abc
import pathlib
from dataclasses import dataclass, field
from typing import List

from deepaas_full import config, utils


class _AbstractModel(abc.ABC):
    data_path = pathlib.Path(config.DATA_PATH)

    @classmethod
    @abc.abstractmethod
    def preprocess_data(cls, datas, func=None):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def preprocess_label(cls, labels, func=None):
        raise NotImplementedError


class _HasTrain(_AbstractModel, abc.ABC):
    """Extension for _AbstractModel that includes trining images and labels.

    Arguments:
        test_images -- FIle name for raw test images.
        test_labels -- File name for raw test labels.
    """

    def __init__(self, **kwds) -> None:
        self.load_training(**kwds)

    def load_training(self, training_images, training_labels, **kwds):
        data_path = pathlib.Path(self.data_path) / "raw"
        self.x_train = utils.raw_images(data_path / training_images)
        self.y_train = utils.raw_labels(data_path / training_labels)

    @property
    def training(self):
        return zip(self.x_train, self.y_train)

    @property
    def training_len(self):
        return len(self.x_train)

    @property
    def x_train(self):
        """The x_train property."""
        return self._x_train

    @x_train.setter
    def x_train(self, value):
        self._x_train = self.preprocess_data(value)

    @property
    def y_train(self):
        """The y_train property."""
        return self._y_train

    @y_train.setter
    def y_train(self, value):
        self._y_train = self.preprocess_label(value)


class _HasTest(_AbstractModel, abc.ABC):
    """Extension for _AbstractModel that includes test images and labels.

    Arguments:
        test_images -- FIle name for raw test images.
        test_labels -- File name for raw test labels.
    """

    def __init__(self, **kwds) -> None:
        self.load_test(**kwds)

    def load_test(self, test_images, test_labels, **kwds):
        data_path = pathlib.Path(self.data_path) / "raw"
        self.x_test = utils.raw_images(data_path / test_images)
        self.y_test = utils.raw_labels(data_path / test_labels)

    @property
    def testing(self):
        return zip(self.x_test, self.y_test)

    @property
    def testing_len(self):
        return len(self.x_test)

    @property
    def x_test(self):
        """The x_test property."""
        return self._x_test

    @x_test.setter
    def x_test(self, value):
        self._x_test = self.preprocess_data(value)

    @property
    def y_test(self):
        """The y_test property."""
        return self._y_test

    @y_test.setter
    def y_test(self, value):
        self._y_test = self.preprocess_label(value)


class BaseModel(_HasTrain, _HasTest):
    """Base class to with abstract methods and generic configuration to define
    specific data models classes based on numpy and neural networks.
    """

    def __init__(self, **kwds) -> None:
        _HasTrain.__init__(self, **kwds)
        _HasTest.__init__(self, **kwds)
        self._weights = {}

    @property
    def w(self):
        return self._weights


@dataclass
class ExecutionStats:
    """Dataclass to store execution loss error and accuracy statistics from
    training and testing.
    """

    err: List[float] = field(default_factory=list)
    acc: List[int] = field(default_factory=list)

    def __repr__(self):
        return f"Err: {self.err}\t Acc: {self.acc}"

    def append(self, loss, acc, data_length):
        self.err.append(loss / data_length)
        self.acc.append(acc / data_length)

