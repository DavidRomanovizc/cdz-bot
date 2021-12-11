import asyncpg

from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self, pool):
        self.pool: Pool = pool

    @classmethod
    async def create(cls):
        pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database="telegram_bot"
        )
        return cls(pool)

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        balance INTEGER DEFAULT 0 NOT NULL,
        is_premium bool NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user_Users(self, full_name, username, telegram_id, balance=0, is_premium=False):
        sql = '''INSERT INTO users (full_name, username, telegram_id, balance, is_premium)
                       VALUES($1, $2, $3, $4, $5) returning *'''
        return await self.execute(sql, full_name, username, telegram_id, balance, is_premium,
                                  fetchrow=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def check_premium(self, telegram_id):
        sql = "SELECT is_premium FROM Users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def update_premiun(self, is_premium, telegram_id, ):
        sql = "UPDATE Users SET is_premium=$1 WHERE telegram_id=$2"
        return await self.execute(sql, is_premium, telegram_id, execute=True)

    async def check_balance(self, telegram_id):
        sql = "SELECT balance FROM Users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def set_balance(self, telegram_id, money):
        sql = "UPDATE Users SET balance=$2 WHERE telegram_id=$1"
        return await self.execute(sql, money, telegram_id, execute=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_users_id(self):
        sql = "SELECT telegram_id FROM Users"
        return await self.execute(sql, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
