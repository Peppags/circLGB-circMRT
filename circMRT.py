# -*- coding: utf-8 -*-

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.externals import joblib


def gnb(x_test, dataname):
    gaussiannb_model_path = "weights/" + dataname + "/gnb.m"
    # Load weights for gaussiannb model
    gnb = joblib.load(gaussiannb_model_path)
    # Perform prediction on samples in x_test
    y_pred = gnb.predict(x_test)
    return y_pred

def gbdt(x_test, dataname):
    gbdt_model_path = "weights/" + dataname + "/gbdt.m"
    gbdt = joblib.load(gbdt_model_path)
    y_pred = gbdt.predict(x_test)
    return y_pred

def lgbm(x_test, dataname):
    lgbm_model_path = "weights/" + dataname + "/lgbm.m"
    lgbm = lgb.Booster(model_file=lgbm_model_path)
    y_pred = lgbm.predict(x_test, num_iteration=lgbm.best_iteration)
    return y_pred

def rf(x_test, dataname):
    rf_model_path = "weights/" + dataname + "/rf.m"
    rf = joblib.load(rf_model_path)
    y_pred = rf.predict(x_test)
    return y_pred

def sgd(x_test, dataname):
    sgd_model_path = "weights/" + dataname + "/sgd.m"
    sgd = joblib.load(sgd_model_path)
    y_pred = sgd.predict(x_test)
    return y_pred

def svm_fun(x_test, dataname):
    svm_model_path = "weights/" + dataname + "/svm.m"
    svm = joblib.load(svm_model_path)
    y_pred = svm.predict(x_test)
    return y_pred

def xgboost(x_test, dataname):
    xgboost_model_path = "weights/" + dataname + "/xgb.m"
    xgboost = joblib.load(xgboost_model_path)
    y_pred = xgboost.predict(x_test)
    return y_pred

def merge_model(x_test, name):
    lgbm_pred = lgbm(x_test, name)
    gnb_pred = gnb(x_test, name)
    gbdt_pred = gbdt(x_test, name)
    rf_pred = rf(x_test, name)
    sgd_pred = sgd(x_test, name)
    svm_pred = svm_fun(x_test, name)
    xgboost_pred = xgboost(x_test, name)

    lgbm_pred = pd.DataFrame(list(np.array(lgbm_pred).reshape(-1, 1)))
    gnb_pred = pd.DataFrame(list(np.array(gnb_pred).reshape(-1, 1)))
    gbdt_pred = pd.DataFrame(list(np.array(gbdt_pred).reshape(-1, 1)))
    rf_pred = pd.DataFrame(list(np.array(rf_pred).reshape(-1, 1)))
    sgd_pred = pd.DataFrame(list(np.array(sgd_pred).reshape(-1, 1)))
    svm_pred = pd.DataFrame(list(np.array(svm_pred).reshape(-1, 1)))
    xgboost_pred = pd.DataFrame(list(np.array(xgboost_pred).reshape(-1, 1)))

    results = pd.concat([lgbm_pred, gnb_pred, gbdt_pred, rf_pred, sgd_pred, svm_pred, xgboost_pred], axis=1)
    results = pd.DataFrame(results)
    ensemble_pred = results.apply(lambda x: x.sum(), axis=1)
    ensemble_pred = list(np.array(ensemble_pred).ravel())

    y_pred = []
    for y in ensemble_pred:
        y_pred_t = 1 if y >= 4 else 0
        y_pred.append(y_pred_t)

    label_name = "circRNA-" + name + " interaction"
    predict_labels = ["-", label_name]
    pred_results = []
    for label in y_pred:
        pred_results.append(predict_labels[label])
    pred_results = pd.DataFrame(pred_results)
    return pred_results


if __name__ == '__main__':

    # Loading some example data
    data_path = "features/circMRT/test.csv"
    data = pd.read_csv(data_path)
    data = pd.DataFrame(data)

    x_test = data.drop(['chr', 'start', 'end', 'strand', 'gene', 'type', 'label'], axis=1)
    chr, start, end, strand, gene, y_test = data['chr'], data['start'], data['end'], data['strand'], data['gene'], data['type']

    mi_name = "MI"
    rbp_name = "RBP"
    tr_name = "TR"

    mi_feature_num = 21
    rbp_feature_num = 26
    tr_feature_num = 15

    feature_importance_path = "features/feature_importance/circMRT_feature_rank.csv"
    ranked_features = pd.read_csv(feature_importance_path, usecols=[0, 1, 2])
    ranked_features = np.array(ranked_features)
    mi_rank_fea, rbp_rank_fea, tr_rank_fea = ranked_features[:, 0], ranked_features[:, 1], ranked_features[:, 2]

    mi_rank_fea = list(mi_rank_fea.ravel())
    # Select the important features for circRNA-miRNA interaction classifier
    mi_top_features = mi_rank_fea[0:mi_feature_num]
    mi_x_test = x_test[mi_top_features]

    rbp_rank_fea = list(rbp_rank_fea.ravel())
    rbp_top_features = rbp_rank_fea[0:rbp_feature_num]
    rbp_x_test = x_test[rbp_top_features]

    tr_rank_fea = list(tr_rank_fea.ravel())
    tr_top_features = tr_rank_fea[0:tr_feature_num]
    tr_x_test = x_test[tr_top_features]

    # circRNA-miRNA interaction prediction by circRNA-miRNA classifier
    mi_pred = merge_model(mi_x_test, mi_name)

    # circRNA-RBP interaction prediction by circRNA-RBP classifier
    rbp_pred = merge_model(rbp_x_test, rbp_name)

    # circRNA-TR interaction prediction by circRNA-TR classifier
    tr_pred = merge_model(tr_x_test, tr_name)

    mi_pred = list(np.array(mi_pred).ravel())
    rbp_pred = list(np.array(rbp_pred).ravel())
    tr_pred = list(np.array(tr_pred).ravel())

    # Print circMRT result
    for i in range(len(mi_pred)):
        result = []
        result.append(mi_pred[i])
        result.append(rbp_pred[i])
        result.append(tr_pred[i])
        print(result)




