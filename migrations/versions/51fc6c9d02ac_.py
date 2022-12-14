"""
Changed FilesData to UnsplashFilesData to remove conflict with FilesData table in image-uploader-project. I am deploying the application on the render.com with the same database as the image-uploader project

Revision ID: 51fc6c9d02ac
Revises: 948377292052
Create Date: 2022-12-20 20:44:36.836838

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '51fc6c9d02ac'
down_revision = '948377292052'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files_data',
                    sa.Column('file_name', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('public_id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('file_url', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('upload_date', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('timestamp', postgresql.DOUBLE_PRECISION(
                        precision=53), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint(
                        'file_name', name='files_data_pkey')
                    )
    # ### end Alembic commands ###
