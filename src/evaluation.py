from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score

def EvaluationReport(model,target,dataset,data_test,target_test):
    print("="*20)
    print("Now Proceeding to Evaluation Metrics")
    print("="*20)
    flag = False
    while flag is False:
        choice = input("Choose 0 for Classification Report, Choose 1 for Confusion Matrix, Choose 2 for ROC Statistics, press q to quit")
        if choice == '0':
            print(classification_report(target,model.predict(dataset)))
        elif choice == '1':
            cm = confusion_matrix(target, model.predict(dataset), labels=model.classes_)
            print("Confusion Matrix:",cm)
            print("True Positive Rate (%):" ,(int(cm[0][0])/(int(cm[0][0])+int(cm[0][1]))*100 ))
            print("True Negative Rate (%):" ,(int(cm[1][1])/(int(cm[1][0])+int(cm[1][1]))*100 ))

        elif choice =='2':
            try:
                print("ROC Area Under Curve Score is:",roc_auc_score(target, model.decision_function(dataset)))
            except AttributeError:
                print("This model does not have Receiver Operating Characterisitcs, select another metric.")
        elif choice == 'q':
            flag = True
        else:print("Your choice is not valid, please select again")