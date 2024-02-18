import shutil
shutil.copyfile('house_prices/train.csv', 'data/raw/train.csv')
shutil.copyfile('house_prices/train.csv', 'data/processed/train_house_prices.csv')
shutil.copyfile('house_prices/train.csv', 'data/processed/test_house_prices.csv')

