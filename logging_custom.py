import logging

# incase of providing extradata to logging format
extraData = {
    'user': 'bilalsaeed'
}


def deleteItem():
    logging.info('Deleting something...', extra=extraData)


def main():

    # to format our custom log messages
    # asctime = log creation time
    # levelname = logging level e.g debug, info etc.
    # user is extra data provided when logging along with log message
    fmtstr = '%(user)s %(asctime)s: %(levelname)s: %(filename)s: %(funcName)s(): %(lineno)d: %(message)s'

    # to format custom datetime in loggin
    datestr = '%m/%d/%Y %I:%M:%S %p'

    logging.basicConfig(level=logging.DEBUG,
                        filename='output_custom.log',
                        filemode='w',
                        format=fmtstr,
                        datefmt=datestr)

    logging.debug('this is a debug message', extra=extraData)
    logging.info('this is a info message', extra=extraData)
    logging.warning('this is a warning message', extra=extraData)
    logging.error('this is a error message', extra=extraData)
    logging.critical('this is a critical message', extra=extraData)

    deleteItem()


if __name__ == '__main__':
    main()
