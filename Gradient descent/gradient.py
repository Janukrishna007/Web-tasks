{
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9XxsoFmaKfmy05nYVc8wt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.10.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "dockerImageVersionId": 30732,
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "import numpy as np",
      "metadata": {
        "id": "ekdF7DxH9BP4",
        "execution": {
          "iopub.status.busy": "2024-06-29T20:17:25.607422Z",
          "iopub.execute_input": "2024-06-29T20:17:25.607775Z",
          "iopub.status.idle": "2024-06-29T20:17:25.612742Z",
          "shell.execute_reply.started": "2024-06-29T20:17:25.607746Z",
          "shell.execute_reply": "2024-06-29T20:17:25.611334Z"
        },
        "trusted": true
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "a = float(input(\"Enter first coefficent  - a : \"))\nb = float(input(\"Enter second coefficent - b : \"))\nc = float(input(\"Enter third coefficent  - c : \"))\nd = float(input(\"Enter fourth coefficent - d : \"))",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RZTrCEpw9k7L",
        "outputId": "e5d43902-c9eb-4dc9-f1e6-7ea36d82b3f4",
        "execution": {
          "iopub.status.busy": "2024-06-29T20:17:25.627050Z",
          "iopub.execute_input": "2024-06-29T20:17:25.627478Z",
          "iopub.status.idle": "2024-06-29T20:17:30.534501Z",
          "shell.execute_reply.started": "2024-06-29T20:17:25.627444Z",
          "shell.execute_reply": "2024-06-29T20:17:30.533412Z"
        },
        "trusted": true
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "Enter first coefficent  - a :  5\nEnter second coefficent - b :  4\nEnter third coefficent  - c :  3\nEnter fourth coefficent - d :  2\n"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "x = np.random.rand()\n\nlearning_rate = .01\nepochs =100",
      "metadata": {
        "id": "uojLsDsl9pHv",
        "execution": {
          "iopub.status.busy": "2024-06-29T20:17:30.536191Z",
          "iopub.execute_input": "2024-06-29T20:17:30.536519Z",
          "iopub.status.idle": "2024-06-29T20:17:30.541656Z",
          "shell.execute_reply.started": "2024-06-29T20:17:30.536490Z",
          "shell.execute_reply": "2024-06-29T20:17:30.540456Z"
        },
        "trusted": true
      },
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "for epoch in range(epochs):\n  value = a*x**3 + b*x**2 + d*x +c\n  gradient  = 3*a *x**2 + 2*b*x+c\n\n  if gradient < -1:\n    gradient =0\n    x -=  learning_rate *gradient",
      "metadata": {
        "id": "8loo6aHH9zhY",
        "execution": {
          "iopub.status.busy": "2024-06-29T20:17:30.543062Z",
          "iopub.execute_input": "2024-06-29T20:17:30.543595Z",
          "iopub.status.idle": "2024-06-29T20:17:30.554798Z",
          "shell.execute_reply.started": "2024-06-29T20:17:30.543560Z",
          "shell.execute_reply": "2024-06-29T20:17:30.553643Z"
        },
        "trusted": true
      },
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "print(f\"The equation is: {a}x^3 + {b}x^2 + {c}x + {d} = 0\")",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XS8JC9HT93dE",
        "outputId": "ba689e49-bfb4-41ce-aa25-8f9daa2965c4",
        "execution": {
          "iopub.status.busy": "2024-06-29T20:17:30.557369Z",
          "iopub.execute_input": "2024-06-29T20:17:30.558371Z",
          "iopub.status.idle": "2024-06-29T20:17:30.568252Z",
          "shell.execute_reply.started": "2024-06-29T20:17:30.558325Z",
          "shell.execute_reply": "2024-06-29T20:17:30.567050Z"
        },
        "trusted": true
      },
      "execution_count": 42,
      "outputs": [
        {
          "name": "stdout",
          "text": "The equation is: 5.0x^3 + 4.0x^2 + 3.0x + 2.0 = 0\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "print(f\"The solution for x is approximately : {x}\")",
      "metadata": {
        "execution": {
          "iopub.status.busy": "2024-06-29T20:17:30.569670Z",
          "iopub.execute_input": "2024-06-29T20:17:30.570015Z",
          "iopub.status.idle": "2024-06-29T20:17:30.585966Z",
          "shell.execute_reply.started": "2024-06-29T20:17:30.569986Z",
          "shell.execute_reply": "2024-06-29T20:17:30.584762Z"
        },
        "trusted": true
      },
      "execution_count": 43,
      "outputs": [
        {
          "name": "stdout",
          "text": "The solution for x is approximately : 0.39318918502299505\n",
          "output_type": "stream"
        }
      ]
    }
  ]
}