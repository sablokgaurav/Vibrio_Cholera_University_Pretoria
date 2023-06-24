   def vibrioLazyPredictClassification(self,input_path_train, input_path_test, X, y, 
                                          column:str,random_state: int):
        self.input_path_train = input_path_train
        self.train = pd.read_csv(self.input_path_train)
        self.input_path_test = input_path_test
        self.test = pd.read_csv(self.input_path_test)
        self.X = self.train.drop(column, axis=1)
        self.y = self.test[column]
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.random_state = random
        self.X_train, self.X_test, self.y_train, self.y_test =
        train_test_split(self.X, self.y, test_size=.5, random_state=self.random_state)
        estimate = LazyClassifier(
            verbose=0, ignore_warnings=True, custom_metric=None)
        models, predictions = estimate.fit
        self.X_train, self.X_test, self.y_train, self.y_test)
        compare_report = sweetviz.compare(
            [self.X_train, self.X], [self.X_test, self.y])
        compare_report.show_html('self.data.html', open_browser=True)
        compare_report.show_notebook()
        print(f'the_models_evaluated_are:{models}')
        return models

    def vibrioLazyPredictRegression(self,input_path_train, input_path_test, X, y, 
                                          column:str,random_state: int):
        self.X = self.train.drop(column, axis=1)
        self.y = self.test[str(column)]
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.X_train, self.X_test, self.y_train, self.y_test =
        train_test_split(self.X, self.y, test_size=.5, self.random_state=random)
        estimate = LazyRegressor(
            verbose=0, ignore_warnings=True, custom_metric=None)
        models, predictions = estimate.fit(
            self.X_train, self.X_test, self.y_train, self.y_test)
        compare_report = sweetviz.compare(
            [self.X_train, self.X], [self.X_test, self.y])
        compare_report.show_html('self.data.html', open_browser=True)
        compare_report.show_notebook()
        return models
        