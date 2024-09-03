{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPDZ8GXqbLmQKE6Y/rOTD9f",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Oliveira-Wilson/Logica-de-programacao/blob/main/04-Estruturas-condicinais.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OvwL-LXgIzer",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e171032a-d446-4307-be5d-e6c9bea9543a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Qual a temperatura atual? 30\n"
          ]
        }
      ],
      "source": [
        "temperatura = float(input(\"Qual a temperatura atual? \"))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if temperatura > 30:\n",
        "    print(\"Muito quente\")\n",
        "elif temperatura < 15:\n",
        "    print(\"Muito frio\")\n",
        "else:\n",
        "    print(\"Temperatura agradável\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SYX8FPmcOcVQ",
        "outputId": "fe096c3d-695a-4904-d54c-d8d8f93f5afe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Temperatura agradável\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "mHiZHhRKMCss"
      }
    }
  ]
}