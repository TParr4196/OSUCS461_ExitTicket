from fastapi import APIRouter, HTTPException
from starlette.responses import PlainTextResponse, RedirectResponse
from OSUCS461.Models import WriteUser, ReadUser, WriteUserPost, ReadUserPost
from OSUCS461.Utilities.CustomLogger import custom_logger
from OSUCS461.Classes.User import User
from OSUCS461.Classes.User.Post import Post

router = APIRouter()
logger = custom_logger('fastAPI', 'fastapi_logs.log')

@router.get("/users")
async def get_all_users():
	try:
		user_list = User.getall()
		return list(map(lambda r: ReadUser(**r), user_list))
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)

# used https://loadforge.com/guides/creating-your-first-endpoint-with-fastapi to figure out dynamic routing
@router.get("/users/{uuid}")
async def get_user(uuid: str):
	try:
		user = User.get(uuid)
		return user
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)

@router.post("/users")
async def create_user(user: WriteUser):
	try:
		uuid = User.create(user)
		user = User.get(uuid)
		return user
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)

@router.put("/users/{uuid}")
async def update_user(uuid: str, name: str):
	try:
		status = User.update(uuid, name)
		return status
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)

@router.delete("/users/{uuid}")
async def delete_user(uuid: str):
	try:
		status = User.delete(uuid)
		return status
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)
	
@router.post("/users/{uuid}/posts")
async def create_post(post: WriteUserPost):
	try:
		post_uuid = Post.create(post)
		post = Post.get(post_uuid)
		return post
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)

@router.get("/users/{uuid}/posts/{post_uuid}")
async def read_post(post_uuid: str):
	try:
		post = Post.get(post_uuid)
		return post
	except Exception as e:
		logger.error(e)
		raise HTTPException(status_code=500)