class Filter:
    def __init__(self, dataset):
        self.dataset = dataset

    # Method 1: Filter by column
    def filter_by_column(self, column, value):
        if column not in self.dataset.columns:
            raise ValueError(f"Column '{column}' does not exist.")

        return self.dataset[self.dataset[column] == value]

    # Method 2: Filter rows with null values
    def filter_null(self, column=None):
        if column is not None:
            if column not in self.dataset.columns:
                raise ValueError(f"Column '{column}' does not exist.")

            return self.dataset[self.dataset[column].isnull()]

        return self.dataset[self.dataset.isnull().any(axis=1)]

    # Method 3: Filter rows without null values
    def filter_not_null(self, column=None):
        if column is not None:
            if column not in self.dataset.columns:
                raise ValueError(f"Column '{column}' does not exist.")

            return self.dataset[self.dataset[column].notnull()]

        return self.dataset[self.dataset.notnull().all(axis=1)]
