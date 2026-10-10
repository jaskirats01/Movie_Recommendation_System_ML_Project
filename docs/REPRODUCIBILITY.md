# Reproduction and evaluation

[Back to README](../README.md)

## Inputs and outputs

The input is `movies_metadata.csv`. Required columns used downstream include `title`, `overview`, `genres`, `tagline`, `vote_average` and `popularity`. Text similarity uses only overview, parsed genres and tagline. Record the source URL, terms of use, file hash and retrieval date when the original dataset is supplied.

The notebook exports four artifacts into its working directory. Move them together when deploying the companion app. Do not commit the source dataset or distribute derived artifacts until its usage conditions are understood.

## Environment record

Use an isolated Python environment. Save the Python version and package versions with every reproduced result. NLTK resource availability and library changes can affect reruns. The repository currently has no lockfile or pinned training environment, so the installation command is a starting point rather than a guarantee of exact historical reproduction.

## Verification checklist

- Run every cell from a fresh kernel.
- Check input and final row counts against the README; explain any difference.
- Inspect the sparse matrix shape and avoid accidentally densifying it.
- Try a known title, an absent title and duplicate titles. The title-index construction warrants explicit duplicate-title testing.
- Confirm all serialized artifacts came from the same execution.

## Evaluation plan

Create a labelled query/relevance set before reporting recommendation-quality metrics. Compare the TF-IDF baseline against simple genre/popularity baselines and use metrics such as precision@k or nDCG@k where relevance labels support them. Report query latency, hardware, memory and dataset size together. No numeric quality, latency or scalability result is claimed by this documentation.

The model captures text similarity and inherits the coverage and biases of its source metadata. It does not establish personal preference, suitability or viewing safety.
