from sqlalchemy import create_engine, text

class DataBase:
    query = {
        'create_company': text('insert into company (name, description) values (:name, :description)'),
        'max_company_id': text('select MAX(id) from company'),
        'delete_company': text('delete from company where id = :company_id'),
        'list_SELECT': text('select * from employee where company_id = :id'),
        'item_SELECT': text('select * from employee where company_id = :c_id and id = e_id'),
        'maxID_SELECT': text('select * MAX(id) from employee where company_id = :c_id'),
        'item_DELETE': text('delete from employee where id = :id_delete'),
        'item_UPDATE': text('update employee set first_name = :new_name where id = :employer_id'),
        'item_INSERT': text(
            'insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)')       
    }

    """Инициализируем класс и двигатель БД"""

    def __init__(self, engine) -> None:
        self.db = create_engine(engine)

    # Создаем компанию в БД
    def create_company(self, company_name: str, description: str):
        try:
            with self.db.connect() as connection:
                 result = connection.execute(self.query['create_company'], parameters=dict(name=company_name, description=description))
            connection.commit()
            return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    # Удаляем компанию в БД
    def delete(self, company_id: int):
        try:
            with self.db.connect() as connection:
                connection.execute(self.query['delete_company'], parameters=dict(company_id=company_id))
                connection.commit()
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    # Получаем ID последней созданной компании
    def last_company_id(self):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['max_company_id']).fetchall()[0][0] 
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    # Получаем список сотрудников из БД
    def get_list_employer(self, company_id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['list_SELECT'], parameters=dict(id=company_id)).fetchall()[0][0]
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")
    
    # Создаем сотрудника в БД
    def create_employer(self, company_id: int, first_name: str, last_name: str, phone: str):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_INSERT'],
                                            parameters=dict(id=company_id, name=first_name, surname=last_name, phone_num=phone))
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")
    
    # Получаем ID сотрудника из БД
    def get_employer_id(self, company_id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['maxID_SELECT'], parameters=dict(c_id=company_id)).fetchall[0][0]
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")
    
    # Изменяем информацию о сотруднике в БД
    def update_employer_info(self, new_name: str, id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_UPDATE'],
                                            parameters=dict(new_name=new_name, employer_id=id))
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")
    
    # Удаляем сотрудника из БД
    def delete_employer(self, id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_DELETE'], parameters=dict(id_delete=id))
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")