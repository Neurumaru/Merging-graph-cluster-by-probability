import numpy as np


# from sklearn.metrics import f1_score


def f1_score(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    if TP == 0:
        return 0
    Precision = TP / (TP + FP)
    Recall = TP / (TP + FN)
    F1_Score = 2 * (Recall * Precision) / (Recall + Precision)
    return F1_Score


def f1_score_multiprocess(l):
    t, p = l
    return f1_score(t, p)
