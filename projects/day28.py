import streamlit as st

def app():
    st.title('Day #28')
    st.subheader('Optuna - Auto Hyperparameter Tuning WebApp')
    st.markdown('''
        This app is a demo of Optuna - Auto Hyperparameter Tuning.
                
        Reference: [Optuna Docs](https://optuna.org/)
    ''')
    st.write('---')

    st.subheader('Install Optuna')
    st.code('!pip install optuna')

    st.subheader('Import Libraries')
    st.code('''
        import optuna
    ''')

    st.subheader('Define Objective Function: XGBoostClassifier')
    st.code('''
        def objective(trial):
            # Load Data
            X, y = load_data()
            
            # Define Parameters
            param = {
                'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
                'max_depth': trial.suggest_int('max_depth', 3, 10),
                'learning_rate': trial.suggest_float('learning_rate', 0.001, 0.1),
                'subsample': trial.suggest_float('subsample', 0.5, 1.0),
                'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
                'gamma': trial.suggest_float('gamma', 0.0, 0.5),
                'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
                'reg_alpha': trial.suggest_float('reg_alpha', 0.0, 1.0),
                'reg_lambda': trial.suggest_float('reg_lambda', 0.0, 1.0),
                'random_state': 42,
                'n_jobs': -1
            }
            
            # Model
            model = XGBClassifier(**param)
            
            # Cross Validation
            cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
            score = cross_val_score(model, X, y, cv=cv, scoring='roc_auc').mean()
            
            return score
    ''')

    st.subheader('Run Study')
    st.code('''
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=100)
    ''')

    st.subheader('Best Hyperparameters')
    st.code('''
        study.best_params
    ''')

    st.subheader('Best Score')
    st.code('''
        study.best_value
    ''')

    st.subheader('Plot Optimization History')
    st.code('''
        optuna.visualization.plot_optimization_history(study)
    ''')
    