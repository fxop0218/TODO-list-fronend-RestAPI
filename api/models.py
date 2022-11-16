from database import db

user_task = db.Table(
    "user_table",
    db.Column("user_id", db.Integer, db.ForeignKey("user_.id")),
    db.Column("task_id", db.Integer, db.ForeignKey("task.id")),
)


class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(252), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime)
    closed = db.Column(db.DateTime)

    def __str__(self) -> str:
        return (
            f"Id: {self.id} "
            f"Id: {self.title} "
            f"Id: {self.text} "
            f"Id: {self.created} "
            f"Id: {self.closed} "
        )


class user_(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    task_list = db.relationship("task", secondary=user_task, backref="users")

    def __str__(self) -> str:
        return f"ID: {self.id} " f"Username: {self.username} "
