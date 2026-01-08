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
