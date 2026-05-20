import os

# Create an output directory for our programmatic SEO landing pages
os.makedirs("guide", exist_ok=True)

# Master database array containing highly searched data science terms
topics = [
    {"slug": "augmenting-logistic-regression-data", "title": "Data Augmentation for Logistic Regression Models", "metric": "Gaussian Noise Transformation", "usecase": "Binary classification datasets with heavy sample imbalance."},
    {"slug": "linear-regression-synthetic-expansion", "title": "Expanding Linear Regression Sample Arrays Natively", "metric": "Continuous Vector Perturbation", "usecase": "Continuous numeric prediction feature frames lacking density."},
    {"slug": "balancing-random-forest-classes", "title": "Balancing Random Forest Classification Features", "metric": "Bootstrap Resampling Frameworks", "usecase": "High-dimensional categorical datasets experiencing class bias."},
    {"slug": "gradient-boosting-variance-optimization", "title": "Optimizing Gradient Boosting Variance Profiles", "metric": "Gaussian Matrix Injection", "usecase": "Boosting algorithms overfitting due to low training row counts."},
    {"slug": "xgboost-synthetic-data-tuning", "title": "Synthesizing High-Fidelity Tables for XGBoost Tuning", "metric": "Statistical Distribution Mapping", "usecase": "Hyperparameter optimization grids requiring massive scale datasets."},
    {"slug": "svm-hyperplane-boundary-augmentation", "title": "Augmenting Support Vector Machine Hyperplane Boundaries", "metric": "Vector Boundary Scaling", "usecase": "Marginal classification tasks with overlapping multi-class labels."}
]

# The baseline HTML template structure with a uniform, polished layout
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SynthetixAI Documentation</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">
    <header class="border-b border-slate-800 bg-slate-900/50 p-4">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <a href="../index.html" class="text-xl font-black bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">SynthetixAI</a>
            <a href="../index.html" class="text-sm bg-slate-800 text-slate-300 px-4 py-1.5 rounded-xl border border-slate-700 hover:text-white transition">← Use Live Generator</a>
        </div>
    </header>

    <main class="flex-grow max-w-3xl mx-auto w-full px-4 py-12">
        <article class="space-y-6">
            <div class="space-y-2">
                <span class="text-xs font-mono text-cyan-400 tracking-widest uppercase font-bold">Data Science Implementation Guide //</span>
                <h1 class="text-3xl font-extrabold text-white tracking-tight">{title}</h1>
            </div>
            
            <p class="text-slate-400 leading-relaxed text-base">
                In modern predictive pipelines, optimization metrics degrade heavily when model arrays exhibit sparse layouts. This technical documentation frames how to actively apply statistical synthesis to scale data frames for robust machine learning runs.
            </p>

            <div class="bg-slate-800/50 border border-slate-800 p-6 rounded-2xl space-y-4">
                <h3 class="text-sm uppercase font-mono text-slate-400 tracking-wider font-bold">Core Processing Blueprint</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                    <div><span class="text-slate-500 block">Recommended Engine Mode:</span> <strong class="text-cyan-400">{metric}</strong></div>
                    <div><span class="text-slate-500 block">Primary Architecture:</span> <strong class="text-blue-400">{usecase}</strong></div>
                </div>
            </div>

            <h2 class="text-xl font-bold text-white pt-4">Algorithmic Strategy Execution</h2>
            <p class="text-slate-400 leading-relaxed text-sm">
                When scaling arrays for these conditions, computing distributions natively in memory ensures vector metrics match your verification boundaries. By mapping localized variances and injecting targeted deviation coordinates, algorithms can evaluate parameters smoothly without skewing downstream outputs.
            </p>
        </article>
    </main>

    <footer class="border-t border-slate-800 bg-slate-950 py-6 text-center text-xs text-slate-600">
        <p>&copy; 2026 SynthetixAI. Structured programmatic data asset layout.</p>
    </footer>
</body>
</html>
"""

# Execute the writing generation loop
generated_count = 0
for topic in topics:
    file_path = os.path.join("guide", f"{topic['slug']}.html")
    
    # Format the template with our structural topic data
    formatted_html = html_template.format(
        title=topic['title'],
        metric=topic['metric'],
        usecase=topic['usecase']
    )
    
    # Save the file to disk cleanly
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(formatted_html)
    generated_count += 1

print(f"Success: Scaled {generated_count} programmatic landing pages inside the '/guide' path!")