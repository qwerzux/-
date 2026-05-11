from database.db_manager import get_connection


class User:
    def __init__(self, id=None, full_name=None, email=None, phone=None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone = phone

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute("""
                INSERT INTO users (full_name, email, phone)
                VALUES (?, ?, ?)
            """, (self.full_name, self.email, self.phone))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE users
                SET full_name = ?, email = ?, phone = ?
                WHERE id = ?
            """, (self.full_name, self.email, self.phone, self.id))

        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name, email, phone
        FROM users
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        User(
            id=row[0],
            full_name=row[1],
            email=row[2],
            phone=row[3]
        )
        for row in rows
    ]


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name, email, phone
        FROM users
        WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return User(
            id=row[0],
            full_name=row[1],
            email=row[2],
            phone=row[3]
        )

    return None