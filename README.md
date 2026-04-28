# Sales Data Analysis Pipeline

End-to-end data analysis pipeline on a synthetic retail sales dataset.
Covers data generation, cleaning, aggregation, and visual reporting.

## Structure

    sales-data-analysis/
    ├── notebooks/
    │   └── sales_analysis.ipynb    # Interactive analysis
    ├── scripts/
    │   └── analysis.py             # Standalone pipeline script
    ├── visualizations/
    │   └── sales_by_product.png    # Generated chart output
    └── README.md

## Setup

    git clone https://github.com/dariolignana96/sales-data-analysis.git
    cd sales-data-analysis
    pip install pandas numpy matplotlib seaborn

## Usage

Run the full pipeline (generates data and saves charts to visualizations/):

    python scripts/analysis.py

Or explore interactively via Jupyter:

    jupyter notebook notebooks/sales_analysis.ipynb

## License

MIT — see [LICENSE](LICENSE) for details.