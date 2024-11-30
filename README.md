### **Revolutionising Histopathology with AI: Advanced Deep Learning for Breast Cancer**
#### **Breast Cancer Diagnostics with CNNs: Feature Extraction and Statistical Analysis**

### **Overview**

This project explores the application of state-of-the-art deep learning models—**ResNet50**, **EfficientNetB0**, and **DenseNet201**—for breast cancer diagnostics using the **BreakHis dataset**. The work involves:
- Training individual CNN models.
- Combining their outputs using an **ensemble approach** to achieve optimal performance metrics.
- Re-purposing the best models as **feature extractors** for clustering and statistical analysis.
- Applying **Grad-CAM** and **LIME** for explainability, linking statistical insights with interpretable visualisations.

By combining feature extraction with clustering and statistical techniques, this work provides a comprehensive pipeline for interpreting and analysing complex datasets, bridging the gap between raw data and actionable insights.

---

## **Key Features**

- **Deep Learning Models**:
  - Trained **ResNet50**, **EfficientNetB0**, and **DenseNet201** for binary classification (benign vs. malignant).
  - Applied ensembling (logistic regression meta-model) to achieve optimal accuracy, sensitivity, and specificity.
  
- **Feature Extraction**:
  - Extracted embeddings from intermediate layers of the best models, encoding textures, shapes, and structural patterns of breast tissue.

- **Clustering**:
  - Applied hierarchical clustering on extracted features to identify distinct patterns in benign vs. malignant samples.
  - Visualised relationships between samples using dendrograms.

- **Statistical Analysis**:
  - Conducted t-tests and ANOVA to rank features based on their ability to distinguish between classes.
  - Identified statistically significant clusters and correlated features with class labels.

- **Explainability**:
  - Integrated **Grad-CAM** and **LIME** to enhance model interpretability, linking feature insights with visual regions of interest.

---

#### **Project Motivation**
Breast cancer diagnosis relies heavily on accurate and interpretable imaging tools. This project addresses critical challenges in medical AI:
- The "black-box" nature of deep learning models.
- Limited interpretability of predictions in clinical settings.
- The need for robust pipelines that bridge feature extraction with actionable insights.

By combining CNNs with statistical methods and explainability tools, this project aims to make breast cancer diagnostics not only accurate but also explainable and clinically useful.

---

#### **Steps:**

### **1. Model Training**
- Trained **ResNet50**, **EfficientNetB0**, and **DenseNet201** on the **BreakHis dataset** for binary classification (benign vs. malignant).
- Optimised model performance using data augmentation and weighted loss functions.

### **2. Model Ensembling**
- Combined the predictions of trained models using a **logistic regression meta-model** to achieve the best performance metrics:
  - **Accuracy**: 99.56%
  - **Sensitivity**: 99.54%
  - **Specificity**: 99.60%

### **3. Feature Extraction**
- Re-purposed the best-performing models to extract embeddings from intermediate layers.
- Captured complex image details to support statistical and clustering analyses.

### **4. Clustering and Visualization**
- Performed hierarchical clustering on extracted features.
- Visualised clusters using dendrograms and PCA scatter plots.

### **5. Statistical Analysis**
- Conducted statistical tests (t-tests, ANOVA) to rank features by their discriminative power.
- Identified clusters and correlated features with class labels (benign vs. malignant).

### **6. Explainability**
- Applied **Grad-CAM** to visualise regions of images influencing predictions.
- Used **LIME** to explain the contribution of individual features to model decisions.

---

## **Results**

### **Model Comparisons**
| **Model**        | **Accuracy** | **AUC**  | **Silhouette Score** |
|-------------------|--------------|----------|----------------------|
| ResNet50          | 94.2%       | 0.93     | 0.68                 |
| EfficientNetB0    | 93.8%       | 0.92     | 0.66                 |
| DenseNet201       | **98.3%**   | **0.96** | **0.78**             |
| **Ensemble**      | **99.56%**  | **0.99** | -                    |

### **Clustering and Statistical Insights**
- **Hierarchical Clustering**: DenseNet201 features produced the most distinct and cohesive clusters, highlighting its ability to separate benign and malignant samples effectively.
- **Statistical Analysis**: DenseNet201 features showed the highest significance in t-tests, with `p-values` consistently below `0.01` for top-ranked features.

### **Explainability**
- **Grad-CAM** visualisations validated that CNNs focused on clinically relevant regions in histopathological images.
- **LIME** provided granular explanations for feature contributions, enhancing trust and interpretability.

---

## **Key Visualisations**

### **1. PCA Scatter Plot**
Demonstrates class separability in the feature space.

### **2. Hierarchical Clustering**
Dendrograms reveal distinct clusters formed by benign and malignant samples.

### **3. Statistical Insights**
Bar charts and boxplots compare feature distributions across classes.

---
#### **How to Use**
 - Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/Histopathology-AI-BreastCancer.git
cd Histopathology-AI-BreastCancer
pip install -r requirements.txt
```
### Usage
 - Train Models:
```bash
python main.py --train
```
 - Evaluate Models:

```bash
python main.py --evaluate
```
 - Visualise Grad-CAM:
```bash
python utils.py --gradcam
```
### Project Structure
`main.py`: Entry point for training and evaluation.
`utils.py`: Utilities for preprocessing, Grad-CAM, and visualisations.
`models/`: Contains ResNet, DenseNet, and EfficientNet implementations.
`notebooks/`: Jupyter notebooks for experiments.
`data/`: Placeholder for dataset storage.

### License
This project is licensed under the MIT License.
