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


from .models import  CourseExpire
class CourseExpireModelAdmin(object):
    '''有效期价格管理类'''
    list_display = ["course","expire"]
xadmin.site.register(CourseExpire,CourseExpireModelAdmin)


from .models import  PriceDiscountType
class PriceDiscountTypeModelAdmin(object):
    '''价格优惠类型'''
    pass
xadmin.site.register(PriceDiscountType,PriceDiscountTypeModelAdmin)


from .models import  PriceDiscount
class PriceDiscountModelAdmin(object):
    '''价格优惠公式'''
    pass
xadmin.site.register(PriceDiscount,PriceDiscountModelAdmin)


from .models import  CoursePriceDiscount
class CoursePriceDiscountModelAdmin(object):
    '''课程与优惠模型'''
    pass
xadmin.site.register(CoursePriceDiscount,CoursePriceDiscountModelAdmin)


from .models import  Activity
class ActivityModelAdmin(object):
    '''活动模型'''
    pass
xadmin.site.register(Activity,ActivityModelAdmin)