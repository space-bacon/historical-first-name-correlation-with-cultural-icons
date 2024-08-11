import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Analyze and correlate baby name trends.")
    parser.add_argument("--preprocess", action="store_true", help="Run data preprocessing")
    parser.add_argument("--analyze", action="store_true", help="Run trend analysis")
    parser.add_argument("--correlate", action="store_true", help="Run correlation analysis")
    parser.add_argument("--visualize", action="store_true", help="Generate visualizations")
    return parser.parse_args()

def run_preprocessing():
    print("Running data preprocessing...")
    subprocess.run(["python", "src/data_preprocessing.py"])

def run_trend_analysis():
    print("Running trend analysis...")
    subprocess.run(["python", "src/trend_analysis.py"])

def run_correlation_analysis():
    print("Running correlation analysis...")
    subprocess.run(["python", "src/correlation_analysis.py"])

def run_visualization():
    print("Generating visualizations...")
    subprocess.run(["python", "src/visualization.py"])

def main():
    args = parse_args()
    if args.preprocess:
        run_preprocessing()
    if args.analyze:
        run_trend_analysis()
    if args.correlate:
        run_correlation_analysis()
    if args.visualize:
        run_visualization()

if __name__ == "__main__":
    main()
