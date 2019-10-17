# -*- coding: utf-8 -*-

import lightgbm as lgb
import numpy as np
import pandas as pd


if __name__ == '__main__':
    # Loading some example data
    data_path = "features/circLGB/test.csv"
    data = pd.read_csv(data_path)
    data = pd.DataFrame(data)

    # Select the important features for circLGB classifier
    rank_feature_path = "features/feature_importance/circLGB_feature_rank.csv"
    rank_feature = np.array(pd.read_csv(rank_feature_path, usecols=[2]))
    rank_feature = list(rank_feature.ravel())
    select_feature = rank_feature[0:54]

    x_test = data[select_feature]
    y_test = data["class_label"].ravel()

    # Load weights for the model
    circlgb_model = lgb.Booster(model_file='weights/circLGB.txt')

    # Prediction the classification of the given sequences in x_test
    y_predict_result = circlgb_model.predict(x_test, num_iteration=circlgb_model.best_iteration)
    
    y_predict = []
    threshold = 0.5
    for pred in y_predict_result:
        result = 1 if pred > threshold else 0
        y_predict.append(result)

    labels = ["lncRNA", "circRNA"]

    y_pred = []
    y_true = []
    for label in y_test:
        y_true.append(labels[label])
    print("The types of the query sequences:")
    print(y_true)

    for label in y_predict:
        y_pred.append(labels[label])
    print("\ncircLGB predicted results:")
    print(y_pred)

    y_true = pd.DataFrame(y_true)
    y_pred = pd.DataFrame(y_pred)

    result_path = "result/circLGB_test_result.csv"
    result = pd.concat([y_true, y_pred], axis=1)
    result.to_csv(result_path, index=True, sep=',', header=['y_true', 'y_pred'])




