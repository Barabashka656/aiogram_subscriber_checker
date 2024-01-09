from bot.utils.database import async_session_maker
from bot.dao.base import BaseDAO
from bot.handlers.models import ArticleModel
from bot.handlers.schemas import Article

from sqlalchemy import or_


class ArticleDAO(BaseDAO):
    model = ArticleModel

class ArticleService:
    @staticmethod
    async def add_article(article_title: str, article_link: str) -> bool:
        async with async_session_maker() as session:
            link_in_db: Article = await ArticleDAO.find_one_or_none(
                session, 
                or_(ArticleModel.link == article_link, 
                    ArticleModel.title == article_title)
            )
            if link_in_db:
                return False

            await ArticleDAO.add(
                session,
                obj_in=Article(
                    link=article_link,
                    title=article_title
                )
            )
            await session.commit()
        return True
    @staticmethod
    async def delete_article(
        article: str | None
    ):
        async with async_session_maker() as session:
            article_obj = await ArticleDAO.find_one_or_none(
                session,
                ArticleModel.title == article
            )
            if article_obj:
                await ArticleDAO.delete(
                    session,
                    ArticleModel.title == article
                )
                await session.commit()
                return 'Статья удалена успешно'
            article_obj = await ArticleDAO.find_one_or_none(
                session,
                ArticleModel.link == article
            )  
            if article_obj:
                await ArticleDAO.delete(
                    session,
                    ArticleModel.link == article
                )
                await session.commit()
                return 'Статья удалена успешно'
            
            return f'Нет статьи "{article}"'
            
    @staticmethod
    async def get_articles():
        async with async_session_maker() as session:
            articles: list[Article] = await ArticleDAO.find_all(
                session
            )
        return articles

from bot.handlers.schemas import User
from bot.utils.database import async_session_maker

from bot.dao.base import BaseDAO
from bot.handlers.models import UserModel

class UserDAO(BaseDAO):
    model = UserModel

class UserService:
    @staticmethod
    async def new_user(user_id: int):
        async with async_session_maker() as session:
            user_exist: User = await UserDAO.find_one_or_none(session, user_id=user_id)
            
            if user_exist and not user_exist.is_active:
                return await UserService.activate_user(user_id)
    
            db_user = await UserDAO.add(
                session,
                obj_in=User(
                    user_id=user_id,
                )
            )
            await session.commit()
        return db_user

    @staticmethod
    async def get_all_users() -> list[User]:
        async with async_session_maker() as session:
            return await UserDAO.find_all(session)

    @staticmethod
    async def activate_user(user_id: int):
        async with async_session_maker() as session:
            await UserDAO.update(
                session,
                user_id == user_id,
                obj_in=User(
                    is_active=True
                )
            )
            await session.commit()

    @staticmethod
    async def deactivate_user(user_id: int):
        async with async_session_maker() as session:
            await UserDAO.update(
                session,
                UserModel.user_id == user_id,
                obj_in=User(
                    is_active=False,
                )
            )
            await session.commit()
