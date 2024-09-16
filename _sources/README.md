# Uplift Modeling for Marketing Personalization in Practice

This is a repository of the [uplift modeling tutorial](https://amsterdam2024.pydata.org/cfp/talk/3VJUMJ/) lectured at [PyData Conference Amsterdam 2024](https://amsterdam.pydata.org/program/).
Uplift modeling is a cutting-edge approach that goes beyond traditional predictive modeling by estimating the causal effects of treatments on individuals. This makes it the go-to framework for personalized marketing, customer retention, and beyond. Our tutorial is designed to provide you with a practical understanding of uplift modeling, complete with real-world Python examples. 

## 1. What You'll Learn

- **Foundations of Uplift Modeling:** Get a concise overview of uplift modeling and why it matters.
- **State-of-the-Art Methods:** Discover the latest techniques for estimating Conditional Average Treatment Effects (CATE) to optimize budget constraints.
- **Python Implementation:** Learn to train, evaluate, and deploy uplift models using Python.
- **Overcoming Production Challenges:** Explore strategies for ensuring model robustness, adaptiveness, and explainability in real-world applications.

## 2. What We Expect You to Know

- Basic knowledge of probability, statistics, and machine learning.
- Familiarity with Python programming is required.

## 3. Tutorial Setup

### Option 1 - Google Colab (preferred)

- Navigate to [Google Colab](https://colab.google/)
- Click on `Open Colab` in the middle of the screen
- Click on the `Github` tab
- Paste the link to this repo: `https://github.com/bookingcom/uplift-modeling-for-marketing-personalization-tutorial`
- Among the notebooks available, select the one that you want to run
- Once prompted to the notebook, you can execute it as usual from the colab environment

### Option 2 - Local Setup

#### 1. Clone This Repo Locally

From the cli:

```git clone https://github.com/bookingcom/uplift-modeling-for-marketing-personalization-tutorial```

And cd into the repo:

```cd uplift-modeling-for-marketing-personalization-tutorial```

#### 2. Env. Setup

**The current setup has been tested with python 3.9**

Two possible ways for setting up your local environment are:

##### 1. Without Virtualenv

Install the requirements in your current env:

`pip install -r tutorial/requirements-local.txt`

##### 2. With Virtualenv

Install a virtual env:

`python -m venv .venv`

Activate the virtual env:

`source .venv/bin/activate`

Install the requirements (from the repo root directory):

`pip install -r tutorial/requirements-local.txt`

#### 3. Start Jupyter

From your cli, by running `jupyter-lab` or `jupyter-notebook`

## 4. Outline

1. **Introduction to Uplift Modeling**
   - **Why Uplift Modeling?** Understand the significance and potential impact.
   - **Key Concepts:** Dive into Conditional Average Treatment Effects (CATE) and treatment response.

2. **Foundation Methods for Uplift Modeling**
   - **Overview of Current Techniques:** Learn about the latest methods used to estimate CATE and how they can be applied to optimize budget constraints.
   - **Training Uplift Models:** Step-by-step coding examples to build your models.
   - **Evaluating Uplift Models:** Explore metrics and methodologies to assess model performance.

3. **E-commerce Tailored Methods in Revenue Uplift Modeling**
    - **Introduction to Incremental Profit per Conversion Transformation:** Implement and interpret results.

4. **Explainability and Trust**
   - **How to Convey Trust in Your Model**: strategies

5. **Challenges in production**
   - **Model Robustness and Adpativeness:** How to ensure your models remain effective over time.
   - **Operational Challenges:** Learn about common operational challenges and how to tackle them.

6. **Other Resources**
   - **Python Packages** : Discussion CausalML, EcoML, DoWhy, UpliftML, etc, packages.
   - **Papers, Tutorials, and Books** : Foundation Papers, and Books in the field.

## 5. Who We are

We are a part of the Smart Benefits ML team at Booking.com, focusing on delivering cutting-edge personalized discounts while navigating the complexities of budget constraints. Our expertise spans various domains of machine learning, from causal inference to MLOps for causal machine learning, ensuring we provide impactful solutions for millions of customers worldwide.


- **Felipe Moraes** is a Machine Learning Scientist. He holds a PhD in Computer Science from Delft University of Technology. In the past, he worked at Amazon Alexa Shopping and research labs at NYU and the University of Quebec, Felipe brings a rich background in recommendation systems and applied machine learning.

- **Hugo Manuel Proença** is a Senior Machine Learning Scientist. Hugo holds a PhD from Leiden University, where he collaborated with GE Aviation, and has industry experience at Huawei AI Labs and Silo AI, making him well-versed in both academic and industrial applications of machine learning.

- **Matteo Romeo** is a Machine Learning Engineer. He holds a Master’s degree in Data and Machine Learning from Politecnico di Milano. Prior to joining Booking.com, he worked on user experience personalization at DAZN and advised clients as an ML consultant. He brings an engineering perspective to building robust and scalable machine learning solutions.

## 6. Acknowledgements

These materials were originally developed at Booking.com. With approval from Booking.com, these materials was released as open source, for which the authors would like to express their gratitude, and to Alina Solovjova, Itsik Adiv, and Ulf Schnabel for their time reviewing these materials.
