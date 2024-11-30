### **Revolutionising Histopathology with AI: Advanced Deep Learning for Breast Cancer**
#### **Overview**
This project explores cutting-edge applications of **deep learning** and **statistical analysis** in breast cancer histopathology, leveraging pre-trained CNN architectures such as **ResNet50**, **EfficientNetB0**, and **DenseNet201** for feature extraction. By integrating these features with advanced clustering techniques and interpretability tools, we aim to uncover meaningful intra-class patterns, improve diagnostic precision, and bridge the gap between **AI-driven insights** and clinical applications.

### Key Features:
- **Feature Extraction**:
   - Utilised state-of-the-art pre-trained CNNs to extract high-dimensional representations from histopathological images.
   - Focused on extracting features relevant to tumour heterogeneity and cellular morphology.

- **Clustering and Statistical Analysis**:
   - Applied techniques like **PCA** for dimensionality reduction and **hierarchical clustering** to group features based on their biological relevance.
   - Evaluated clustering performance using validation metrics such as **Silhouette Score** and **Calinski-Harabasz Index**.

- **Visual Interpretability**:
   - Incorporated **Grad-CAM** and **LIME** to enhance the interpretability of CNN decisions.
   - Used visualisation techniques like t-SNE and correlation heatmaps to reveal underlying patterns.

### Dataset:
- The project uses the **BreakHis** dataset, a benchmark in medical imaging, providing diverse histopathological images of breast tissue across multiple magnifications.

### Objectives:
1. **Unveil Hidden Patterns**: Leverage deep learning to identify intra-class variations in histopathological data.
2. **Enhance Model Interpretability**: Use statistical insights and visualisation tools to demystify black-box AI models.
3. **Support Precision Medicine**: Enable more nuanced, personalised diagnostic pathways for breast cancer.

### Repository Highlights:
- **Comprehensive Implementation**: Includes pipelines for data preprocessing, feature extraction, clustering, and visualisation.
- **Reproducible Code**: Modular scripts designed for scalability and adaptation to other medical imaging tasks.
- **Insights and Applications**: Detailed analyses that connect AI innovations with real-world healthcare needs.

### Future Directions:
- Expanding to other medical imaging datasets.
- Enhancing clinical validation with patient outcomes.
- Combining handcrafted and deep learning features for richer analyses.

The aim of this project is to enhance model interpretability and performance in medical diagnostics by leveraging:
- **Pre-trained CNNs** for feature extraction.
- **Clustering and Statistical Analysis** to identify meaningful patterns.
- **Explainability Tools** to bridge the gap between AI models and clinical trust.

---

## **Key Features**

- **Feature Extraction**:
  - Extracted embeddings from ResNet50, EfficientNetB0, and DenseNet201 using intermediate layers.
  - Features encoded textures, shapes, and structural patterns of breast tissue images.
- **Clustering**:
  - Applied hierarchical clustering to group data, revealing distinct patterns in benign vs. malignant classes.
  - Visualized clusters using dendrograms for interpretability.
- **Statistical Analysis**:
  - Conducted t-tests and ANOVA to assess feature importance and distinguish between classes.
- **Model Comparisons**:
  - Benchmarked CNN architectures on clustering metrics, statistical relevance, and classification accuracy.

---

## **Project Motivation**

Breast cancer diagnosis relies heavily on accurate and interpretable imaging tools. This project addresses critical challenges in medical AI:
- The "black-box" nature of deep learning models.
- Limited interpretability of predictions in clinical settings.
- The need for robust pipelines that bridge feature extraction with actionable insights.

By combining CNNs with statistical methods, this project aims to make breast cancer diagnostics not only accurate but also explainable and clinically useful.

---

## **What I’ve Done**

### **1. Data Preprocessing**
- Preprocessed the **BreakHis** dataset, resizing images to `224 x 224` pixels and normalizing intensities.
- Split the dataset into training and validation sets, maintaining class balance using stratified sampling.

### **2. Feature Extraction**
- Leveraged pre-trained **ResNet50**, **EfficientNetB0**, and **DenseNet201** models to extract embeddings.
- Focused on intermediate layers to capture rich image representations.

### **3. Clustering and Visualization**
- Performed hierarchical clustering on extracted features.
- Visualized relationships between samples using dendrograms and PCA scatter plots.

### **4. Statistical Analysis**
- Conducted statistical tests (t-tests, ANOVA) to rank features based on their ability to distinguish classes.
- Identified clusters and correlated features with class labels (benign vs. malignant).

### **5. Model Benchmarking**
- Compared models on metrics like accuracy, AUC, and silhouette scores.
- DenseNet201 emerged as the top performer across all benchmarks.

### **6. Explainability**
- Integrated **Grad-CAM** and **LIME** to enhance model interpretability, linking statistical findings to visual explanations.

---

## **Results**

### **Model Comparisons**
| **Model**        | **Accuracy** | **AUC**  | **Silhouette Score** |
|-------------------|--------------|----------|----------------------|
| ResNet50          | 94.2%       | 0.93     | 0.68                 |
| EfficientNetB0    | 93.8%       | 0.92     | 0.66                 |
| DenseNet201       | **98.3%**   | **0.96** | **0.78**             |

### **Clustering and Statistical Insights**
- **Hierarchical Clustering**: DenseNet201 produced the most distinct and cohesive clusters, highlighting its ability to separate benign and malignant samples effectively.
- **Statistical Analysis**: DenseNet201 features showed the highest significance in t-tests, with p-values consistently below 0.01 for top-ranked features.

### **Explainability**
- Grad-CAM visualizations validated that CNNs focused on clinically relevant regions in histopathological images.

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
