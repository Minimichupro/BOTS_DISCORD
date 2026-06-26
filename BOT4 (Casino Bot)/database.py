import aiosqlite


DB_PATH = "casino.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.cursor() as cur:
            await cur.execute("""
                              CREATE TABLE IF NOT EXISTS users (
                              user_id INT PRIMARY KEY,
                              balance INT DEFAULT 1000
                              )
                              """)
            await db.commit()


async def get_balance(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.cursor() as cur:
            await cur.execute("""
                              INSERT OR IGNORE INTO users (user_id)
                              VALUES (?)""", (user_id,)
                              )
                
            await cur.execute("""
                              SELECT balance
                              FROM users
                              WHERE user_id = ?""", (user_id,)
                              )
            user_balance = await cur.fetchone()
                
            await db.commit()

            # fetchone() can return None in some error cases; fall back to default balance
            if user_balance is None:
                return 1000

            return user_balance[0]
        

async def update_balance(user_id, amount):
    async with aiosqlite.connect(DB_PATH) as db:
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


async def get_top_players(limit: int) -> list: 
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.cursor() as cur:

            await cur.execute("""
                              SELECT user_id, balance
                              FROM users
                              ORDER BY balance DESC LIMIT ?""", (limit,))
            
            return list(await cur.fetchall())