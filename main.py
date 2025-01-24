import argparse
from models import build_model
from utils import preprocess_data, evaluate_model

def main():
    parser = argparse.ArgumentParser(description="Histopathology AI Project")
    parser.add_argument('--train', action='store_true', help="Train the model")
    parser.add_argument('--evaluate', action='store_true', help="Evaluate the model")
    args = parser.parse_args()

    if args.train:
        print("Training the model...")
        # Add training code here

    if args.evaluate:
        print("Evaluating the model...")
        # Add evaluation code here

if __name__ == "__main__":
    main()
