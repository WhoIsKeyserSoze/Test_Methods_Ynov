from src.digging_estimator import DiggingEstimator
from unittest.mock import MagicMock

estimator = DiggingEstimator()
estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
