import aiosqlite


DB_PATH = "casino.db"


async def init_db(db: aiosqlite.Connection):
    async with db.cursor() as cur:
        await cur.execute("""
                            CREATE TABLE IF NOT EXISTS users (
                            user_id INT PRIMARY KEY,
                            balance INT DEFAULT 1000
                            )
                            """)
        await db.commit()


async def get_balance(db: aiosqlite.Connection, user_id: int) -> int:
    async with db.cursor() as cur:
        await cur.execute("""
                            SELECT balance
                            FROM users
                            WHERE user_id = ?""", (user_id,)
                          )
        user_balance = await cur.fetchone()


        if user_balance is not None:
            return user_balance[0]


        await cur.execute("""
                            INSERT INTO users (user_id, balance)
                            VALUES (?, 1000)""", (user_id,)
                          )
        await db.commit()
        
        return 1000
        

async def update_balance(db: aiosqlite.Connection, user_id: int, amount: int):
    async with db.cursor() as cur:

        await cur.execute("""
                          INSERT OR IGNORE INTO users (user_id)
                          VALUES (?)""", (user_id,)
                          )

        await cur.execute("""
                          UPDATE users
                          SET balance = MAX(0, balance + ?)
                          WHERE user_id = ?
                          """, (amount, user_id)
                          )
        await db.commit()


async def get_top_players(db: aiosqlite.Connection, limit: int) -> list:
    async with db.cursor() as cur:
        await cur.execute("""
                          SELECT user_id, balance
                          FROM users
                          ORDER BY balance DESC LIMIT ?""", (limit,))
        return list(await cur.fetchall())