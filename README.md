# Sales Data Analysis Pipeline

End-to-end data analysis pipeline on a synthetic retail sales dataset.
Covers data generation, cleaning, aggregation, and visual reporting.

## Overview

The pipeline generates a realistic sales dataset procedurally, processes it
with pandas, and produces charts ready for business reporting. Useful for
testing analysis workflows without relying on sensitive or proprietary data.

## Stack

- Python 3 — pandas, numpy, matplotlib, seaborn
- Jupyter Notebook

## Structure

├── data/             # Generated CSV output
├── notebooks/        # Jupyter Notebook for interactive exploration
├── scripts/          # Production scripts (ETL + visualization)
├── visualizations/   # Chart output (.png/.jpg)
└── README.md


## Setup

```bash
git clone https://github.com/dariolignana96/sales-data-analysis.git
cd sales-data-analysis
pip install pandas numpy matplotlib seaborn
```

## Usage

```bash
python scripts/analysis.py
```

Generates `data/sales_data.csv` and saves charts to `visualizations/`.

## License

MIT — see [LICENSE](LICENSE) for details.