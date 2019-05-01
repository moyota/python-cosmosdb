from cosmosdb.cosmosdb import DatabaseConnection
from cosmosdb.cosmosdb import getItem, getReplacedItem

if __name__ == "__main__":
    print("---")
    dbConnection = DatabaseConnection()

    print(dbConnection.initialize_database())
    print(dbConnection.initialize_container())

    dbConnection.create_item(getItem("1"))
    dbConnection.create_item(getItem("2"))
    dbConnection.create_item(getItem("3"))
    dbConnection.upsert_item(getReplacedItem("3"))
    dbConnection.upsert_item(getReplacedItem("4"))
    dbConnection.delete_item(getItem("2"))

    print("---")
    itemList = dbConnection.read_items()
    for item in itemList:
        print(item)
