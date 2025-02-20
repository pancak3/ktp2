import logging
import datetime
import os
import shutil
from pathlib import Path
from pprint import pformat
from joblib import dump, load
from .MyClasses import Model


def save_model(grid, test_acc, scores):
    if not os.path.exists("models"):
        remake_dir("models")
    model = Model(grid.best_params_, test_acc, grid.scoring, grid.cv, grid.best_estimator_, scores)
    f_path = 'models/{0:.4f}_{1}'.format(test_acc, f"{datetime.datetime.now():%Y-%m-%d_%H:%M}")
    while os.path.exists(f_path):
        f_path += "_"
    dump(model, f_path)
    logging.info("\n{} \n[*] Saved {}".format(pformat(vars(model)), f_path))
    return f_path


def load_model(f_path):
    model = load(f_path)
    logging.info("\n{} \n[*] Loaded {}".format(pformat(vars(model)), f_path))
    return model


def remake_dir(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    # os.mkdir(dir_name, 0o755)
