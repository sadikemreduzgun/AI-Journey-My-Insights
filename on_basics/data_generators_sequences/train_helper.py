import os, numpy as np, pandas as pd
from tensorflow.keras.utils import Sequence


class ParquetDataGenerator:
    def __init__(self, parquet_dir, batch_size=32, shuffle=True):
        self.parquet_dir = parquet_dir
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.files = [os.path.join(parquet_dir, f) for f in os.listdir(parquet_dir) if f.endswith('.parquet')]
        self._reset()

    def _reset(self):
        self.index = 0
        if self.shuffle:
            import random
            random.shuffle(self.files)

    def _read_data(self, parquet_file):
        return pd.read_parquet(parquet_file)

    def __iter__(self):
        self._reset()
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        batch_files = self.files[self.index:self.index+self.batch_size]
        dfs = [self._read_data(f) for f in batch_files]
        self.index += self.batch_size
        return pd.concat(dfs, ignore_index=True)


class ParquetSequence(Sequence):
    def __init__(self, parquet_dir, batch_size=32, shuffle=True):
        self.parquet_dir = parquet_dir
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.files = [os.path.join(parquet_dir, f) for f in os.listdir(parquet_dir) if f.endswith('.parquet')]
        self.on_epoch_end()

    def __len__(self):
        # number of batches per epoch
        return int(np.ceil(len(self.files) / self.batch_size))

    def __getitem__(self, idx):
        # get a batch of files
        batch_files = self.files[idx * self.batch_size:(idx + 1) * self.batch_size]
        dfs = [pd.read_parquet(f) for f in batch_files]
        batch_df = pd.concat(dfs, ignore_index=True)

        # 🔥 convert to NumPy/tensors for training
        X = batch_df.drop('label', axis=1).to_numpy()
        y = batch_df['label'].to_numpy()
        return X, y

    def on_epoch_end(self):
        # shuffle files after each epoch
        if self.shuffle:
            np.random.shuffle(self.files)


if __name__ == '__main__':
    gen = ParquetDataGenerator('train_dicts_parquet', batch_size=2)

    for batch in gen:
        batch: pd.DataFrame
        print('-----')
        print(batch.shape)  # Each iteration gives you a DataFrame batch
        print(batch.columns)
        #break
