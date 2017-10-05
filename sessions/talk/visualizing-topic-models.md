title: "Visualizing Topic Models"
subtitle: ""
speaker: parul-sethi
track: pydata
video:
---
Topic Modelling is a great way to infer topics in a large corpus of text documents but analyzing them could become difficult without any visualization. The purpose of this talk is to introduce the visualizations that aids the process of training topic models and analyze their results  for downstream NLP applications. I’ll give a brief introduction to Topic Models before moving to visualizations.

I’ll demonstrate the steps to train LDA model in gensim and create the following visualizations using the trained model and how to interpret them:

1. LDA Training visualization: Monitoring the LDA model training using Visdom integration in gensim

2. pyLDAvis: Topic interpretation using the relevance metric effectively

3. Topic Networks: Discover connections between topics 

3. Topic difference visualization: Determine exact distances between every topic pair along with their intersection/difference of terms

4. Dendrogram (with extended heatmap): Topic clustering with a deeper insight into the inter-topic semantic validity

5. LDA Projections: Document clustering using tensorboard based on the topic representation of documents

The interface for this talk would be Jupyter notebook containing the LDA training and visualizations code.