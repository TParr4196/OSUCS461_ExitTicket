from OSUCS461.Classes.Database import DB
from OSUCS461.Models import WriteUser, ReadUser
from OSUCS461.Utilities import createHash, nowSeconds

class User:
    table = "user"

    @staticmethod
    def create(user: WriteUser) -> str:
        uuid = createHash(User.table)
        return DB.Add(User.table, data={"uuid": uuid, "name": user.name, "time_created": nowSeconds()})["uuid"]
    
    @staticmethod
    def get(uuid: str) -> ReadUser:
        user = DB.GetBy(User.table, field_params={"uuid": uuid})
        result = ReadUser(**user)
        return result

    @staticmethod
    def update(uuid: str, name: str):
        DB.Update( User.table, data={"name": name}, field_params={"uuid": uuid})
        user = DB.GetBy(User.table, field_params={"uuid": uuid})
        result = ReadUser(**user)
        return result

    @staticmethod
    def delete(uuid: str) -> ReadUser:
        status = DB.DeleteWhere(User.table, field_params={"uuid": uuid})
        return status

    @staticmethod
    def getall():
        return DB.GetAll(User.table)