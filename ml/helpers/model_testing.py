import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from typing import Dict, List, Any

# Project dependencies
from helpers.logging import ml_logging


def compute_confusion_matrix(y_true, y_pred) -> Dict[str, int]:
    """
    Computes the confusion matrix values (TN, FP, FN, TP).
    """
    cm = confusion_matrix(y_true, y_pred)
    if cm.shape == (2, 2):
        tn, fp, fn, tp = cm.ravel()
    else:
        tn, fp, fn, tp = 0, 0, 0, 0
    
    return {"TN": tn, "FP": fp, "FN": fn, "TP": tp}


def extract_metrics(report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts precision, recall, and f1-score for both classes and their averages.
    """
    return {
        "precision_0": report.get("0", {}).get("precision"),
        "recall_0": report.get("0", {}).get("recall"),
        "f1_score_0": report.get("0", {}).get("f1-score"),
        "precision_1": report.get("1", {}).get("precision"),
        "recall_1": report.get("1", {}).get("recall"),
        "f1_score_1": report.get("1", {}).get("f1-score"),
        "macro_avg_precision": report.get("macro avg", {}).get("precision"),
        "macro_avg_recall": report.get("macro avg", {}).get("recall"),
        "macro_avg_f1": report.get("macro avg", {}).get("f1-score"),
        "weighted_avg_precision": report.get("weighted avg", {}).get("precision"),
        "weighted_avg_recall": report.get("weighted avg", {}).get("recall"),
        "weighted_avg_f1": report.get("weighted avg", {}).get("f1-score"),
    }


def compute_accuracy(conf_matrix: Dict[str, int]) -> float:
    """
    Computes accuracy from the confusion matrix values.
    """
    total_samples = sum(conf_matrix.values())
    return (conf_matrix["TP"] + conf_matrix["TN"]) / total_samples if total_samples > 0 else None


def evaluate_model(model: RandomForestClassifier,
                   X_test: pd.DataFrame, y_test: pd.Series, 
                   iterations: int = 20) -> List[Dict[str, Any]]:
    """
    Evaluates a model multiple times, computing performance metrics.

    :param model: The trained model to be evaluated.
    :param X_test: Test features.
    :param y_test: True labels.
    :param iterations: Number of times to repeat the evaluation.
    :return: A list of dictionaries containing evaluation metrics.
    """
    inferences = []
    ml_logging.info("Starting Evaluate model...")
    for i in range(iterations):
        ml_logging.info(f"Getting inference {i + 1}/{iterations}..")
        y_pred = model.predict(X_test)
        conf_matrix = compute_confusion_matrix(y_test, y_pred)
        report = classification_report(y_test, y_pred, labels=[0, 1], output_dict=True)
        metrics = extract_metrics(report)
        accuracy = compute_accuracy(conf_matrix)

        inference = {**conf_matrix, "accuracy": accuracy, **metrics}
        ml_logging.info(f"Inference {i + 1}/{iterations} result:\n{inference}")

        inferences.append(inference)
    
    return inferences
