import pandas as pd
pd.options.display.float_format = '{:,2f}'.format
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import pmdarima as pm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.stats.diagnostic import het_arch 
import statsmodels.api as sm
#from arch import arch_model

warnings.filterwarnings("ignore")


def white_noise(mu=0, sigma=1, size=100):
    s = np.random.normal(mu, sigma, size=size)
    array = sns.histplot(s, bins=40, kde=True)


def process_ar(time, a_0, a_1, y_inicial):
    y = y_inicial
    s = []
    for i in np.arange(time):
        if(i == 1):
            s.append(y)
        if(i > 1):
            y = a_0 + a_1 * y + np.random.randn()
            s.append(y)
    s = pd.Series(s)
    return s.plot()

def plotACFandPACF(data, lags= 20):
    fig, (ax1, ax2) = plt.subplots(1,2, figsize= (16,5))
    fig = sm.graphics.tsa.plot_acf(data, lags=lags, ax=ax1)
    ax1.axhline(y=-1.96/np.sqrt(len(data)), linestyle='--', color='gray')
    ax1.axhline(y=-.96/np.sqrt(len(data)), linestyle='--', color='gray')
    ax1.set_xlim(0.5, lags)
    ax1.set_xlabel('Lags')
    lim_inf = -sm.tsa.stattools.acf(data)[1:].max() - 0.1
    lim_sup = sm.tsa.stattools.acf(data)[1:].max() + 0.1
    ax1.set_ylim(lim_inf, lim_sup)

    fig = sm.graphics.tsa.plot_pacf(data, lags=lags, ax=ax2)

    ax2.axhline(y=-1.96/np.sqrt(len(data)), linestyle='--', color='gray')
    ax2.axhline(y=-.96/np.sqrt(len(data)), linestyle='--', color='gray')
    ax2.set_xlim(0.5, lags)
    ax2.set_xlabel('Lags')
    lim_inf = -sm.tsa.stattools.acf(data)[1:].max() - 0.1
    lim_sup = sm.tsa.stattools.acf(data)[1:].max() + 0.1
    ax2.set_ylim(lim_inf, lim_sup)
    ax2.set_xlabel('Lags')


def regressionArima(data, ar=1,i=0,ma=1, trend='c'):
    mod = ARIMA(data.dropna(), order=(ar,i,ma), trend=trend)
    res = mod.fit()
    print(res.summary())
    print(res.params)


def adf_test(x, regression='c'):
    index = ['Test Statistic', 'p-value', '# of Lags Used', ' # of Observations Used']
    adf_test = adfuller(x, autolag='AIC', regression=regression)
    results = pd.Series(adf_test[0:4], index=index)
    for key, value in adf_test[4].items():
        results[f'Critical value ({key})'] = value
    if(adf_test[4:5][0]['5%'] > adf_test[0]):
        print("It is stationary")
    else:
        print("It is NOT stationary")
    return results


def best_model(data, intercept=True):
    model = pm.auto_arima(data,
            error_action= 'ignore',
            suppres_warnings=True,
            seasonal=False,
            stepwise=False,
            approximation=False,
            n_jobs=-1,
            with_intercept=intercept)
    print(model.sumary())


