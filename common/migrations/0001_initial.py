# Generated by Django 3.1.3 on 2022-02-10 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# 정방향 migrate 시
def forward_func(apps, schema_editor):
    # 모든 User에 대한 Profile 생성
    auth_user_model = settings.AUTH_USER_MODEL.split(',')  # 'auth.USER'
    User = apps.get_model(*auth_user_model)  # unpacking
    Profile = apps.get_model('common', 'Profile')

    for user in User.objects.all():
        print('Create profile for user#{}'.format(user.pk))
        Profile.objects.create(user=user)


# 역방향 migrate 시
def backward_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('stock_firm', models.CharField(choices=[('KIWOOM', '키움증권'), ('SAMSUNG', '삼성증권'), ('KOREA', '한국투자증권'), ('KOOKMIN', 'KB증권'), ('NONGHYUP', 'NH투자증권'), ('MIREA', '미래에셋증권'), ('SHINHAN', '신한금융투자'), ('ETC', '그 외')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(forward_func, backward_func),
    ]