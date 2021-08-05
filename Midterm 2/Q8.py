import mysql.connector

class BankDB:
    """Application for an banking database on MySQL"""

    def connect(self):
        """Makes a connection to the database and returns connection to caller"""
        try:
            # TODO: Fill in your connection information
            print("Connecting to database.")
            self.cnx = mysql.connector.connect(
                user='cosc304', password='cosc304', host='68.183.198.25', database='workson')
            return self.cnx
        except mysql.connector.Error as err:
            print(err)

    def loanAmounts(self, bankName):
        
        query = f'SELECT amount FROM Loan WHERE bankName = "{bankName}" ORDER BY amount desc LIMIT 5;'
       
        try:
            cursor = self.cnx.cursor()
            print(query)            
            cursor.execute(query)
            
            for(amount) in cursor:
                print(amount[0], end='')
            cursor.close()
            return

        except mysql.connector.Error as err:
            print(err)
            return


    def largestLoans(self):
    #         """Return the largest loans"""
        query1 = 'SELECT bankName, count(amount) as numLoans, sum(amount) as totalLoans FROM Loan GROUP BY bankName;'
        
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query1)
            
            for(bankName, numLoans, totalLoans) in cursor:
                print(f'Bank: {bankName} Loans: {numLoans} Total: {totalLoans}')
                print ("Top 5 Loans: \n") 
                result = bankDB.loanAmounts(bankName)
                print(result)
            cursor.close()
            return

        except mysql.connector.Error as err:
            print(err)
            return


    def close(self):
        try:
            print("Closing database connection.")
            self.cnx.close()
        except mysql.connector.Error as err:
            print(err)

    def resultSetToString(self, cursor, maxrows):
        output = ""
        cols = cursor.column_names
        output += "Total columns: "+str(len(cols))+"\n"
        output += str(cols[0])
        for i in range(1, len(cols)):
            output += ", "+str(cols[i])
        for row in cursor:
            output += "\n"+str(row[0])
            for i in range(1, len(cols)):
                output += ", "+str(row[i])
        output += "\nTotal results: "+str(cursor.rowcount)
        return output



bankDB = BankDB()
bankDB.connect()

bankDB.largestLoans()
print("\n")

bankDB.close()
