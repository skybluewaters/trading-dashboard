#!/bin/bash
cd "$(dirname "$0")/.."
PYTHONPATH=$(pwd) python dashboard/test_backtest.py

