#!/usr/bin/python
""" model

#FIXME Description

Author: datadonk23
Date: #FIXME
"""

import os
import numpy as np
import pandas as pd

from sklearn.externals import joblib


class Model(object):
    """ FIXME

    Trained model: FIXME

    Methods
    -------
    predict(input)
        Predicts target class based on given input

    """

    def __init__(self):
        actual_filepath = os.path.dirname(os.path.realpath(__file__))
        model_file = os.path.join(actual_filepath, "models/trained_model.pkl")
        self.trained_model = joblib.load(model_file)


    def predict(self, input):
        """ Predicts target class based on given input

        Parameters
        ----------
        input
            FIXME

        Returns
        -------
        FIXME

        """
        pred = self.trained_model.predict(input)

        return pred
