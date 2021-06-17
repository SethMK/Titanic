import os
from dotenv import find_dotenv, load_dotenv
import logging

def extract_data(file_path, file_name):
    '''
    method to pull files
    '''
    os.system("kaggle competitions download -c titanic -p {} -f {}".format(file_path, file_name))

def main():
    '''
    main method
    '''

    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')

    # file_paths
    file_path = '../data/raw'

    # file names
    train = 'train.csv'
    test = 'test.csv'

    extract_data(file_path, train)
    extract_data(file_path, test)
    logger.info('downloaded raw training and test data')

if __name__ == '__main__':
    # getting root directory
    # project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    #call the main
    main()

