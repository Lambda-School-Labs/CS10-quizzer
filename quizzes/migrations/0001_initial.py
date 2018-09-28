# Generated by Django 2.1.1 on 2018-09-26 20:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('ChoiceID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ChoiceText', models.TextField()),
                ('isCorrect', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'choices',
                'db_table': 'Choices',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('ClassID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ClassName', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'classes',
                'db_table': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Class_Quiz',
            fields=[
                ('Class_QuizID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('ClassID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Class')),
            ],
            options={
                'verbose_name_plural': 'Class_Quiz',
                'db_table': 'Class_Quiz',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('QuestionID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Question', models.TextField()),
                ('isMajor', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'questions',
                'db_table': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('QuizID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('QuizName', models.CharField(max_length=100)),
                ('Public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('Classes', models.ManyToManyField(to='quizzes.Class')),
            ],
            options={
                'verbose_name_plural': 'quizzes',
                'db_table': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestionChoice',
            fields=[
                ('QQCID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Choice')),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Question')),
                ('Quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=50)),
                ('StudentEmail', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('ClassID', models.ManyToManyField(to='quizzes.Class')),
            ],
            options={
                'verbose_name_plural': 'students',
                'db_table': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Student_Quiz',
            fields=[
                ('Student_QuizID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Grade', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('Quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Quiz')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Student')),
            ],
            options={
                'verbose_name_plural': 'Student_Quiz',
                'db_table': 'Student_Quiz',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TeacherID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TeacherEmail', models.CharField(max_length=256, unique=True)),
                ('TeacherName', models.CharField(max_length=50)),
                ('TeacherPW', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'teachers',
                'db_table': 'Teachers',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Teacher'),
        ),
        migrations.AddField(
            model_name='question',
            name='QuizID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Quiz'),
        ),
        migrations.AddField(
            model_name='class_quiz',
            name='QuizID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Quiz'),
        ),
        migrations.AddField(
            model_name='class',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Teacher'),
        ),
        migrations.AddField(
            model_name='choice',
            name='QuestionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Question'),
        ),
    ]
