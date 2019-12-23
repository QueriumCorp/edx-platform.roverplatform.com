from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from lms.djangoapps.grades.subsection_grade_factory import SubsectionGradeFactory
from lms.djangoapps.grades.course_grade import CourseGrade
from lms.djangoapps.grades.course_data import CourseData


from opaque_keys.edx.keys import CourseKey, UsageKey
from common.djangoapps.third_party_auth.lti_consumers.willolabs.exceptions import LTIBusinessRuleError

import logging
log = logging.getLogger(__name__)

def parent_usagekey(
    user,
    course_id=None, 
    course_key=None,
    usage_id=None, 
    usage_key=None, 
    usage_key_string=None
    ):
    """
    Returns the UsageKey of the homework assignment containing the usage_key that was passed.
    This method assumes that the usage_key passed points to a homework problem.
    """
    log.info('parent_usagekey()')
    if course_key is None and course_id is not None:
        course_key = CourseKey.from_string(course_id)

    if usage_key is None and usage_id is not None:
        usage_key = UsageKey.from_string(usage_id)
    else:
        if usage_key is None and usage_key_string is not None:
            usage_key = UsageKey.from_string(usage_key_string)

    if course_key is None:
        raise LTIBusinessRuleError("Did not receive a valid course_key object nor identifier.")

    if usage_key is None:
        raise LTIBusinessRuleError("Did not receive a valid usage_key object nor identifier.")

    problem_key_string = 'block-v1:' + usage_key._to_string()

    course_data = CourseData(
        user=user, 
        course=None, 
        collected_block_structure=None, 
        structure=None, 
        course_key=course_key
        )
    
    course_grade = CourseGradeFactory().read(
        user=user, 
        course_key=course_key
        )

    for chapter in course_grade.chapter_grades.itervalues():
        for section in chapter['sections']:
            grades_factory = SubsectionGradeFactory(
                student=user, 
                course=None, 
                course_structure=None, 
                course_data=course_data
                )
            subsection_grades = grades_factory.create(
                subsection=section, 
                read_only=True
                )

            for problem_key_BlockUsageLocator, problem_ProblemScore in subsection_grades.problem_scores.items():
                if str(problem_key_BlockUsageLocator) == problem_key_string:
                    retval = '/courses/' + course_key.html_id() + '/courseware/' + chapter['url_name'] + '/' + section.url_name
                    log.info(retval)
                    return retval

    raise LTIBusinessRuleError("Did not find problem_key_string {problem_key_string} in the grade data for course {course_id}".format(
        course_id = course_key.html_id(),
        problem_key_string = problem_key_string
    ))
    return None