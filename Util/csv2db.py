import codecs, configparser, csv, glob, logging, os, sys, time, datetime, sqlite3

class csv2db:
    def __init__(self):
        self.errors = []

        # load config file
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        # get logger
        self.logger = logging.getLogger('csv2db_logger')
        self.logger.setLevel(logging.DEBUG)

        # set handler
        dateTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        logFileName = os.path.join(self.config['Log']['path'], dateTime + "_csv2db.log")
        fileHandler = logging.FileHandler(logFileName)
        streamHandler = logging.StreamHandler()

        # set log fomatter
        fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
        fileHandler.setFormatter(fomatter)
        streamHandler.setFormatter(fomatter)

        # attach log handler
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(streamHandler)

    # conver csv to database
    def convert(self):
        # initalize
        self.errors = []
        db = self.config['DB']['path']
        conn = sqlite3.connect(db)
        conn.text_factory = str  # allows utf-8 data to be stored
        cur = conn.cursor()

        # traverse the directory and process each .csv file
        csvDir = self.config['ExternalDatas']['path']
        for csvfile in glob.glob(os.path.join(csvDir, "*.csv")):
            # remove the path and extension and use what's left as a table name
            tablename = os.path.splitext(os.path.basename(csvfile))[0]

            for encoding in ['utf-8', 'euc-kr', 'cp949', 'utf-16-le', 'utf-16', 'utf-16-be']:
                with codecs.open(csvfile, "r",  encoding=encoding) as f:
                    reader = csv.reader(f)
                    # check file encoding
                    try:
                        reader = list(reader)
                    except:
                        #self.errors.append('Encoding Error(%s) : %s' % (encoding, csvfile))
                        continue

                    # open file
                    self.logger.info("Open %s file(%s)" % (csvfile, encoding))

                    if reader and len(reader) > 0:
                        header = reader[0]
                        # drop old table
                        sql = "DROP TABLE IF EXISTS %s" % tablename
                        cur.execute(sql)

                        # add quote for near 'GROUP' syntax error
                        header = ["'" + i + "'" for i in header]
                        columnCount = len(header)

                        # create table sql command, if id field not in table then make it.
                        if not any(['id' == column.lower() for column in header]):
                            sql = "CREATE TABLE %s (%s)" % (tablename, 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' + ", ".join(
                                ["%s" % column for column in header]))
                        else:
                            sql = "CREATE TABLE %s (%s)" % (tablename, ", ".join(["%s" % column for column in header]))
                        cur.execute(sql)

                        # insert sql command
                        sql = "INSERT INTO %s (%s) VALUES (%s)" % (tablename, ", ".join(header), ", ".join(["?" for i in header]))

                        # insert values - ignore header
                        for i, row in enumerate(reader[1:]):
                            if len(row) < columnCount:
                                errorMsg = "%s : not matched row item count. %d line" % (tablename, i+2)
                                self.logger.warning("-" * 50)
                                self.logger.warning(errorMsg)
                                self.logger.warning("%s" % header)
                                self.logger.warning("%s" % row)
                                self.errors.append(errorMsg)
                                continue
                            cur.execute(sql, row[:columnCount])

                        # commit
                        conn.commit()
                        break
                    else:
                        self.logger.warning("%s file error" % csvfile)
                        self.errors.append("%s file error" % csvfile)
            # not found encoding
            else:
                self.logger.warning("not found encoding. %s" % csvfile)
                self.errors.append("not found encoding. %s" % csvfile)
        cur.close()
        conn.close()
        self.logger.info("Done.\n")
        self.logger.info("-" * 50)
        self.logger.info("%d error(s)." % len(self.errors))
        for error in self.errors:
            self.logger.warning(error)


# run
if __name__ == '__main__':
    csvToDB = csv2db()
    csvToDB.convert()