from database.db_manager import get_connection

class Operator:
    def __init__(self, id=None, full_name = None, position = None, phone = None):
        self.id = id
        self.full_name = full_name
        self.position = position
        self.phone = phone

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO operators (full_name, position, phone)
                VALUES (?, ?, ?)
            ''', (self.full_name, self.position, self.phone))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE operators SET full_name = ?, position = ?, phone = ?
                WHERE id = ?
            ''', (self.full_name, self.position, self.phone))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM operators WHERE id = ?', (self.id))
            conn.commit()
            conn.close()

def get_all_operators():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, full_name, position, phone
        FROM operators
    ''')

    rows = cursor.fetchall()
    conn.close()
    return [
        Operator (
            id=row[0], 
            full_name=row[1], 
            position=row[2], 
            phone=row[3]
        )
        for row in rows
    ]

def get_operator_by_id(operator_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, full_name, position, phone
        FROM operators
        WHERE id = ?
    ''', (operator_id,))
    row = cursor.fetchall()
    conn.close()

    if row:
        return Operator (
            id=row[0], 
            full_name=row[1], 
            position=row[2], 
            phone=row[3]
        )
    
    return None