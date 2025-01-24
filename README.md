### Histopathology AI: Breast Cancer Detection with ResNet, DenseNet, and EfficientNet

#### **Overview**
This project applies state-of-the-art deep learning models—**ResNet50**, **EfficientNetB0**, and **DenseNet121**—to classify histopathology images into benign and malignant categories. Using the **BreakHis** dataset, it explores ensemble learning, advanced evaluation metrics, and calibration techniques to ensure robust and interpretable predictions.

---

#### **Motivation**
Histopathological analysis plays a critical role in diagnosing breast cancer. This project seeks to:
1. Build reliable and interpretable AI pipelines to support pathologists.
2. Evaluate deep learning models with custom metrics for medical imaging.
3. Enhance prediction reliability with calibration and ensembling methods.

---

#### **Key Features**
- **Advanced CNN Models**:
  - Transfer learning with ResNet50, EfficientNetB0, and DenseNet121.
  - Custom layers tailored for binary classification.

- **Cross-Validation**:
  - Stratified K-Fold cross-validation for robust model evaluation.

- **Metrics**:
  - Custom metrics include sensitivity, specificity, precision, F1-score, and ROC-AUC.

- **Calibration Techniques**:
  - Includes Platt scaling and isotonic regression to improve the reliability of probabilistic outputs.

- **Visualisation**:
  - Training/validation loss and accuracy curves.
  - Confusion matrices, ROC curves, and precision-recall plots for performance insights.

- **Hyperparameter Tuning**:
  - Threshold optimisation to maximize F1-score.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/drnsmith/Histopathology-AI-BreastCancer.git
cd Histopathology-AI-BreastCancer
```

### **2. Set Up the Environment**
Create a virtual environment and install the dependencies:
```bash
python -m venv env
# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On Unix or macOS:
source env/bin/activate
# Install dependencies
pip install -r requirements.txt
```

### **3. Download the BreakHis Dataset**
Obtain the dataset from Kaggle and place it in the appropriate directory (`data/`).

---

## **Usage**

### **1. Train Models**
Train models using cross-validation:
```bash
python final_experiments.py --train
```

### **2. Evaluate Models**
Evaluate the trained models:
```bash
python final_experiments.py --evaluate
```

### **3. Calibration**
Apply Platt scaling or isotonic regression for calibration:
```bash
python final_experiments.py --calibrate
```

### **4. Visualisation**
Generate performance plots and confusion matrices:
```bash
python final_experiments.py --visualize
```

### **5. Model Interpretability**
Use Grad-CAM and LIME for visualising important regions in histopathology images:
```bash
python grad_cam_lime.py
```

---

## **Results**
- **Accuracy**: The ensemble model achieved ~95% accuracy.
- **Calibration**: Improved probabilistic reliability using isotonic regression.
- **Explainability**: Grad-CAM highlighted regions critical for model decisions, improving trust in predictions.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add NewFeature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a pull request.


## Repository History Cleaned

As part of preparing this repository for collaboration, its commit history has been cleaned. This action ensures a more streamlined project for contributors and removes outdated or redundant information in the history. 

The current state reflects the latest progress as of 24/01/2025.

For questions regarding prior work or additional details, please contact the author.


---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
Special thanks to the creators of the **BreakHis dataset** and the open-source community for tools that facilitated this project.
