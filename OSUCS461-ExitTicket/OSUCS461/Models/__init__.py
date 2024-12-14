from pydantic import BaseModel

class BasePydanticModel(BaseModel):
	class Config:
		from_attributes = False
		validate_assignment = True

class WriteUser(BasePydanticModel):
	name: str

class ReadUser(WriteUser):
	uuid: str
	time_created: int

class WriteUserPost(BasePydanticModel):
	user_uuid: str
	text: str
	post_9char: str

class ReadUserPost(WriteUserPost):
	uuid: str
	time_created: int