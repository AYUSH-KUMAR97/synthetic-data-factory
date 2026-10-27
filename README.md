<div align="center">

# SynthetixAI

### Client-side synthetic data generation and exploratory analysis

Upload a CSV, inspect its structure, generate an augmented dataset in the browser, and download the result without sending the uploaded file to an application server.

</div>

## Overview

SynthetixAI is a static, browser-based data utility for experimenting with tabular data augmentation and exploratory data analysis (EDA). It uses [Danfo.js](https://danfo.jsdata.org/) for in-memory dataframe operations and [Chart.js](https://www.chartjs.org/) for visualizations.

The application currently provides:

- CSV upload by file picker or drag and drop
- Input row, column, and file-size metadata
- A sample preview of the uploaded dataset
- Optional removal of rows containing missing values and duplicate rows
- Three synthetic data generation strategies:
  - **Gaussian noise** for numeric features
  - **Bootstrap resampling** for categorical and mixed data
  - **SMOTE-Lite interpolation** between sampled rows
- A configurable output row multiplier
- Original-versus-synthetic feature mean comparisons
- Download of the generated dataset as `augmented_synthetic_dataset.csv`
- Client-side EDA with numeric distributions, summary statistics, correlation-style visualization, and scatter plots
- A local budget and expense tracker
- Additional data-science implementation guides in [`guide/`](./guide)

> **Important:** Synthetic data is generated using randomized, heuristic methods. Validate statistical quality, privacy, and model performance before using generated data in production or high-stakes decisions.

## Quick start

### Option 1: Open the application directly

Open [`index.html`](./index.html) in a modern browser.

For the most reliable behavior, especially when testing browser security settings, use a local HTTP server instead.

### Option 2: Run a local HTTP server

From the repository root:

```powershell
python -m http.server 8000
```

Then open <http://localhost:8000> in your browser.

No `npm install`, build step, or backend service is required. The page loads Tailwind CSS, Danfo.js, and Chart.js from public CDNs, so an internet connection is required unless those dependencies are vendored locally.

## Using the application

1. Open the application and upload a `.csv` file.
2. Review the detected dimensions and the input preview.
3. Choose the cleaning options if needed:
   - Drop rows with missing/null values.
   - Remove exact duplicate rows.
4. Choose an augmentation strategy and set the target size or multiplier.
5. Select **Execute Pipeline & Synthesize Vector Matrix**.
6. Review the generated preview and distribution comparison.
7. Select **Download Augmented CSV File**.
8. Use the EDA controls to inspect numeric distributions and summary information before or after augmentation.

The input file must contain at least one usable column. Numeric columns are interpolated or perturbed according to the selected strategy; non-numeric values are sampled from existing values.

## How the strategies work

### Gaussian noise

For numeric columns, the application estimates the column mean and standard deviation, then creates values using normally distributed noise. Non-numeric columns are populated by random sampling from the original values.

### Bootstrap resampling

Rows are sampled with replacement. This is useful as a simple baseline for expanding a dataset while retaining the values and categories present in the source data.

### SMOTE-Lite interpolation

The application samples two rows and interpolates numeric values between them using a random weight. Non-numeric values are selected from one of the sampled rows. This is an approximation intended for exploration, not a replacement for a validated SMOTE or synthetic-data library.

## Project structure

```text
.
├── index.html              # Main application and inline browser logic
├── script.js               # Additional/legacy client-side engine code
├── generate_pages.py       # Generates the HTML files in guide/
├── guide/                  # Generated implementation guides
└── readme.md              # Project documentation
```

## Generating the guide pages

The guide pages are generated from the topic list and HTML template in [`generate_pages.py`](./generate_pages.py).

Run:

```powershell
python generate_pages.py
```

This creates or overwrites the six HTML files in [`guide/`](./guide).

## Privacy and security

- CSV processing is performed in the browser's memory.
- The repository does not include an upload API, database, or server-side processing service.
- Generated files are downloaded directly by the browser.
- The page loads third-party JavaScript dependencies from CDNs. Review or self-host those dependencies if your environment requires a fully offline or controlled supply chain.
- Do not upload sensitive or regulated data unless your browser, network, and organizational policies permit the workflow.
- Client-side processing does not by itself guarantee that the generated data is anonymous or free from memorization risk.

## Limitations

- This is a static frontend; there is no authentication, persistence, API, or server-side job queue.
- Results are randomized and may differ between runs.
- The augmentation algorithms are intentionally lightweight and should be benchmarked against domain-specific methods.
- Browser memory and performance limit practical CSV size. The interface currently advertises uploads up to approximately 50 MB, but actual capacity depends on the browser and device.
- The analytics interface is an in-browser visualization layer; it is not a full replacement for a validated statistical analysis workflow.

## Contributing

1. Create a branch for your change.
2. Keep the application runnable as a static site.
3. Test the changed flow in a current desktop browser.
4. Regenerate the guide pages when changing the generator template or topic data.
5. Keep documentation and user-facing behavior in sync.

Because this repository has no configured build or test runner, validation currently consists of serving the site locally and exercising the affected browser workflow.

