# Generated by Django 2.1.7 on 2019-11-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('image', models.ImageField(blank=True, help_text='图片大小：1920*720', null=True, upload_to='banner', verbose_name='轮播图')),
                ('name', models.CharField(max_length=150, verbose_name='轮播图名称')),
                ('note', models.CharField(max_length=150, verbose_name='备注信息')),
                ('link', models.CharField(max_length=150, verbose_name='轮播图广告地址')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='NavInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='导航栏名称')),
                ('link', models.CharField(max_length=250, verbose_name='导航栏地址')),
                ('opt', models.SmallIntegerField(choices=[(1, 'top'), (2, 'footer')], default=1, verbose_name='位置')),
            ],
            options={
                'verbose_name': '导航菜单',
                'verbose_name_plural': '导航菜单',
                'db_table': 'lv_nav',
            },
        ),
    ]
