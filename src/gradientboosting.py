import time
from sklearn.compose import make_column_selector as selector
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OrdinalEncoder

from evaluation import EvaluationReport

def gradientBoost(df):
    print("="*20)
    print("You have selected gradient boost model.")
    print("Now Commencing Pipeline Transformation")
    print("="*20)
    time.sleep(10)

    target_name = "Survive"
    target = df[target_name]
    dataset = df.drop(columns=[target_name,"ID"])

    numerical_columns_selector = selector(dtype_exclude=object)
    categorical_columns_selector = selector(dtype_include=object)

    numerical_columns = numerical_columns_selector(dataset)
    categorical_columns = categorical_columns_selector(dataset)

    print("="*20)
    print("Pipeline has been configured - Data has been encoded and Transformed")
    print("="*20)
    time.sleep(10)

    data_train, data_test, target_train, target_test = train_test_split(dataset, target, random_state=42)
    
    categorical_preprocessor = OrdinalEncoder(handle_unknown="use_encoded_value",unknown_value=-1)

    preprocessor = ColumnTransformer([
        ('categorical', categorical_preprocessor, categorical_columns)],
        remainder="passthrough")

    model = make_pipeline(preprocessor, GradientBoostingClassifier())
    print("="*20)
    print("Now Commencing Model Fitting")
    print("="*20)
    time.sleep(10)

    model = model.fit(data_train, target_train)
    
    EvaluationReport(model,target,dataset,data_test,target_test)

