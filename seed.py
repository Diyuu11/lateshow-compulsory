from app import app
from models import db, Guest, Episode, Appearance

with app.app_context():
    print("🌱 Seeding database...")

    db.drop_all()
    db.create_all()

    # Add guests
    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    g3 = Guest(name="Tracey Ullman", occupation="television actress")

    db.session.add_all([g1, g2, g3])
    db.session.commit()

    # Add episodes
    e1 = Episode(date="1/11/99", number=1)
    e2 = Episode(date="1/12/99", number=2)

    db.session.add_all([e1, e2])
    db.session.commit()

    # Add appearances
    a1 = Appearance(rating=4, episode_id=e1.id, guest_id=g1.id)
    a2 = Appearance(rating=5, episode_id=e2.id, guest_id=g3.id)

    db.session.add_all([a1, a2])
    db.session.commit()

    print("✅ Done seeding!")
