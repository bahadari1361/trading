#!/bin/bash
mkdir -p trading-analysis/{config,data/{historical,signals},notebooks,src/{api,analysis}}
touch trading-analysis/{.gitignore,README.md,requirements.txt}
touch trading-analysis/config/{settings.json,settings.example.json}
touch trading-analysis/notebooks/strategy_testing.ipynb
touch trading-analysis/src/{api/{__init__.py,ftmo.py,tradingview.py},analysis/{__init__.py,indicators.py,signals.py},main.py}

# .gitignore content
cat > trading-analysis/.gitignore <<EOL
# Python
venv/
*.pyc
__pycache__/

# Data files
data/

# Environment files
.env
config/settings.json

# Jupyter
.ipynb_checkpoints/
EOL

# README.md content
cat > trading-analysis/README.md <<EOL
# Trading Analysis System

Automated trading analysis for FTMO and TradingView platforms.

## Features
- Technical indicator calculations
- Signal generation
- TradingView data integration
- FTMO account integration
EOL

# requirements.txt
cat > trading-analysis/requirements.txt <<EOL
pandas>=1.3.0
numpy>=1.21.0
requests>=2.26.0
python-dotenv>=0.19.0
jupyter>=1.0.0
matplotlib>=3.4.0
EOL

echo "Repository structure created successfully!"
