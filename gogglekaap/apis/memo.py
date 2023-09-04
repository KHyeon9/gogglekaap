from flask import g

from flask_restx import Namespace, Resource, fields

from gogglekaap.models.memo import Memo as MemoModel
from gogglekaap.models.user import User as UserModel

ns = Namespace(
    'memos',
    description='메모 관련 API'
)

memo = ns.model(
    'Memo',
    {
        'id': fields.Integer(required=True, description='메모 고유 아이디'),
        'user_id': fields.Integer(required=True, description='유저 고유 아이디'),
        'title': fields.String(required=True, description='메모 제목'),
        'content': fields.String(required=True, description='메모 내용'),
        'created_at': fields.DateTime(description='메모 작성일'),
        'updated_at': fields.DateTime(description='메모 변경일'),
    }
)

@ns.route('')
class MemoList(Resource):
    @ns.marshal_list_with(memo, skip_none=True)
    def get(self):
        """메모 복수 조회"""
        data = MemoModel.query.join(
            UserModel,
            UserModel.id == MemoModel.user_id
        ).filter(
            UserModel.id == g.user.id
        ).order_by(
            MemoModel.created_at.desc()
        ).limit(10).all()

        return data

@ns.route('/<int:id>')
@ns.param('id', '메모 고유 아이디')
class Memo(Resource):
    @ns.marshal_list_with(memo, skip_none=True)
    def get(self, id):
        """메모 단수 조회"""
        memo = MemoModel.query.get_or_404(id)

        if g.user.id != memo.user_id:
            ns.abort(403)

        return memo