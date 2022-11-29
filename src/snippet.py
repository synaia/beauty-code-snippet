def get_wine_vars():
    df_wine = pd.read_csv('../../dataset/wine.data', header=None)
    df_wine.columns = ['Class label', 'Alcohol',
                       'Malic acid', 'Ash',
                       'Alcalinity od ash', 'Magnesium',
                       'Total phenols', 'Flavanoids',
                       'Nonflavanoid phenols',
                       'Proanthocyamins',
                       'Color intensity', 'Hue',
                       'OD280/OD315 of diluted wines',
                       'Proline']

    X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)

    stdscaler = StandardScaler()
    X_train_std = stdscaler.fit_transform(X_train)
    X_test_std = stdscaler.transform(X_test)

    return X_train, X_test, y_train, y_test, X_train_std, X_test_std