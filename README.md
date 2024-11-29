### Revolutionising Histopathology with AI: Advanced Deep Learning for Breast Cancer Diagnosis

This project leverages cutting-edge deep learning (DL) models like ResNet, DenseNet, and EfficientNet to classify histopathology images into benign or malignant categories. By addressing class imbalance, model interpretability, and feature space analysis, it aims to deliver reliable AI solutions for breast cancer diagnosis.

#### Features
- **Pre-processing Pipelines**: Standardises histopathology images for model training.
- **Advanced Architectures**: Includes ResNet, DenseNet, and EfficientNet implementations.
- **Model Interpretability**: Visualisations using Grad-CAM.
- **Class Balancing**: Handles imbalanced datasets with techniques like weighted loss functions.
- **Performance Metrics**: Evaluates using precision, recall, F1-score, and AUC-ROC.

#### Installation
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
