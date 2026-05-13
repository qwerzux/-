from database.db_manager import get_connection

class Ticket:
    def __init__(self, id=None, user_id=None, operator_id=None, description=None, status='Новое',):
        self.id = id
        self.user_id = user_id
        self.operator_id = operator_id
        self.description = description
        self.status = status

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute('''
                INSERT INTO tickets (user_id, operator_id, description, status)
                VALUES (?, ?, ?, ?)
            ''', (self.user_id, self.operator_id, self.description, self.status))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE tickets SET user_id = ?, operator_id = ?, description = ?, status = ?
                WHERE id = ?
            ''', (self.user_id, self.operator_id, self.description, self.status, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tickets WHERE id = ?',
(self.id,))
            conn.commit()
            conn.close()

def get_all_tickets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, user_id, operator_id, description, status
        FROM tickets
    ''')
    rows = cursor.fetchall()
    conn.close()
    return [ 
        Ticket (
            id=row[0], user_id=row[1], operator_id=row[2], description=row[3], status=row[4]
        )
        for row in rows
    ]

def get_ticket_by_id(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, user_id, operator_id, description, status
        FROM tickets
        WHERE id = ?
    ''', (ticket_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Ticket (
            id=row[0], user_id=row[1], operator_id=row[2], description=row[3], status=row[4]
        )
    return None