# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mess(models.Model):
    mess_name = models.CharField(primary_key=True, max_length=32)
    person_in_charge = models.CharField(max_length=32, blank=True, null=True)
    mess_contact = models.CharField(max_length=10, blank=True, null=True)
    block_in = models.ForeignKey('Block', models.DO_NOTHING, db_column='block_in', blank=True, null=True)

    class Meta:
        
        db_table = 'mess'


class Block(models.Model):
    block_no = models.CharField(primary_key=True, max_length=5)
    block_name = models.CharField(max_length=25, blank=True, null=True)
    no_of_floors = models.IntegerField(blank=True, null=True)
    warden_on_duty = models.ForeignKey('Warden', models.DO_NOTHING, db_column='warden_on_duty', blank=True, null=True)

    class Meta:
        
        db_table = 'block'


class Parent(models.Model):
    p_name = models.CharField(primary_key=True, max_length=32)
    p_contact = models.CharField(max_length=10, blank=True, null=True)
    p_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'parent'


class Student(models.Model):
    reg_no = models.CharField(primary_key=True, max_length=9)
    s_name = models.CharField(max_length=32, blank=True, null=True)
    s_address = models.CharField(max_length=50, blank=True, null=True)
    s_contact = models.CharField(max_length=10, blank=True, null=True)
    s_dob = models.DateField(blank=True, null=True)
    s_school = models.CharField(max_length=10, blank=True, null=True)
    s_program = models.CharField(max_length=10, blank=True, null=True)
    s_mess = models.ForeignKey(Mess, models.DO_NOTHING, db_column='s_mess', blank=True, null=True)
    parent_name = models.ForeignKey(Parent, models.DO_NOTHING, db_column='parent_name', blank=True, null=True)
    s_room_no = models.ForeignKey('Room', models.DO_NOTHING, db_column='s_room_no', blank=True, null=True)

    class Meta:
        
        db_table = 'student'


class Room(models.Model):
    room_no = models.CharField(primary_key=True, max_length=5)
    room_type = models.CharField(max_length=30, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    block_num = models.ForeignKey(Block, models.DO_NOTHING, db_column='block_num', blank=True, null=True)

    class Meta:
        
        db_table = 'room'


class Warden(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=7)
    w_name = models.CharField(max_length=32, blank=True, null=True)
    w_dob = models.DateField(blank=True, null=True)
    w_address = models.CharField(max_length=50, blank=True, null=True)
    w_contact = models.CharField(max_length=10, blank=True, null=True)
    w_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'warden'


    s_reg_no = models.ForeignKey(Student, models.DO_NOTHING, db_column='s_reg_no', blank=True, null=True)
    reason = models.CharField(max_length=25, blank=True, null=True)
    place_of_visit = models.CharField(max_length=15, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey(Warden, models.DO_NOTHING, db_column='approved_by', blank=True, null=True)

    class Meta:
        
        db_table = 'leave_application'
