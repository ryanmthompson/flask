__author__ = 'rthompson'

from database_models import Group, Role, Site, User
from werkzeug.security import generate_password_hash, check_password_hash

def build_sample_db(db):
    """
    Populate a small db with some example entries.
    """

    import string
    import random

    db.drop_all()
    db.create_all()
    # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(login="test", password="test")
    test_user = User(login="test", password=generate_password_hash("test"))
    db.session.add(test_user)

    firstNames = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    lastNames = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    for i in range(len(firstNames)):
        user = User()
        user.firstName = firstNames[i]
        user.lastName = lastNames[i]
        user.login = user.firstName.lower()
        user.email = user.login + "@example.com"
        user.password = generate_password_hash(''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)))
        db.session.add(user)

    roles = [
        Role(name = 'ACINT', description = 'Acoustic Intelligence'),
        Role(name = 'C-HUMINT', description = 'Counter Human Resources Intelligence'),
        Role(name = 'C-IMINT', description = 'Counter Imagery Intelligence'),
        Role(name = 'C-MASINT', description = 'Counter-Measures and Signature Intelligence'),
        Role(name = 'COMINT', description = 'Communications Intelligence'),
        Role(name = 'DATAINT', description = 'Data Intelligence'),
        Role(name = 'ELINT', description = 'Electronic Intelligence'),
        Role(name = 'EMINT', description = 'Emissions Intelligence'),
        Role(name = 'EOINT', description = 'Electro-Optical Intelligence'),
        Role(name = 'FSINT', description = 'Foreign Instrumentation and Signature Intelligence'),
        Role(name = 'GEOINT', description = 'Geospatial Intelligence'),
        Role(name = 'HUMINT', description = 'Human Resources Intelligence'),
        Role(name = 'IMINT', description = 'Imagery Intelligence'),
        Role(name = 'IRINT', description = 'Infrared Intelligence'),
        Role(name = 'ISINT', description = 'Infrared Intelligence'),
        Role(name = 'LASINT', description = 'Laser Intelligence'),
        Role(name = 'LITINT', description = 'Literature Intelligence'),
        Role(name = 'MASINT', description = 'Measurement and Signature Intelligence'),
        Role(name = 'MEDINT', description = 'Medical Intelligence'),
        Role(name = 'NUCINT', description = 'Nuclear Intelligence'),
        Role(name = 'OPELINT', description = 'Operational Electronic Intelligence'),
        Role(name = 'OPINT', description = 'Optical Intelligence'),
        Role(name = 'ORBINT', description = 'Orbital Intelligence'),
        Role(name = 'OSINT', description = 'Open Source Intelligence'),
        Role(name = 'PHOTOINT', description = 'Photographic Intelligence'),
        Role(name = 'RADINT', description = 'Radar Intelligence'),
        Role(name = 'SIGINT', description = 'Signals Intelligence'),
        Role(name = 'SOINT', description = 'Staff Officer Intelligence'),
        Role(name = 'TECHELINT', description = 'Technical ELINT'),
        Role(name = 'TECHINT', description = 'Technical Intelligence'),
        Role(name = 'TELINT', description = 'Telemetry Intelligence'),
        Role(name = 'TGTINT', description = 'Targeting Intelligence'),
        Role(name = 'VIDINT', description = 'Video Intelligence'),
        Role(name = 'VISINT', description = 'Visual Intelligence'),
    ]

    for r in roles:
        db.session.add(r)

    db.session.commit()
    return
