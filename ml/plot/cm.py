import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, model_name):
  """
  Plot a confusion matrix of model

  :param cm: confusion matrix
  :param model_name: name of model
  """
  plt.figure(figsize=(6, 4))
  sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Negativo", "Positivo"], yticklabels=["Negativo", "Positivo"])
  plt.title(f'Matriz de Confusão - {model_name}')
  plt.xlabel('Predito')
  plt.ylabel('Real')
  plt.show()