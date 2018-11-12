import logging


def main():

    logging.basicConfig(level=logging.DEBUG,
                        filename='output.log', filemode='w')

    logging.debug("This is a debug log message")
    logging.info('This is a info log message')
    logging.warning('This is a warning log message')
    logging.error('This is a error log message')
    logging.critical('This is a critical log message')

    # can also provide formatted string
    logging.info('{} variable is empty'.format('temp'))


if __name__ == '__main__':
    main()
