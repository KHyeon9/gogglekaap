from sqlalchemy import func

from gogglekaap.exts import db

memos_labels = db.Table(
    'memos_labels',
    db.Column('memd_id', db.Integer, db.ForeignKey('memo.id'), primary_key=True),
    db.Column('label_id', db.Integer, db.ForeignKey('label.id'), primary_key=True),
)

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    linked_image = db.Column(db.String(200), nullable=True)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    created_at = db.Column(db.DateTime(),default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(),
        default=func.now(),
        onupdate=func.now()
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'user.id',
            ondelete='CASCADE'
        ),
        nullable=False
    )

    labels = db.relationship(
        'Label', # 라벨과의 연관성을 가짐
        secondary = memos_labels, # N:M 관계 테이블을 참조
        backref = db.backref('memos') # Label 객체에도 memos객체에 접근하도록 처리하라
    )