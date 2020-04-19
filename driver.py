from Employee import *

def main():
    # connect 
    engine = create_engine('sqlite:///:memory:', echo=False)
    
  
    Base.metadata.create_all(engine)
    
 
    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    

    # add objects
    session.add_all([
       Employee('Engineer', 'Billie', 'Muzzy', 5),
       Employee('Manager', 'Atlas', 'Muzzy', 3),
       Employee('Supervisor','Gizmo','Muzzy', 20),
       Employee('Engineer','Joel', 'Myhre', 32),
       Employee('Engineer','Tyler', 'Anthony', 120),
       Employee('Engineer','Julieann', 'Wheeler', 1)
        ])
    
    session.commit()
    
    # querying
    
    print("Order by first name:")
    for row in session.query(Employee).order_by(Employee.first_name):
        print(row.role, row.first_name, row.last_name, row.hours)
    
    print()
    print("Order by last name:")
    for row in session.query(Employee).order_by(Employee.last_name):
        print(row.role, row.first_name, row.last_name, row.hours)
        
    print()
    print("Order by hours:")
    for row in session.query(Employee).order_by(Employee.hours):
        print(row.role, row.first_name, row.last_name, row.hours)
    
    print()
    print("Employees with last name 'Muzzy'")
    for row in session.query(Employee).filter(Employee.last_name=='Muzzy'):
        print(row.role, row.first_name, row.last_name, row.hours)
        
        
    print()
    print("Employees with more than 5 hours of PTO")
    for row in session.query(Employee).filter(Employee.hours > 5):
        print(row.role, row.first_name, row.last_name, row.hours)
        
        
    print()
    print("Manager:")
    for row in session.query(Employee).filter(Employee.role == "Manager"):
        print(row.first_name, row.last_name)
    
    session.close()
    
main()