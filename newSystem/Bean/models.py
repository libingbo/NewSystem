# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Glyhccyhjlb(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    glyhgh = models.ForeignKey('Xwglyhb', models.DO_NOTHING, db_column='GLYHGH', blank=True, null=True)  # Field name made lowercase.
    yhm = models.CharField(db_column='YHM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sfbs = models.IntegerField(db_column='SFBS', blank=True, null=True)  # Field name made lowercase.
    zxsj = models.DateTimeField(db_column='ZXSJ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'GLYHCCYHJLB'


class Llyhlljlb(models.Model):
    #这里外键默认关联的是表的主键(id)  , 所以你看到的时候改了 , 改成unique的列
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    xwid = models.ForeignKey('Xwnrb', models.DO_NOTHING, db_column='XWID', blank=True, null=True)  # Field name made lowercase.
    yhm = models.ForeignKey('Xwllyhb', models.DO_NOTHING, db_column='YHM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LLYHLLJLB'


class Xwfbyhb(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   #Field name made lowercase.
    yhm = models.CharField(db_column='YHM', unique=True, max_length=60)  # Field name made lowercase.
    mm = models.CharField(db_column='MM', max_length=60)  # Field name made lowercase.
    qx = models.CharField(db_column='QX', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sr = models.DateTimeField(db_column='SR', blank=True, null=True)  # Field name made lowercase.
    xb = models.CharField(db_column='XB', max_length=6, blank=True, null=True)  # Field name made lowercase.
    gxqm = models.CharField(db_column='GXQM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tx = models.CharField(db_column='TX', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'XWFBYHB'


class Xwglyhb(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    xm = models.CharField(db_column='XM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sr = models.DateTimeField(db_column='SR', blank=True, null=True)  # Field name made lowercase.
    gh = models.CharField(db_column='GH', unique=True, max_length=16)  # Field name made lowercase.
    lxfs = models.CharField(db_column='LXFS', max_length=11)  # Field name made lowercase.
    xb = models.CharField(db_column='XB', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'XWGLYHB'


class Xwllyhb(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yhm = models.CharField(db_column='YHM', unique=True, max_length=60)  # Field name made lowercase.
    mm = models.CharField(db_column='MM', max_length=60)  # Field name made lowercase.
    qx = models.CharField(db_column='QX', max_length=6)  # Field name made lowercase.
    sr = models.DateTimeField(db_column='SR', blank=True, null=True)  # Field name made lowercase.
    xb = models.CharField(db_column='XB', max_length=6, blank=True, null=True)  # Field name made lowercase.
    gxqm = models.CharField(db_column='GXQM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tx = models.CharField(db_column='TX', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'XWLLYHB'


class Xwnrb(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fl = models.IntegerField(db_column='FL')  # Field name made lowercase.
    bt = models.CharField(db_column='BT', max_length=60)  # Field name made lowercase.
    dy = models.CharField(db_column='DY', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nr = models.TextField(db_column='NR')  # Field name made lowercase.
    tp = models.CharField(db_column='TP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shzt = models.IntegerField(db_column='SHZT', blank=True, null=True)  # Field name made lowercase.
    shjg = models.IntegerField(db_column='SHJG', blank=True, null=True)  # Field name made lowercase.
    llcs = models.IntegerField(db_column='LLCS', blank=True, null=True)  # Field name made lowercase.
    dzcs = models.IntegerField(db_column='DZCS', blank=True, null=True)  # Field name made lowercase.
    plcs = models.IntegerField(db_column='PLCS', blank=True, null=True)  # Field name made lowercase.
    rdz = models.FloatField(db_column='RDZ', blank=True, null=True)  # Field name made lowercase.
    fbzyhm = models.ForeignKey(to= Xwfbyhb , to_field='yhm', on_delete=models.SET , db_column='FBZYHM', max_length=60 , null=False)  # Field name made lowercase.
    fbsj = models.DateTimeField(db_column='FBSJ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'XWNRB'

'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:

        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:

        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'
'''