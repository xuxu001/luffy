# -*- coding:utf-8 -*-
import xadmin
from .models import CourseCategory
class CourseCategoryModelAdmin(object):
    '''课程分类模型管理类'''
    pass
xadmin.site.register(CourseCategory,CourseCategoryModelAdmin)

from .models import Course
class CourseModelAdmin(object):
    '''课程模型管理类'''
    pass
xadmin.site.register(Course,CourseModelAdmin)

from .models import Teacher
class TeacherModelAdmin(object):
    '''导师模型管理类'''
    pass
xadmin.site.register(Teacher,TeacherModelAdmin)

from .models import CourseChapter
class CourseChapterModelAdmin(object):
    '''课程章节管理类'''
    pass
xadmin.site.register(CourseChapter,CourseChapterModelAdmin)

from .models import CourseLesson
class CourseLessonModelAdmin(object):
    '''课时时长管理类'''
    pass
xadmin.site.register(CourseLesson,CourseLessonModelAdmin)