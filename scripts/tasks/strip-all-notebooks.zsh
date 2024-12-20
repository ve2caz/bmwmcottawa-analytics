#!/usr/bin/env zsh
#
# This script removes metadata and outputs from cells in a notebook.
#
# The following cells must remain empty to prevent leaking sensitive information:
# - {"metadata": {}},
# - {"outputs": []},
# 
# Jupyter notebooks are JSON files:
# {
#  "cells": [
#     {
#      "cell_type": "markdown",
#      "metadata": {},
#      "source": [
#         "## This is a markdown cell"
#      ]
#     },
#     {
#      "cell_type": "code",
#      "execution_count": null,
#      "metadata": {},
#      "outputs": [],
#      "source": [
#         "# This is a code cell\n",
#         "print(\"Hello, world!\")"
#      ]
#     }
#  ],
#  "metadata": {
#     "kernelspec": {
#      "display_name": "Python 3",
#      "language": "python",
#      "name": "python3"
#     },
#     "language_info": {
#      "codemirror_mode": {
#         "name": "ipython",
#         "version": 3
#      },
#      "file_extension": ".py",
#      "mimetype": "text/x-python",
#      "name": "python",
#      "nbconvert_exporter": "python",
#      "pygments_lexer": "ipython3",
#      "version": "3.8.5"
#     }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 4
# }
#
#
# Usage:
#   $ ./strip-notebooks.zsh
find . -name "*.ipynb" | while read notebook; do
    jq '
        .cells |= map(
            if .cell_type == "code" then
                .outputs = [] | .execution_count = null
            else
                .
            end
        )
    ' "$notebook" > tmp.$$.ipynb && mv tmp.$$.ipynb "$notebook"
done
