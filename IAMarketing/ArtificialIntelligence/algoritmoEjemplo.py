import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import zipfile
import cv2
import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.keras import layers, optimizers
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import (Input, Add, Dense, Activation,
ZeroPadding2D, BatchNormalization, Flatten, Conv2D,
AveragePooling2D, MaxPooling2D, Dropout)
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.initializers import glorot_uniform
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import (ReduceLROnPlateau,
EarlyStopping, ModelCheckpoint, LearningRateScheduler)
from IPython.display import display
from tensorflow.keras import backend as K
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import plotly.graph_objects as go
import matplotlib 
import os

def showDataSet():
    sales_df = pd.read_csv('../DataSet/sales_data_sample.csv', sep=',', decimal='.', encoding = "ISO-8859-1")
    sales_df = sales_df.drop(['ADDRESSLINE1', 'ADDRESSLINE2', 'POSTALCODE', 'CITY',
    'TERRITORY', 'PHONE', 'STATE', 'CONTACTFIRSTNAME','CONTACTLASTNAME', 'CUSTOMERNAME', 
    'ORDERNUMBER', 'STATUS', 'ORDERDATE', 'QTR_ID'], axis=1)
    return sales_df

def importDataSet():
    sales_df = pd.read_csv('../DataSet/sales_data_sample.csv', sep=',', decimal='.', encoding = "ISO-8859-1")
    sales_df = sales_df.drop(['ADDRESSLINE1', 'ADDRESSLINE2', 'POSTALCODE', 'CITY',
    'TERRITORY', 'PHONE', 'STATE', 'CONTACTFIRSTNAME','CONTACTLASTNAME', 'CUSTOMERNAME', 
    'ORDERNUMBER', 'STATUS', 'ORDERDATE', 'QTR_ID'], axis=1)

    def dummies(x):
        dummy = pd.get_dummies(sales_df[x])
        sales_df.drop(columns = x , inplace = True)
        return pd.concat([sales_df, dummy], axis = 1)

    sales_df = dummies("COUNTRY")
    sales_df = dummies("PRODUCTLINE")
    sales_df = dummies("DEALSIZE")
    sales_df['PRODUCTCODE'] = pd.Categorical(sales_df['PRODUCTCODE']).codes

    return sales_df

def getScaledData():
    sales_df = pd.read_csv('../DataSet/sales_data_sample.csv', sep=',', decimal='.', encoding = "ISO-8859-1")
    sales_df = sales_df.drop(['ADDRESSLINE1', 'ADDRESSLINE2', 'POSTALCODE', 'CITY',
    'TERRITORY', 'PHONE', 'STATE', 'CONTACTFIRSTNAME','CONTACTLASTNAME', 'CUSTOMERNAME', 
    'ORDERNUMBER', 'STATUS', 'ORDERDATE', 'QTR_ID'], axis=1)

    def dummies(x):
        dummy = pd.get_dummies(sales_df[x])
        sales_df.drop(columns = x , inplace = True)
        return pd.concat([sales_df, dummy], axis = 1)

    sales_df = dummies("COUNTRY")
    sales_df = dummies("PRODUCTLINE")
    sales_df = dummies("DEALSIZE")
    sales_df['PRODUCTCODE'] = pd.Categorical(sales_df['PRODUCTCODE']).codes
    scaler = StandardScaler()
    sales_df_scaled = scaler.fit_transform(sales_df)
    return sales_df_scaled

def createGraphic():
    sales_df_scaled = getScaledData()
    kmeans = KMeans(5)
    kmeans.fit(sales_df_scaled)
    labels = kmeans.labels_
    pca = PCA(n_components = 2)
    principal_comp = pca.fit_transform(sales_df_scaled)
    pca_df = pd.DataFrame(data = principal_comp, columns = ['pca1', 'pca2'])
    pca_df = pd.concat([pca_df, pd.DataFrame({'cluster':labels})], axis = 1)
    ax = sns.scatterplot(x = "pca1", y = "pca2", hue = "cluster", data = pca_df, palette = ["red", "green", "blue",
    "pink", "yellow"])
    imgName = "IAApp/static/Graphic.png"
    plt.savefig(imgName)
    plt.close()

def createCorrMatrix():
    df = importDataSet()
    sales_df_simplyfied = df[["QUANTITYORDERED", "PRICEEACH", "ORDERLINENUMBER", "SALES", "MONTH_ID", "YEAR_ID", "MSRP", "PRODUCTCODE"]]
    corr_df = sales_df_simplyfied.corr(method='pearson')
    corr_df.style.background_gradient(cmap='coolwarm')
    #return corr_df.to_html()
    return "Hola putos"

