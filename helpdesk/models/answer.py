from database.db_manager import get_connection

class Answer:
    def __init__(self, id=None, ticket_id=None, answer_text=None):
        self.id = id
        self.ticket_id = ticket_id
        self.answer_text = answer_text

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute('''
                INSERT INTO answers (ticket_id, answer_text)
                VALUES (?, ?)
            ''', (self.ticket_id, self.answer_text))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE answers
                SET ticket_id = ?, answer_text = ?
                WHERE id = ?
            ''', (self.ticket_id, self.answer_text, self.id))

        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM answers WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()


def get_answers_by_ticket_id(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, ticket_id, answer_text
        FROM answers
        WHERE ticket_id = ?
    """, (ticket_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        Answer(
            id=row[0],
            ticket_id=row[1],
            answer_text=row[2]
        )
        for row in rows
    ]
def delete(self):
    if self.id is not None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM answers WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
        
def get_answer_by_id(answer_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, ticket_id, answer_text
        FROM answers
        WHERE id = ?
    """, (answer_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return Answer(
            id=row[0],
            ticket_id=row[1],
            answer_text=row[2]
        )

    return None