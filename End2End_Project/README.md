This folder contains the end-to-end model building process. This is designed to be a standalone folder that can be downloaded to run independently of the GitHub repository. That means it has its own Setup, Functions, and requirements files cleaned for artifacts that aren't used in the notebook. 

The workflow here is to pull in the original dataset, apply data cleaning methods and get the data in working shape for the ARIMA model. We apply sector-level scalers, which is also stored in this folder. Then, predictions on the best performing ARIMA model for each sector/field office are saved and used to generate the MAPE values for 6 time steps. Once these are plotted, it can be used for identifying model failures and performance issues. 

In addition, there are two folders within the Model_Outputs that correspond to the full time series and a zoomed-in version on the most recent 24 months. These can be used to view predictions on each sector/field office of interest.

Finally, each ARIMA model trained on individual sectors has been saved as pickle files into a folder called saved_models. This allows for each model to be tuned independently from others if forecasting performance is deemed to be weak. The last code cell in the notebook allows users to reload models from pickle format for any finetuning/retraining purposes. 

