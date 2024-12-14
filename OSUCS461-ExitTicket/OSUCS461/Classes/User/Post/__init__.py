from OSUCS461.Classes.Database import DB
from OSUCS461.Models import WriteUserPost, ReadUserPost
from OSUCS461.Utilities import createHash, nowSeconds


class Post:
    table = "user_post"

    @staticmethod
    def create(post: WriteUserPost) -> str:
        uuid = createHash(Post.table)
        return DB.Add(Post.table, data={"uuid": uuid, "user_uuid": post.user_uuid, "post_9char": post.post_9char, "text": post.text, "time_created": nowSeconds()})["uuid"]
    
    @staticmethod
    def get(uuid: str) -> ReadUserPost:
        user = DB.GetBy(Post.table, field_params={"uuid": uuid})
        result = ReadUserPost(**user)
        return result

'''

`uuid` varchar(65) NOT NULL,
  `user_uuid` varchar(56) DEFAULT NULL,
  `post_9char` varchar(9) DEFAULT NULL,
  `text` longtext DEFAULT NULL,
  `time_created` int(11) DEFAULT NULL,
class WriteUserPost(BasePydanticModel):
	text: str

class ReadUserPost(BasePydanticModel):
	uuid: str
	user_uuid: str
	post_9char: str
	time_created: int
'''