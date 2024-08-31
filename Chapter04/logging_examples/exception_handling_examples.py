import logging
import pandas as pd

logging.basicConfig(filename='exception_handling.log',
                    level=logging.DEBUG,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

def process(data_to_be_processed):
    '''Dummy example that returns original data plus 1'''
    logging.info("Data processed!") 
    return data_to_be_processed + 1

def process_data01(data): 
    try: 
        # Do some processing on the data 
        result = process(data) 
    except Exception as e: 
        # Log the exception 
        logging.exception("Exception occurred while processing data") 

        # Re-raise the exception with a new exception
        new_exception = ValueError("Error processing data") 
        raise new_exception from e

    return result

# df = pd.DataFrame(['1'])
# process_data01(df)

def process_data02(data): 
    try: 
        # Do some processing on the data 
        result = process(data) 
    except Exception as e: 
        # Log the exception 
        message = f"Exception ocurres while processing data: {data}"

        raise Exception(message) from e

    return result

# df = pd.DataFrame([1,'2',3])
# process_data02(df)


def process_data03(
        data): 
    try: 
        # Do some processing on the data 
        result = process(data) 
    except Exception as e: 
        # Log the exception 
        message = f"Exception ocurres while processing data: {data}"

        raise Exception(message) from e

    return result

df = pd.DataFrame([1,'2',3])
process_data02(df)
