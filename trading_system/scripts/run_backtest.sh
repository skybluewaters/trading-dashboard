#!/bin/bash
cd "$(dirname "$0")/.."
PYTHONPATH=. python -m dashboard.test_backtest

