from app import create_app
from models import db, Episode, Guest, Appearance

app = create_app()

with app.app_context():
    # Create some sample guests
    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")
    
    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    # Create some sample episodes
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)
    
    db.session.add_all([episode1, episode2])
    db.session.commit()

    # Create some sample appearances
    appearance1 = Appearance(rating=5, episode_id=episode1.id, guest_id=guest1.id)
    appearance2 = Appearance(rating=4, episode_id=episode2.id, guest_id=guest2.id)
    appearance3 = Appearance(rating=3, episode_id=episode2.id, guest_id=guest3.id)

    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()

    print("Database seeded successfully!")
