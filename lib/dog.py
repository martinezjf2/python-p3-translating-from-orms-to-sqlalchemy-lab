from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)
    pass
    
def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs
    pass

def find_by_name(session, name):
    dogs_by_name = session.query(Dog).filter(Dog.name == name).first()
    return dogs_by_name
    pass

def find_by_id(session, id):
    dog_by_id = session.query(Dog).filter(Dog.id == id).first()
    return dog_by_id
    pass

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog
    pass

def update_breed(session, dog, breed):
    dog = session.query(Dog).filter(Dog.name == dog.name).first()
    dog.breed = breed    
    return dog
    pass