# Image Retrieval Using Deep Learning and Graph Theory

This repository contains the **official implementation** of the paper:

> **Image Retrieval Using Deep Learning and Graph Theory**  
> Authors: Arjuwan M. A. Al-Jawadi¹, Ayhan A. K. Al-Shumam²  
> Journal: Kufa Journal of Engineering, 2025–2026

---

## Overview

This repository implements the method proposed in the paper and provides **full reproducibility** of the results.  
All experiments are conducted on a CPU using a **single script (`main.py`)**.  

The repository includes:  
- Implementation of the MLP architecture ([176154-1-7-5-1]) used for image classification.  
- Self-collected Fish–Stationary Image Dataset (FSID).  
- Scripts and instructions to reproduce the results exactly, including random seeds and hardware information.

---

## Environment Setup

- Python ≥ 3.9  
- NumPy  
- Matplotlib  
- H5py  
- PIL (Pillow)  
- SciPy  

Install all dependencies with:

```bash
pip install -r requirements.txt

---


## Fish–Stationary Image Dataset (FSID)

This dataset contains self-collected images used for binary classification
between fish and stationary/background objects.

## Classes
- Fish
- Stationary

## Sample Images

### Fish
![Fish sample 1](dataset/images/fish_001.jpg)
![Fish sample 2](dataset/images/fish_002.jpg)

### Stationary
![Stationary sample 1](dataset/images/stationary_001.jpg)
![Stationary sample 2](dataset/images/stationary_002.jpg)

## Image format
- RGB images (JPG/PNG)

## License
Creative Commons Attribution 4.0 International (CC BY 4.0)

## Owner
© 2026 The Authors

