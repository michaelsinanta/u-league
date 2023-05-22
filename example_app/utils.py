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
    
        # Check Courier
        cursor.execute(f'''
            SELECT *
            FROM PANITIA
            WHERE username='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Panitia'
    
        # Check Customer
        cursor.execute(f'''
            SELECT *
            FROM PENONTON
            WHERE username='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Penonton'      
    
    return 'none'