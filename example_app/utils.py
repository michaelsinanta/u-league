from django.db import connection

def dict_fetch_all(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def get_user_role(username):    
    with connection.cursor() as cursor:
        # Check Manajer
        cursor.execute(f'''
            SELECT *
            FROM MANAJER
            WHERE username='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Manajer'
    
        # Check Panitia
        cursor.execute(f'''
            SELECT *
            FROM PANITIA
            WHERE username='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Panitia'
    
        # Check Penonton
        cursor.execute(f'''
            SELECT *
            FROM PENONTON
            WHERE username='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Penonton'      
    
    return 'none'

def get_user_id(username):
    with connection.cursor() as cursor:
        # Check Manajer
        cursor.execute(f'''
            SELECT id_manajer
            FROM MANAJER
            WHERE username='{username}';
        ''')
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        
        # Check Panitia
        cursor.execute(f'''
            SELECT id_panitia
            FROM PANITIA
            WHERE username='{username}';
        ''')
        result = cursor.fetchone()
        if result is not None:
            return result[0]
    
        # Check Penonton
        cursor.execute(f'''
            SELECT id_penonton
            FROM PENONTON
            WHERE username='{username}';
        ''')
        result = cursor.fetchone()
        if result is not None:
            return result[0]    
    
    return 'none'