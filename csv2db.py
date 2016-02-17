import sqlite3
import csv
import os
import glob
import logging

# get logger
logger = logging.getLogger('csv2db_logger')
logger.setLevel(logging.DEBUG)

# remove old log file
logFileName = os.path.splitext(os.path.basename(__file__))[0] + ".log"
if os.path.exists(logFileName):
    os.remove(logFileName)

# set handler
fileHandler = logging.FileHandler(logFileName)
streamHandler = logging.StreamHandler()

# set log fomatter
fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
fileHandler.setFormatter(fomatter)
streamHandler.setFormatter(fomatter)

# attach log handler
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)


# conver csv to database
def csv2db():
    # initalize
    db = "db.sqlite3"
    conn = sqlite3.connect(db)
    conn.text_factory = str  # allows utf-8 data to be stored
    cur = conn.cursor()

    # traverse the directory and process each .csv file
    for csvfile in glob.glob(os.path.join("csv", "*.csv")):
        # remove the path and extension and use what's left as a table name
        tablename = os.path.splitext(os.path.basename(csvfile))[0]

        logger.info("Open %s file" % csvfile)

        with open(csvfile, "r") as f:
            reader = csv.reader(f)
            reader = list(reader)
            if reader and len(reader) > 0:
                header = reader[0]
                # drop old table
                sql = "DROP TABLE IF EXISTS %s" % tablename
                cur.execute(sql)

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
                for row in reader[1:]:
                    cur.execute(sql, row)

                # commit
                conn.commit()
            else:
                logger.warning("error")
    cur.close()
    conn.close()
    logger.info("end")

# run
if __name__ == '__main__':
    csv2db()
