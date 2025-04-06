from flask import Blueprint, request, jsonify
from models import db, Episode, Guest, Appearance
from sqlalchemy.exc import IntegrityError

routes = Blueprint('routes', __name__)

# GET /episodes
@routes.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": e.id,
        "date": e.date,
        "number": e.number
    } for e in episodes]), 200

# GET /episodes/<id>
@routes.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "guest_id": a.guest.id,
                "episode_id": a.episode.id,
                "guest": {
                    "id": a.guest.id,
                    "name": a.guest.name,
                    "occupation": a.guest.occupation
                }
            } for a in episode.appearances
        ]
    }), 200

# GET /guests
@routes.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        "id": g.id,
        "name": g.name,
        "occupation": g.occupation
    } for g in guests]), 200

# POST /appearances
@routes.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()

    rating = data.get("rating")
    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")

    try:
        new_appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(new_appearance)
        db.session.commit()

        return jsonify({
            "id": new_appearance.id,
            "rating": new_appearance.rating,
            "guest_id": new_appearance.guest.id,
            "episode_id": new_appearance.episode.id,
            "episode": {
                "id": new_appearance.episode.id,
                "date": new_appearance.episode.date,
                "number": new_appearance.episode.number
            },
            "guest": {
                "id": new_appearance.guest.id,
                "name": new_appearance.guest.name,
                "occupation": new_appearance.guest.occupation
            }
        }), 201

    except (ValueError, IntegrityError) as e:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400
