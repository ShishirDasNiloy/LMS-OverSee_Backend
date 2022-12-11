"""added: userdetails, teacher, student, classroo, topic

Revision ID: 7bcebd4a20b3
Revises: 52cf0159c7d2
Create Date: 2022-12-11 17:52:46.191724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bcebd4a20b3'
down_revision = '52cf0159c7d2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topic',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('class_room_id', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('topic_name', sa.String(length=255), nullable=False),
    sa.Column('topic_type', sa.String(length=255), nullable=True),
    sa.Column('topic_details', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['class_room_id'], ['class_room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class_room_with_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('class_room_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_room_id'], ['class_room.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.String(length=20), nullable=True),
    sa.Column('admition_year', sa.Date(), nullable=True),
    sa.Column('batch', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.String(length=20), nullable=True),
    sa.Column('designation', sa.String(length=50), nullable=True),
    sa.Column('degree', sa.String(length=255), nullable=True),
    sa.Column('institute', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic_discuss',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('discussion_details', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('fathers_name', sa.String(length=100), nullable=True),
    sa.Column('mothers_name', sa.String(length=100), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('blood_group', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_details')
    op.drop_table('topic_discuss')
    op.drop_table('teachers')
    op.drop_table('students')
    op.drop_table('class_room_with_user')
    op.drop_table('topic')
    # ### end Alembic commands ###
